import scrapy

# When running this code using the Anaconda Console or in your command line
# run 'scrapy crawl manipurSLDC3' since the name of the spider is as such down below.
class ManipurSLDC3(scrapy.Spider):
    name = 'manipurSLDC3'
    def start_requests(self): 
        urls = [
            'https://sldcmanipur.com/', # List of URLs being scraped
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Main function for scraping the website for data.
    def parse(self, response):
            # Obtained from copying the Xpath for each name under "Sub-station name(Transformer)" column using 
            # the developer tools in browser and hovering over the element.
            # Note: Removed '/tbody' from every xPath copied to extract data from website.
            #       Added '/text()' inside the quotations after the copied Xpath
            #       to specify that the text of that Xpath is desired.
            #       Also, for '/tr[i]', where i is the number copied along with the Xpath,
            #       must reduce change to '/tr[i-1]' so that no row is missing. 
            T_labels = [
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[1]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[2]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[3]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[4]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[5]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[6]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[7]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[8]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[9]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[10]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[11]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[12]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[13]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[14]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[15]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[16]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[17]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[18]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[19]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[20]/td[1]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[21]/td[1]/text()',

            ]
            # Obtained from copying the Xpath for each name under "Transformer Load" column using 
            # the developer tools in browser and hovering over the element.
            # Note: Removed '/tbody' from every xPath copied to extract data from website.
            #       Added '/text()' inside the quotations after the copied Xpath
            #       to specify that the text of that Xpath is desired.
            #       Also, for '/tr[i]', where i is the number copied along with the Xpath,
            #       must reduce change to '/tr[i-1]' so that no row is missing. 
            T_loads = [
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[1]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[2]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[3]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[4]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[5]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[6]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[7]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[8]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[9]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[10]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[11]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[12]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[13]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[14]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[15]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[16]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[17]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[18]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[19]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[20]/td[2]/text()',
                '//*[@id="form1"]/div[3]/div[1]/div[1]/div[4]/table/tr[21]/td[2]/text()',
                
            ]
            # Empty Object which will be filled with data from website.
            object = {}
            # For all Xpaths listed in T_labels, extract the line names and their load from the website
            # and if both the name and load exist, add the name under "Transformer Names" and the load in "Transformer Loads".
            # Then finally, yield the object every iteration.
            for i in range(len(T_labels)):
                transformer = response.xpath(T_labels[i]).get() # Use '.get()' to extract just the text
                load = response.xpath(T_loads[i]).get()
                object["Transformer Names"] = transformer
                object["Transformer Loads"] = load
                yield object
