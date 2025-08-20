
# ./config/config.py

import yaml
from functools import lru_cache
from utils.path_utils import find_root_dir, get_path



# load config.yaml
@lru_cache(maxsize=1)
def load_config(reload: bool = False) -> dict:
    if reload:
        load_config.cache_clear() # clear cache if forced reload
    
    ROOT_DIR = find_root_dir()
    CONFIG_PATH = ROOT_DIR.joinpath("config", "config.py")

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"config file not found at {CONFIG_PATH}")

    with open(file=CONFIG_PATH, mode="r", encoding="utf-8") as file:
        return yaml.safe_load(file)


# root directory
ROOT_DIR = find_root_dir()
CONFIG_PATH = ROOT_DIR.joinpath("config", "config.py")

config = load_config()

# Diretories
DATA_DIR = get_path(config["paths"]["data"])
MODEL_DIR = get_path(config["paths"]["model"])
LOG_DIR = get_path(config["paths"]["logs"])




