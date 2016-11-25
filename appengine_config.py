"""App Engine Python Environment Configuration File.

`appengine_config.py` is automatically loaded when Google App Engine
starts a new instance of your application. This runs before any
WSGI applications specified in app.yaml are loaded.
"""
from google.appengine.api import modules
# from google.appengine.ext import vendor

# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
# vendor.add('lib')


def namespace_manager_default_namespace_for_request():
    """Set the namespace to current version before every request."""
    return modules.get_current_version_name().lower()
