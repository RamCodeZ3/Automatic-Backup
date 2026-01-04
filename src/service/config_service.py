import json
import os


class ConfigService:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.PATH = os.path.join(base_dir, "config", "config.json")
        self.config = self._load()

    def _load(self):
        if not os.path.exists(self.PATH):
            self.config = self._default_config()
            self.save()
            return self.config

        with open(self.PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def _default_config(self):
        return {
            "backupType": "local",
            "backupInterval": "monthly",
            "backupPath": "path",
            "firstTime": True
        }

    def get_key_value(self, key):
        return self.config.get(key)

    def set_json(self, key, value):
        self.config[key] = value
        self.save()

    def save(self):
        os.makedirs(os.path.dirname(self.PATH), exist_ok=True)
        with open(self.PATH, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)
