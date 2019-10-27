import json
import re
from mutapath import Path

_register = dict()


def register(name, ttf_fname, fontd_fname):
    """Register an Iconfont
    :param name: font name identifier.
    :param ttf_fname: ttf filename (path)
    :param fontd_fname: fontdic filename. (See create_fontdic)
    """
    font_file = Path(fontd_fname)
    fontd = json.loads(font_file.text)
    _register[name] = ttf_fname, fontd_fname, fontd


def icon(code, size=None, color=None, font_name=None):
    """ Gets an icon from iconfont.
    :param code: Icon codename (ex: 'icon-name')
    :param size: Icon size
    :param color: Icon color
    :param font_name: Registered font name. If None first one is used.
    :returns: icon text (with markups)
    """
    font = next(iter(_register.keys())) if font_name is None else font_name
    font_data = _register[font]
    s = "[font=%s]%s[/font]" % (font_data[0], chr(font_data[2][code]))
    if size is not None:
        s = "[size=%s]%s[/size]" % (size, s)
    if color is not None:
        s = "[color=%s]%s[/color]" % (color, s)

    return s


def create_fontdict_file(css_fname, output_fname=""):
    """Creates a font dictionary file. Basically creates a dictionary filled
    with icon_code: unicode_value entries
    obtained from a CSS file.
    :param css_fname: CSS filename where font's rules are declared.
    :param output_fname: Fontd file destination
    """
    css_file = Path(css_fname)
    if output_fname:
        output_file = Path(output_fname)
    else:
        output_file = css_file.with_suffix(".fontd")

    res = _parse(css_file.read_text("utf-8"))
    output_file.write_text(json.dumps(res))

    return res


def _parse(data):
    # find start index where icons rules start
    pat_start = re.compile('}.+content:', re.DOTALL)
    rules_start = [x for x in re.finditer(pat_start, data)][0].start()
    data = data[rules_start:]  # crop data
    data = data.replace("\\", '0x')  # replace unicodes
    data = data.replace("'", '"')  # replace quotes
    # iterate rule indices and extract value
    pat_keys = re.compile('[a-zA-Z0-9_-]+:before')
    res = dict()
    for i in re.finditer(pat_keys, data):
        start = i.start()
        end = data.find('}', start)
        key = i.group().replace(':before', '')
        try:
            value = int(data[start:end].split('"')[1], 0)
        except (IndexError, ValueError):
            continue
        if key.startswith("fa-"):
            _, key = key.split("-", 1)
        res[key] = value
    return res
