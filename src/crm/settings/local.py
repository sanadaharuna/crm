from .default import *
# import os

# BASE_DIR = os.path.dirname(os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__))))

DEBUG = True


# if os.environ.get("ON_DOCKER"):
#     STATIC_URL = "/crm/static/"
#     STATIC_ROOT = "/static"
# else:
#     STATIC_URL = "/static/"
#     STATIC_ROOT = os.path.join(BASE_DIR, "static")
#     ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/"


def show_toolbar(request):
    return True


INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}
