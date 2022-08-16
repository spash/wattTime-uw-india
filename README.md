# How we approach scraping Indian emission grid data for WattTime

This repo contains the code for our scrapers and the documentation for our data sources. Data sources are found in datasources.md

## Setup

### MacOS, from terminal

(Tested with Python 3.9.13 via virtual environment) 
- *Navigate to tutorial folder containing _init.py_*
- *create virtual environment, activate it, and (_optional_) install scrapy with pip.* Enter:
```
python3 -m venv env
source env/bin/activate
pip install scrapy
```

(_Optional_) *Create initial project directory (do first time)*
From chosen directory:
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

Find your local outputs (json and html pages) in "local-output" directory by default (which are .gitignore'd)

*Save html pages to /local_output with* `scrapy crawl [spidername]` 
*(_note: use the spider name variable within the class, not the spider class name itself_)
*Save output as json file with* `local scrapy crawl [spidername] -o ./local_output/[spidername].json`

### Scrapy Shell

*Enter Scrapy Shell*
```
scrapy shell '[url]'
```

Quit the Scrapy CLI with command `quit`


## Troubleshooting: Frequent issues

Type `shelp()` in the Scrapy shell
