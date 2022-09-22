import scrapy

class MadhyaPradeshSDLC(scrapy.Spider):
    name = "madhyapradeshSDLC"
    
    def start_requests(self):
        urls = [
            'https://www.sldcmpindia.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    
    def parse(self, response):
        object = {}
        realTimeData = [
            '//*[@id="freq_val"]/text()',
            '//*[@id="uirate_val"]/text()',
            '//*[@id="demand_val"]/text()',
        ]

        realTimeDataCategories = [
            'WR Grid Frequency', 
            'Dev Rate', 
            'Catered Demand',
        ]

        for i in range(len(realTimeData)):
            data = response.xpath(realTimeData[i]).extract()
            if data:
                object[realTimeDataCategories[i]] = data
        yield object
