"""Package for tests."""
import os
import subprocess
import sys

sys.path.insert(1, os.path.abspath(os.curdir))
sys.path.insert(1, os.path.join(os.path.abspath(os.curdir), 'lib_tests'))

try:
    gae_sdk_path = subprocess.check_output(['which', 'dev_appserver.py'])
except subprocess.CalledProcessError:
    # continuous integration workaround
    gae_sdk_path = '/opt/citools/google-cloud-sdk/'


gae_sdk_path = os.path.dirname(gae_sdk_path).replace('/bin', '')
gae_sdk_path = os.path.join(gae_sdk_path, 'platform', 'google_appengine')
sys.path.append(gae_sdk_path)
sys.path.append(os.path.join(gae_sdk_path, 'lib', 'yaml', 'lib'))
sys.path.append('/apps/gcp/google-cloud-sdk/platform/google_appengine/lib/endpoints-1.0') # noqa

for lib in 'endpoints-1.0 protorpc-1.0 webapp2-2.5.2 webob-1.2.3'.split():
    sys.path.append(os.path.join(gae_sdk_path, 'lib', lib))

print sys.path
