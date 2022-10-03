import scrapy

# When running this code using the Anaconda Console or in your command line
# run 'scrapy crawl manipurSLDC' since the name of the spider is as such down below.
class ManipurSLDC(scrapy.Spider):
    name = "manipurSLDC"
    
    def start_requests(self):
        urls = [
            'https://sldcmanipur.com/', # List of URLs being scraped
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    # Main function for scraping the website for data.
    def parse(self, response):
        # Empty Object which will be filled with data from website.
        object = {}

        # Obtained from copying the XPath of the data needed from website using the developer
        # tools in browser and hovering over the element.
        # Note: Added '/text()' inside the quotations after the copied Xpath
        #       to specify that the text of that Xpath is desired. 
        realTimeData = [
            '//*[@id="UpdatePanel1"]/div[2]/div[1]/div/div[1]/h3/text()',
            '//*[@id="UpdatePanel1"]/div[2]/div[2]/div/div[1]/h3/text()',
            '//*[@id="UpdatePanel1"]/div[2]/div[3]/div/div[1]/h3/text()',
            '//*[@id="UpdatePanel1"]/div[2]/div[4]/div/div[1]/h3/text()',
        ]

        # Category names of the data obtained from the website.
        realTimeDataCategories = [
            'Schedule',
            'Drawal',
            'Deviation',
            'Frequency',
        ]


        # For all Xpaths listed in realTimeData, extract data from the website
        # and if the data exists, add the data under the category it belongs to.
        # Then finally, yield the object with all the data scraped. 
        for i in range(len(realTimeData)):
            data = response.xpath(realTimeData[i]).get()
            if data:
                object[realTimeDataCategories[i]] = data
        yield object

    
