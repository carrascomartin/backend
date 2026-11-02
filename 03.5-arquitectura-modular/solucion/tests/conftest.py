"""pytest config: asegura que la raíz del backend esté en sys.path."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
