# kivysome

[![CodeFactor](https://www.codefactor.io/repository/github/matfax/kivysome/badge)](https://www.codefactor.io/repository/github/matfax/kivysome)

Font Awesome Icons for Kivy

## Usage

Once you have a .fontd file (see below) for your ttf iconfont generated you can use it like this:

In your main.py register your font:
```python
    iconfonts.register('default_font', 'iconfont_sample.ttf', 'iconfont_sample.fontd')
```

In your kv file or string:
```yaml
    #: import icon kivy.garden.iconfonts.icon
    Button:
        markup: True # Always turn markup on
        text: "%s"%(icon('icon-comment'))
```
See __init__.py for another example.

## Generating a fontd file

A .fontd file is just a python dictionary filled with icon_code: unicode_value entries. 
This information is extracted from a css file (all iconfonts packages I've seen have one).

