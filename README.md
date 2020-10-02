# kivysome

[![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/matfax/kivysome/build/master?style=for-the-badge)](https://github.com/matfax/kivysome/actions)
[![Codecov](https://img.shields.io/codecov/c/github/matfax/kivysome?style=for-the-badge)](https://codecov.io/gh/matfax/kivysome)
[![Dependabot Status](https://img.shields.io/badge/dependabot-enabled-blue?style=for-the-badge&logo=dependabot&color=0366d6)](https://github.com/matfax/kivysome/network/updates)
[![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/kivysome?style=for-the-badge)](https://libraries.io/pypi/kivysome)
[![CodeFactor](https://www.codefactor.io/repository/github/matfax/kivysome/badge?style=for-the-badge)](https://www.codefactor.io/repository/github/matfax/kivysome)
[![security: bandit](https://img.shields.io/badge/security-bandit-purple.svg?style=for-the-badge)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kivysome?style=for-the-badge)](https://pypi.org/project/kivysome/)
[![PyPI](https://img.shields.io/pypi/v/kivysome?color=%2339A7A6&style=for-the-badge)](https://pypi.org/project/kivysome/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/kivysome?color=ff69b4&style=for-the-badge)](https://pypistats.org/packages/kivysome)
[![GitHub License](https://img.shields.io/github/license/matfax/kivysome.svg?style=for-the-badge)](https://github.com/matfax/kivysome/blob/master/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/matfax/kivysome?color=9cf&style=for-the-badge)](https://github.com/matfax/kivysome/commits/master)

Font Awesome 5 Icons for Kivy

## Usage

### Enable it

#### Using a version

This will only work for free versions of Font Awesome.

```python
import kivysome 
kivysome.enable(kivysome.LATEST, group=kivysome.FontGroup.REGULAR)
```

#### Using a kit

Kits will not be maintained any further.
They will work as long as Font Awesome don't change their API.

##### 1. Generate your kit

Go to [Font Awesome](https://fontawesome.com/kits) and generate your kit there.
The specified version is respected.
For the moment, only free licenses are supported. 

##### 2. Enable it

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
    text: "%s Comment" % icon('comment', 24)
```

## Caching

Kivysome will cache the files in the font folder and not redownload them from GitHub.
If a kit is given, however, the kit version will have to be fetched from Font Awesome on every execution.
If `kivysome.LATEST` is given, the latest version will also have to be determined from GitHub's servers.
Font packs will only be downloaded if new versions are published, then.
To completely avoid regular server access, a pinned version will have to be given.
The initial download can also be circumvented by downloading it a single time on the developer's machine and publishing
the downloaded `fonts` folder with the project. The folder should then contain a `.css`, `.fontd`, and a `.ttf` file
matching the pinned Font Awesome version and font group.

Check the `examples` folder for more insight.
