# How we scrape Indian emission grid data for WattTime

This repo contains the code for our scrapers and the documentation for our data sources. Data sources are found in datasources.md

## Setup

### MacOS, from terminal

(Tested with Python 3.9.13 via virtual environment) 
- Navigate to tutorial folder containing _init.py_
- Create virtual environment
    activate it
    (_optional_) install scrapy with pip:
```
python3 -m venv env
source env/bin/activate
pip install scrapy
```

- (_Optional_) Create initial project directory (do first time)
```
scrapy startproject tutorial
```

This creates the default structure:

```
tutorial/
    scrapy.cfg            # configuration file


    tutorial/             # Import your code from this second 'tutorial' directory
        __init__.py

        items.py          # project items

        middlewares.py    # project middlewares

        pipelines.py      # project pipelines

        settings.py       # project settings

        spiders/          # project spiders
            __init__.py
```

### Scrapy Shell

- Enter Scrapy shell: `scrapy shell '[url]'`
- View Scrapy commands: `scrapy -h`
- View help for particular command: `scrapy <command> [options] [args]`
- View web response in shell: `view(response)`
- Quit Scrapy shell: `quit`


### Output
By default, your local outputs (json and html pages) are in "local-output" directory (and are .gitignore'd)

- Save html pages to /local_output: `scrapy crawl [spidername]` 
    (_Note: use the spider name variable within the class, not the spider class name itself_)
- Save output as json file: `local scrapy crawl [spidername] -o ./local_output/[spidername].json`

The database schema is defined in `/tutorial/models.py`. It's connection string is found in `/tutorial/settings.py`, which is where you may create **pipelines**, numbered 0-1000, which represents the order of their execution. Ex:
```
ITEM_PIPELINES = {
    'tutorial.pipelines.SaveSpider1Pipeline': 100,
}
```





## Troubleshooting: Frequent issues

Diagnose with `shelp()` via the Scrapy shell



## Optional

### Colorized Logging
Add the `colorlog` package to your `settings.py` file:
```import copy
from colorlog import ColoredFormatter
import scrapy.utils.log

color_formatter = ColoredFormatter(
    (
        '%(log_color)s%(levelname)-5s%(reset)s '
        '%(yellow)s[%(asctime)s]%(reset)s'
        '%(white)s %(name)s %(funcName)s %(bold_purple)s:%(lineno)d%(reset)s '
        '%(log_color)s%(message)s%(reset)s'
    ),
    datefmt='%y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'blue',
        'INFO': 'bold_cyan',
        'WARNING': 'red',
        'ERROR': 'bg_bold_red',
        'CRITICAL': 'red,bg_white',
    }
)

_get_handler = copy.copy(scrapy.utils.log._get_handler)

def _get_handler_custom(*args, **kwargs):
    handler = _get_handler(*args, **kwargs)
    handler.setFormatter(color_formatter)
    return handler
scrapy.utils.log._get_handler = _get_handler_custom
```
