from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.animation import Animation
from os.path import join, dirname

import kivysome
from kivysome import FontGroup

if __name__ == '__main__':

    kv = """
#: import icon kivysome.icon
BoxLayout:
    Button:
        markup: True
        text: "%s"%(icon('comment', 32))
    Button:
        markup: True
        text: "%s"%(icon('clipboard-check', 64))

    Button:
        markup: True
        text: "%s Text"%(icon('laugh-wink', 24))

    Button:
        markup: True
        text: "%s"%(icon('file-word', 64, 'ff3333'))

    Label:
        id: _anim
        markup: True
        text: "%s"%(icon('circle-notch', 32))
        font_color: 1, 0, 0, 1
        p: 0
        canvas:
            Clear
            PushMatrix
            Rotate:
                angle: -self.p
                origin: self.center_x , self.center_y
            Rectangle:
                size: (32, 32)
                pos: self.center_x - 16, self.center_y - 16
                texture: self.texture
            PopMatrix
    """

    # DO NOT COPY THIS LINK!
    # Generate your own here: https://fontawesome.com/kits
    kivysome.enable("https://kit.fontawesome.com/045c3333e7.js", group=FontGroup.SOLID, font_folder="../fonts")

    root = Builder.load_string(kv)
    an = Animation(p=360, duration=2) + Animation(p=0, duration=0)
    an.repeat = True
    an.start(root.ids['_anim'])
    runTouchApp(root)
