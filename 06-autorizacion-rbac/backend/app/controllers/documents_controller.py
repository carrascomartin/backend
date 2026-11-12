"""
Controller de DOCUMENTOS — el recurso protegido (scopes + tenancy + object-level).

Orden de checks en cada endpoint de un documento puntual:
    1. 404 si no existe
    2. 403 tenancy (otra empresa)
    3. 403 object-level (dueño o admin)
"""

from fastapi import APIRouter, Depends, HTTPException, status

from app import storage
from app.dependencies import get_current_user, require_role, require_scope
from app.models import DocumentCreate, DocumentRead, DocumentUpdate, Role, User

router = APIRouter(prefix="/api", tags=["3 · Documentos"])


def _forbidden(detail: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


def _is_owner_or_admin(user: User, doc) -> bool:
    # El rol sale del USUARIO (fresco de storage), no del token.
    return doc.owner_id == user.id or user.role == Role.ADMIN


@router.post(
    "/documents",
    response_model=DocumentRead,
    status_code=status.HTTP_201_CREATED,
)
def create_document(
    body: DocumentCreate,
    current_user: User = Depends(require_scope("write")),
):
    """Crea un documento: draft privado a nombre tuyo, en TU empresa."""
    return storage.create_document(owner=current_user, body=body)


@router.get("/documents", response_model=list[DocumentRead])
def list_documents(
    current_user: User = Depends(get_current_user),
):
    """Lista lo que PODÉS ver: públicos de tu empresa + tus documentos."""
    return storage.list_documents(
        tenant_id=current_user.tenant_id,
        user_id=current_user.id,
    )


@router.get("/documents/{doc_id}", response_model=DocumentRead)
def get_document(
    doc_id: int,
    current_user: User = Depends(get_current_user),
):
    """Ve un documento por id (IDOR mitigado)."""
    doc = storage.get_document(doc_id)
    if doc is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Documento no encontrado")
    # Tenancy: por encima de todo, incluso en documentos públicos.
    if doc.tenant_id != current_user.tenant_id:
        raise _forbidden("No podés ver documentos de otra empresa")
    if doc.visibility == "public":
        return doc
    if _is_owner_or_admin(current_user, doc):
        return doc
    raise _forbidden("No podés ver este documento")


@router.patch("/documents/{doc_id}", response_model=DocumentRead)
def update_document(
    doc_id: int,
    body: DocumentUpdate,
    current_user: User = Depends(require_scope("write")),
):
    """Edita un documento: solo el DUEÑO o un ADMIN de la empresa."""
    doc = storage.get_document(doc_id)
    if doc is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Documento no encontrado")
    if doc.tenant_id != current_user.tenant_id:
        raise _forbidden("No podés editar documentos de otra empresa")
    if not _is_owner_or_admin(current_user, doc):
        raise _forbidden("No podés editar este documento")
    return storage.update_document(doc_id, body)


@router.delete("/documents/{doc_id}", response_model=DocumentRead)
def delete_document(
    doc_id: int,
    _admin: User = Depends(require_role(Role.ADMIN)),
    current_user: User = Depends(require_scope("write")),
):
    """Borra un documento: SOLO admin, con scope write, y de su empresa."""
    doc = storage.get_document(doc_id)
    if doc is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Documento no encontrado")
    if doc.tenant_id != current_user.tenant_id:
        raise _forbidden("No podés borrar documentos de otra empresa")
    deleted = storage.delete_document(doc_id)
    return deleted


@router.post("/documents/{doc_id}/publish", response_model=DocumentRead)
def publish_document(
    doc_id: int,
    current_user: User = Depends(require_scope("write")),
):
    """Publica un documento: el DUEÑO publica lo suyo; el admin, cualquiera de su empresa."""
    doc = storage.get_document(doc_id)
    if doc is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Documento no encontrado")
    if doc.tenant_id != current_user.tenant_id:
        raise _forbidden("No podés publicar documentos de otra empresa")
    if not _is_owner_or_admin(current_user, doc):
        raise _forbidden("No podés publicar este documento")
    return storage.set_document_published(doc_id, True)