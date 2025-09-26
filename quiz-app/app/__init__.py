from flask import Flask
import os

# optional: absolute paths to avoid template/static issues
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "app", "templates")
)

# import routes at the end to avoid circular imports
from app import routes