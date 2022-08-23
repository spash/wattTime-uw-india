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

        t_labels = ['//*[@id="Label7"]/text()', '//*[@id="Label14"]/text()',
        '//*[@id="Label15"]/text()', '//*[@id="Label16"]/text()',
        '//*[@id="Label40"]/text()','//*[@id="Label41"]/text()',
        '//*[@id="Label19"]/text()', '//*[@id="Label42"]/text()',
        '//*[@id="Label22"]/text()', '//*[@id="Label23"]/text()', 
        '//*[@id="Label317"]/text()', '//*[@id="Label316"]/text()',
        '//*[@id="Label24"]/text()', '//*[@id="Label320"]/text()',
        '//*[@id="Label321"]/text()', '//*[@id="Label322"]/text()',
        '//*[@id="Label323"]/text()', '//*[@id="Label324"]/text()',
        '//*[@id="Label25"]/text()', '//*[@id="Label26"]/text()',
        '//*[@id="Label326"]/text()', '//*[@id="Label327"]/text()']
        t_loads = ['//*[@id="L1"]/strong/text()', '//*[@id="L2"]/strong/text()',
         '//*[@id="L3"]/strong/text()', '//*[@id="L4"]/strong/text()', 
         '//*[@id="L5"]/strong/text()', '//*[@id="L6"]/strong/text()', 
         '//*[@id="L7"]/strong/text()', '//*[@id="L8"]/strong/text()', 
         '//*[@id="L9"]/strong/text()', '//*[@id="L10"]/strong/text()',
         '//*[@id="L11"]/strong/text()', '//*[@id="L12"]/strong/text()',
         '//*[@id="L13"]/strong/text()', '//*[@id="L14"]/strong/text()',
         '//*[@id="L15"]/strong/text()', '//*[@id="L16"]/strong/text()',
         '//*[@id="L17"]/strong/text()', '//*[@id="L18"]/strong/text()',
         '//*[@id="L19"]/strong/text()', '//*[@id="L20"]/strong/text()',
         '//*[@id="L47"]/strong/text()', '//*[@id="L48"]/strong/text()']
        # i = 0
        object = {}
        # length of labels is 10 rn
        for i in range(len(t_labels)):
            transformer = response.xpath(t_labels[i]).extract()
            load = response.xpath(t_loads[i]).extract()
            if transformer and load :
                object['Transformer: '  + str(transformer)[2:-2]] = int(str(load)[2:-2])
        
        L_labels = ['//*[@id="Label8"]/text()', '//*[@id="Label27"]/text()',
        '//*[@id="Label28"]/text()', '//*[@id="Label44"]/text()',
        '//*[@id="Label31"]/text()','//*[@id="Label45"]/text()',
        '//*[@id="Label33"]/text()', '//*[@id="Label34"]/text()',
        '//*[@id="Label35"]/text()', '//*[@id="Label38"]/text()', 
        '//*[@id="Label47"]/text()', '//*[@id="Label304"]/text()',
        '//*[@id="Label305"]/text()', '//*[@id="Label306"]/text()',
        '//*[@id="Label307"]/text()', '//*[@id="Label308"]/text()',
        '//*[@id="Label309"]/text()', '//*[@id="Label310"]/text()',
        '//*[@id="Label311"]/text()', '//*[@id="Label312"]/text()',
        '//*[@id="Label313"]/text()', '//*[@id="Label314"]/text()',
        '//*[@id="Label315"]/text()', '//*[@id="Label36"]/text()',
        '//*[@id="Label46"]/text()', '//*[@id="Label325"]/text()']
        L_loads = ['//*[@id="L21"]/strong/text()', '//*[@id="L22"]/strong/text()',
         '//*[@id="L23"]/strong/text()', '//*[@id="L24"]/strong/text()', 
         '//*[@id="L25"]/strong/text()', '//*[@id="L26"]/strong/text()', 
         '//*[@id="L27"]/strong/text()', '//*[@id="L28"]/strong/text()', 
         '//*[@id="L29"]/strong/text()', '//*[@id="L30"]/strong/text()',
         '//*[@id="L31"]/strong/text()', '//*[@id="L32"]/strong/text()',
         '//*[@id="L33"]/strong/text()', '//*[@id="L34"]/strong/text()',
         '//*[@id="L35"]/strong/text()', '//*[@id="L36"]/strong/text()',
         '//*[@id="L37"]/strong/text()', '//*[@id="L38"]/strong/text()',
         '//*[@id="L39"]/strong/text()', '//*[@id="L40"]/strong/text()',
         '//*[@id="L41"]/strong/text()', '//*[@id="L42"]/strong/text()',
         '//*[@id="L43"]/strong/text()', '//*[@id="L44"]/strong/text()',
         '//*[@id="L45"]/strong/text()', '//*[@id="L46"]/strong/text()']
        for i in range(len(L_labels)):
            line = response.xpath(L_labels[i]).extract()
            load = response.xpath(L_loads[i]).extract()
            if transformer and load :
                object['Line: '  + str(line)[2:-2]] = int(str(load)[2:-2])        
        yield object