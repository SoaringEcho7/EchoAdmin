from robyn import Robyn
from pathlib import Path

app = Robyn(__file__)

# Configure template directory
TEMPLATE_DIR = Path(__file__).parent / "templates"
STATIC_DIR = Path(__file__).parent / "static"

# Load routes
from app.controllers import *  # noqa
