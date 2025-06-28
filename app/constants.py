import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_PATH = os.path.join(BASE_DIR, "static")
INSTANCE_PATH = os.path.join(BASE_DIR, "instance")
DB_PATH = os.path.join(INSTANCE_PATH, "database.db")