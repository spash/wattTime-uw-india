import scrapy

# When you run this code in your anaconda console or command line
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
        t_labels = ['//*[@id="Label7"]/text()', '//*[@id="Label14"]/text()',
        '//*[@id="Label15"]/text()', '//*[@id="Label16"]/text()',
        '//*[@id="Label40"/text()','//*[@id="Label41"/text()',
        '//*[@id="Label19"/text()', '//*[@id="Label42"/text()',
        '//*[@id="Label22"/text()', '//*[@id="Label23"/text()']
        l_labels = ['//*[@id="L1"]/strong/text()', '//*[@id="L2"]/strong/text()',
         '//*[@id="L3"]/strong/text()', '//*[@id="L4"]/strong/text()', 
         '//*[@id="L5"]/strong/text()', '//*[@id="L6"]/strong/text()', 
         '//*[@id="L7"]/strong/text()', '//*[@id="L8"]/strong/text()', 
         '//*[@id="L9"]/strong/text()', '//*[@id="L10"]/strong/text()']
        i = 0
        object = {}
        for i in range(len(t_labels)):
            transformer = response.xpath(t_labels[i]).extract()
            object[str(transformer)] = response.xpath(l_labels[i]).extract()
           
        yield object