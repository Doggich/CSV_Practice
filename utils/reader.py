from pathlib import Path
import json
from schemes.config_scheme import ConfigScheme


# когда проверял работу модуля отдельно от main.py
# import sys
# PROJECT_ROOT = Path(__file__).resolve().parent.parent
# if str(PROJECT_ROOT) not in sys.path:
#     sys.path.insert(0, str(PROJECT_ROOT))


def read_config(config_path: str | Path) -> ConfigScheme | Exception:
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не существует")
    with open(file=path, mode="r", encoding="utf-8") as f:
        raw_data = json.load(f)
            
    return ConfigScheme(**raw_data) 

