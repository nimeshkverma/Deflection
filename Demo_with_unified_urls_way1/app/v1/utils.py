import os
import sys

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path

from mapping import API_MAPPINGS
from common_utils import api_response


def get_response(api_request):
    return api_response(api_request, API_MAPPINGS)
