import unittest

import kivysome
import socket


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        kivysome.enable("5.13.1", force=True)

        def guard(*args, **kwargs):
            raise ValueError("Socket is blocked for testing purposes!")
        socket.socket = guard

    def test_kivy_awesome_regular_blocked(self):
        with self.assertRaises(ValueError):
            # DO NOT COPY THIS LINK!
            # Generate your own here: https://fontawesome.com/kits
            kivysome.enable("https://kit.fontawesome.com/23372bf9a2.js", force=True)

    def test_kivy_awesome_cached_version(self):
        kivysome.enable("5.13.1")

    def test_kivy_awesome_version_blocked(self):
        with self.assertRaises(ValueError):
            kivysome.enable("5.13.1", force=True)
