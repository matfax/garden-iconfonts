# kivysome

[![codecov](https://codecov.io/gh/matfax/kivysome/branch/master/graph/badge.svg)](https://codecov.io/gh/matfax/kivysome)
[![CodeFactor](https://www.codefactor.io/repository/github/matfax/kivysome/badge)](https://www.codefactor.io/repository/github/matfax/kivysome)

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
