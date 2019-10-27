import unittest

import kivysome
from kivysome import iconfonts


class Tests(unittest.TestCase):

    def test_kivy_awesome_regular(self):
        # DO NOT COPY THIS LINK!
        # Generate your own here: https://fontawesome.com/kits
        kivysome.enable("https://kit.fontawesome.com/23372bf9a2.js", force=True)

    def test_kivy_awesome_wrong_url(self):
        with self.assertRaises(ValueError):
            kivysome.enable("https://google.com")

    def test_kivy_awesome_invalid_url(self):
        with self.assertRaises(ValueError):
            kivysome.enable("invalid")

    def test_create_fontdict_file(self):
        res = iconfonts.create_fontdict_file("tests/iconfont_sample.css",
                                             'tests/iconfont_sample.fontd')
        self.assertEqual(res, {'icon-plus-circled': 59395, 'icon-spin6': 59393,
                               'icon-doc-text-inv': 59396,
                               'icon-emo-happy': 59392,
                               'icon-comment': 59397, 'icon-users': 59394})

    def test_register(self):
        iconfonts.register('name', 'tests/iconfont_sample.ttf',
                           'tests/iconfont_sample.fontd')
        self.assertEqual(iconfonts._register['name'][0], 'tests/iconfont_sample.ttf')

    def test_icon(self):
        iconfonts.register('name', 'tests/iconfont_sample.ttf',
                           'tests/iconfont_sample.fontd')
        r = iconfonts.icon('icon-comment')
        self.assertEqual(
            "[font=tests/iconfont_sample.ttf]%s[/font]" % chr(59397), r)
        r = iconfonts.icon('icon-comment', 20)
        self.assertEqual(
            "[size=20][font=tests/iconfont_sample.ttf]%s[/font][/size]" %
            chr(59397), r)
