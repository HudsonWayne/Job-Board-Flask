# config.py

import os

class Config:
    SECRET_KEY = os.environ.get("HudsonWayne") or "your-default-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
