import unittest
from unittest import mock

import kivysome

requests_gag = mock.patch(
    "requests.Session.request",
    mock.Mock(side_effect=RuntimeError("requests are blocked for testing purposes")),
)


class CacheTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        kivysome.enable("5.13.1", force=True)

    def test_kivy_awesome_regular_blocked(self):
        with requests_gag:
            with self.assertRaises(RuntimeError):
                # DO NOT COPY THIS LINK!
                # Generate your own here: https://fontawesome.com/kits
                kivysome.enable("5.13.1", force=True)

    def test_kivy_awesome_cached_version(self):
        with requests_gag:
            kivysome.enable("5.13.1")

    def test_kivy_awesome_version_blocked(self):
        with requests_gag:
            with self.assertRaises(RuntimeError):
                kivysome.enable("5.13.1", force=True)
