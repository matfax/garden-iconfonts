# kivysome

[![CircleCI](https://circleci.com/gh/matfax/kivysome/tree/master.svg?style=shield)](https://circleci.com/gh/matfax/kivysome/tree/master)
[![codecov](https://codecov.io/gh/matfax/kivysome/branch/master/graph/badge.svg)](https://codecov.io/gh/matfax/kivysome)
[![Renovate Status](https://badges.renovateapi.com/github/matfax/kivysome)](https://renovatebot.com/)
[![CodeFactor](https://www.codefactor.io/repository/github/matfax/kivysome/badge)](https://www.codefactor.io/repository/github/matfax/kivysome)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kivysome)](https://pypi.org/project/kivysome/)
[![PyPI](https://img.shields.io/pypi/v/kivysome?color=%2339A7A6)](https://pypi.org/project/kivysome/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/kivysome?color=%231447F9)](https://pypistats.org/packages/kivysome)
[![GitHub License](https://img.shields.io/github/license/matfax/kivysome.svg)](https://github.com/matfax/kivysome/blob/master/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/matfax/kivysome?color=%232954A5)](https://github.com/matfax/kivysome/commits/master)

Font Awesome 5 Icons for Kivy

## Usage

### 1. Generate your kit

Go to [Font Awesome](https://fontawesome.com/kits) and generate your kit there.
The specified version is respected.
For the moment, only free licenses are supported. 

### 2. Enable it

In your main.py register your font:

```python
import kivysome 
kivysome.enable("https://kit.fontawesome.com/{YOURCODE}.js", group=kivysome.FontGroup.SOLID)
```

### 3. Use it

In your `.kv` file or string, reference the short Font Awesome (i.e., without `fa-` prefix) as you can copy them from their website.

```yaml
#: import icon kivysome.icon
Button:
    markup: True # Always turn markup on
    text: "%s"%(icon('comment'))
```

Check the `examples` folder for more insight.
