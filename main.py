from utils.logger import init_logger
from utils.reader import read_config
from schemes.config_scheme import ConfigScheme

def main() -> None:
    config: ConfigScheme = read_config("./config.json")

    init_logger(config["log"])

if __name__ == "__main__":
    main()