import os
import pytest
import site
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
# from django.contrib.auth.models import User
# from search.models import *
# from search.tests import factories as search_facs

site.addsitedir(os.path.dirname(__file__))

pytestmark = pytest.mark.django_db
