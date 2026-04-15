import json
from app.core.config import load_config

def get_texts():
    config = load_config()
    lang = config["language"]

    with open(f"app/i18n/{lang}.json", encoding="utf-8") as f:
        return json.load(f)