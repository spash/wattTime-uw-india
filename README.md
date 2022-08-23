# How we use Scrapy

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
- Save output as json file from scrapy shell: `scrapy crawl [spider name] -o [file name].json`
- Save output as csv file from scrapy shell: `scrapy crawl [spider name] -o [file name].csv`

The database schema is defined in `/tutorial/models.py`. It's connection string is found in `/tutorial/settings.py`, which is where you may create **pipelines**, numbered 0-1000, which represents the order of their execution. Ex:
```
ITEM_PIPELINES = {
    'tutorial.pipelines.SaveSpider1Pipeline': 100,
}
```

**Note**: `/tutorial/settings.py` is global. To affect the output of one specific spider, overwrite the Feed URI `custom_settings` variable [^FeedURI] in your spider class, using the desired `.json` or `.csv` file name:
```
custom_settings = {
        # don't forget to update your settings.py file (refer to footnote above)
       'FEED_URI' : 'folder/filename.csv'
   }
```




## Troubleshooting: Frequent issues

Diagnose with `shelp()` via the Scrapy shell

[^FeedURI]: Feed URI examples shown at the bottom of https://doc.scrapy.org/en/latest/topics/feed-exports.html with an example of pipelines also here https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
