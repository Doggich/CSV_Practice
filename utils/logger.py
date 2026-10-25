import logging
from pathlib import Path

def init_logger(log_path: str | Path) -> None:
    path: Path = Path(log_path)
    
    path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=str(path.resolve()),
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
        filemode="a",
        force=True
    )


