/**
 * Autorización en la INTERFAZ (UX honesta): no mostramos una acción que el
 * server va a rechazar con 403. La SEGURIDAD real vive en el server.
 *
 *   | helper              | admin | editor | viewer |
 *   |---------------------|:-----:|:------:|:------:|
 *   | scopeAllowsWrite    |  ✅   |   ✅   |   ❌   |  (depende del TOKEN)
 *   | canManageUsers      |  ✅   |   ❌   |   ❌   |
 *   | canChangeRole       |  ✅   |   ❌   |   ❌   |
 *   | canDelete           |  ✅   |   ❌   |   ❌   |
 *   | canEdit             |  ✅   | solo lo suyo | solo lo suyo |
 *   | canPublish          |  ✅   | solo lo suyo | solo lo suyo |
 */

import type { DocumentRead, Role } from "./types";

/** ¿Este TOKEN puede escribir? "read write" contiene "write"; "read" no. */
export function scopeAllowsWrite(scope: string | undefined): boolean {
  return scope?.split(" ").includes("write") ?? false;
}

/** ¿Puede ver el panel de usuarios (GET /api/users)? Solo admin. */
export function canManageUsers(role: Role | undefined): boolean {
  return role === "admin";
}

/** ¿Puede cambiar el rol de otro usuario? Solo admin. */
export function canChangeRole(role: Role | undefined): boolean {
  return role === "admin";
}

/** ¿Puede BORRAR documentos? Solo admin. */
export function canDelete(role: Role | undefined): boolean {
  return role === "admin";
}

/** ¿Puede EDITAR un documento? Dueño o admin. */
export function canEdit(userId: number, doc: DocumentRead, role: Role | undefined): boolean {
  return doc.owner_id === userId || role === "admin";
}

/** ¿Puede PUBLICAR un documento? Dueño o admin. */
export function canPublish(userId: number, doc: DocumentRead, role: Role | undefined): boolean {
  return doc.owner_id === userId || role === "admin";
}