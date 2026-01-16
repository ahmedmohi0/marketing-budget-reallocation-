from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Paths:
    root: Path
    raw: Path
    processed: Path

def get_paths(root: str | Path = ".") -> Paths:
    root = Path(root).resolve()
    return Paths(
        root=root,
        raw=root / "data" / "raw",
        processed=root / "data" / "processed",
    )
