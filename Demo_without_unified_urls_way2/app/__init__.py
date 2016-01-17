import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from config import VERSIONS_ALLOWED
from app_config import register_versions, app

register_versions(VERSIONS_ALLOWED)
