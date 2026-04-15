import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "language": "es",
    "theme": "dark",
    "currency": "COP",
    "company": "Mi Negocio"
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)