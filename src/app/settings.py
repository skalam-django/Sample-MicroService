import os
from dotenv import load_dotenv
from pathlib import Path 
from app.utils import truthy

PROJECT_NAME = 'Sample Microservice'
SHORT_NAME = 'SM'

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / 'configs'


env = os.environ.get(f"{SHORT_NAME}_ENV")
if env is not None:
    dotenv_path = CONFIG_DIR / f'.env.{env.lower()}'
    if not dotenv_path.exists():
        dotenv_path = CONFIG_DIR / f'.env.local'
    load_dotenv(dotenv_path)
    print(f"{dotenv_path} loaded!")

FLASK_ENV = os.environ.get("FLASK_ENV") or os.getenv("FLASK_ENV")
if FLASK_ENV is None:
    raise EnvironmentError("Please set this enviroment key: FLASK_ENV")

SECRET_KEY = os.environ.get(f"{SHORT_NAME}_SECRET_KEY") or os.getenv(f"{SHORT_NAME}_SECRET_KEY")
if SECRET_KEY is None:
    raise EnvironmentError(f"Please set this enviroment key: {SHORT_NAME}_SECRET_KEY")


FLASK_DEBUG = os.environ.get("FLASK_DEBUG") or os.getenv("FLASK_DEBUG")
FLASK_DEBUG = FLASK_DEBUG in truthy

VERSION = os.environ.get(f"{SHORT_NAME}_VERSION") or os.getenv(f"{SHORT_NAME}_VERSION")

ENABLE_LOGGING = os.environ.get(f"{SHORT_NAME}_ENABLE_LOGGING") or os.getenv(f"{SHORT_NAME}_ENABLE_LOGGING")
ENABLE_LOGGING = ENABLE_LOGGING in truthy


