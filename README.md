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
python3 -m pip install scrapy
python3 -m pip install twisted
```
### Windows, from Anaconda Command Prompt
- The easiest way to install scrapy is through anaconda, so ensure you have anaconda installed first
- Create virtual environment and activate it

```
create --name virtualenv_scrapy
conda activate virtualenv_scrapy
conda install -c conda-forge scrapy
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

### Scrapy Shell - MacOS

- Enter Scrapy shell: 
    -   `pip install scrapy-user-agents`
    -   `scrapy shell '[url]'`
- View Scrapy commands: `scrapy -h`
- View help for particular command: `scrapy <command> [options] [args]`
- View web response in shell: `view(response)`
- Quit Scrapy shell: `quit`

### Conda Prompt - Windows

- Navigate to folder where your project is in the conda prompt
```
cd ../wattTime/initialscrape
```
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
[^FeedURI]: Feed URI examples shown at the bottom of https://doc.scrapy.org/en/latest/topics/feed-exports.html with an example of pipelines also here https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
- Diagnose with `shelp()` via the Scrapy shell
- Scraping items to csv or JSON helpful link: https://www.geeksforgeeks.org/saving-scraped-items-to-json-and-csv-file-using-scrapy/
- User Agents errors are common for example an error like this can be seen in the command prompt
```
DEBUG: Assigned User-Agent Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36
2022-09-15 12:40:04 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://sldccg.com/robots.txt> (referer: None)
2022-09-15 12:40:04 [protego] DEBUG: Rule at line 1 without any user agent to enforce it on.
2022-09-15 12:40:04 [protego] DEBUG: Rule at line 2 without any user agent to enforce it on.
2022-09-15 12:40:04 [protego] DEBUG: Rule at line 7 without any user agent to enforce it on.
2022-09-15 12:40:04 [protego] DEBUG: Rule at line 8 without any user agent to enforce it on.
2022-09-15 12:40:04 [protego] DEBUG: Rule at line 9 without any user agent to enforce it on.
2022-09-15 12:40:04 [protego] DEBUG: Rule at line 10 without any user agent to enforce it on.
2022-09-15 12:40:04 [protego] DEBUG: Rule at line 11 without any user agent to enforce it on.
2022-09-15 12:40:04 [scrapy_user_agents.middlewares] DEBUG: Assigned User-Agent Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36
```
- By adjusting USER_AGENT = 'insert your user agent' in the settings.py you can mitigate this issue. See this link for further explanation: https://stackoverflow.com/questions/69313884/debug-rule-at-line-3-without-any-user-agent-to-enforce-it-on-python-scrapy
