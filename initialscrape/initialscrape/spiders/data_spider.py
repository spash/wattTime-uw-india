import scrapy
from scrapy import Selector

#When you run this code in your anaconda console or command line
# you run 'scrapy crawl quotes' where quotes is the name assigned below 
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://sldccg.com/trans.php',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        # requests scrapy url
    
    def parse(self, response):
        tables = [0,0]
        tables[0] = response.xpath('//*[@id="testdiv"]/table/tbody/tr[2]/td[1]/table').extract()
        # second table xpath
        tables[1] = response.xpath('//*[@id="testdiv"]/table/tbody/tr[2]/td[2]/table').extract()
        for tbl in tables:
            yield {
                'Transformer Name': response.xpath('//*[@id="testdiv"]/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td[1]/span/text()').extract(),
                'Load': response.xpath('//*[@id="testdiv"]/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td[2]/span/strong/text()').extract(),
                'Test': 'hi'
            }
