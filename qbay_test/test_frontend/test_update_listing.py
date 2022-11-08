from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import *


class FrontEndHomePageTest(BaseCase):

    def test_update_listing_success(self, *_):

        # login first
        self.open(base_url + "/login")
        self.type("#email", "111@111.com")
        self.type("#password", "123!Abc")
        self.click("#btn-submit")

        # edit properities
        self.click("#edit-pro")
