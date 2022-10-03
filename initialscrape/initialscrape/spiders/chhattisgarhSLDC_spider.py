import scrapy
import sys
from scrapy.crawler import CrawlerRunner
from ..items import LineItem, TransformerItem
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

# When you run this code in your anaconda console or command line
# you run 'scrapy crawl chhattisgarhSLDC' where chhattisgarhSLDC is the name assigned below


class chhattisgarhSLDC1(scrapy.Spider):
    name = "chhattisgarhSLDC"

    def start_requests(self):
        urls = ["https://sldccg.com/trans.php", "https://sldccg.com/gen.php"]

        # yield scrapy.Request(url=urls[0], callback=cbs[0])
        yield scrapy.Request(url=urls[0], callback=self.parse1)

    def parse1(self, response):
        # In developer tools hover over the element and copy Xpath
        # T labels is for transformers

        t_labels = [
            '//*[@id="Label7"]/text()',
            '//*[@id="Label14"]/text()',
            '//*[@id="Label15"]/text()',
            '//*[@id="Label16"]/text()',
            '//*[@id="Label40"]/text()',
            '//*[@id="Label41"]/text()',
            '//*[@id="Label19"]/text()',
            '//*[@id="Label42"]/text()',
            '//*[@id="Label22"]/text()',
            '//*[@id="Label23"]/text()',
            '//*[@id="Label317"]/text()',
            '//*[@id="Label316"]/text()',
            '//*[@id="Label24"]/text()',
            '//*[@id="Label320"]/text()',
            '//*[@id="Label321"]/text()',
            '//*[@id="Label322"]/text()',
            '//*[@id="Label323"]/text()',
            '//*[@id="Label324"]/text()',
            '//*[@id="Label25"]/text()',
            '//*[@id="Label26"]/text()',
            '//*[@id="Label326"]/text()',
            '//*[@id="Label327"]/text()',
        ]
        t_loads = [
            '//*[@id="L1"]/strong/text()',
            '//*[@id="L2"]/strong/text()',
            '//*[@id="L3"]/strong/text()',
            '//*[@id="L4"]/strong/text()',
            '//*[@id="L5"]/strong/text()',
            '//*[@id="L6"]/strong/text()',
            '//*[@id="L7"]/strong/text()',
            '//*[@id="L8"]/strong/text()',
            '//*[@id="L9"]/strong/text()',
            '//*[@id="L10"]/strong/text()',
            '//*[@id="L11"]/strong/text()',
            '//*[@id="L12"]/strong/text()',
            '//*[@id="L13"]/strong/text()',
            '//*[@id="L14"]/strong/text()',
            '//*[@id="L15"]/strong/text()',
            '//*[@id="L16"]/strong/text()',
            '//*[@id="L17"]/strong/text()',
            '//*[@id="L18"]/strong/text()',
            '//*[@id="L19"]/strong/text()',
            '//*[@id="L20"]/strong/text()',
            '//*[@id="L47"]/strong/text()',
            '//*[@id="L48"]/strong/text()',
        ]

        items = []
        t_item = TransformerItem()
        for i in range(len(t_labels)):
            transformer = response.xpath(t_labels[i]).extract()  # Bhilai ICT
            load = response.xpath(t_loads[i]).extract()  # get actual number
            if transformer and load:
                t_item["Transformer_name"] = str(transformer)[2:-2]
                t_item["Transformer_load"] = int(str(load)[2:-2])
            yield t_item


class chhattisgarhSLDC2(scrapy.Spider):
    def start_requests(self):

        yield scrapy.Request(url="https://sldccg.com/trans.php", callback=self.parse2)
        # Currently the last url is facing issues with user agent thus this last request is commented out
        # else: yield scrapy.Request(url=urls[i], callback=cbs[i])
        # L labels is for lines

    def parse2(self, response):
        L_labels = [
            '//*[@id="Label8"]/text()',
            '//*[@id="Label27"]/text()',
            '//*[@id="Label28"]/text()',
            '//*[@id="Label44"]/text()',
            '//*[@id="Label31"]/text()',
            '//*[@id="Label45"]/text()',
            '//*[@id="Label33"]/text()',
            '//*[@id="Label34"]/text()',
            '//*[@id="Label35"]/text()',
            '//*[@id="Label38"]/text()',
            '//*[@id="Label47"]/text()',
            '//*[@id="Label304"]/text()',
            '//*[@id="Label305"]/text()',
            '//*[@id="Label306"]/text()',
            '//*[@id="Label307"]/text()',
            '//*[@id="Label308"]/text()',
            '//*[@id="Label309"]/text()',
            '//*[@id="Label310"]/text()',
            '//*[@id="Label311"]/text()',
            '//*[@id="Label312"]/text()',
            '//*[@id="Label313"]/text()',
            '//*[@id="Label314"]/text()',
            '//*[@id="Label315"]/text()',
            '//*[@id="Label36"]/text()',
            '//*[@id="Label46"]/text()',
            '//*[@id="Label325"]/text()',
        ]
        L_loads = [
            '//*[@id="L21"]/strong/text()',
            '//*[@id="L22"]/strong/text()',
            '//*[@id="L23"]/strong/text()',
            '//*[@id="L24"]/strong/text()',
            '//*[@id="L25"]/strong/text()',
            '//*[@id="L26"]/strong/text()',
            '//*[@id="L27"]/strong/text()',
            '//*[@id="L28"]/strong/text()',
            '//*[@id="L29"]/strong/text()',
            '//*[@id="L30"]/strong/text()',
            '//*[@id="L31"]/strong/text()',
            '//*[@id="L32"]/strong/text()',
            '//*[@id="L33"]/strong/text()',
            '//*[@id="L34"]/strong/text()',
            '//*[@id="L35"]/strong/text()',
            '//*[@id="L36"]/strong/text()',
            '//*[@id="L37"]/strong/text()',
            '//*[@id="L38"]/strong/text()',
            '//*[@id="L39"]/strong/text()',
            '//*[@id="L40"]/strong/text()',
            '//*[@id="L41"]/strong/text()',
            '//*[@id="L42"]/strong/text()',
            '//*[@id="L43"]/strong/text()',
            '//*[@id="L44"]/strong/text()',
            '//*[@id="L45"]/strong/text()',
            '//*[@id="L46"]/strong/text()',
        ]
        l_item = LineItem()
        for i in range(len(L_labels)):
            line = response.xpath(L_labels[i]).extract()
            load = response.xpath(L_loads[i]).extract()
            if line and load:
                l_item["Line_name"] = str(line)[2:-2]
                l_item["Line_load"] = int(str(load)[2:-2])
            yield l_item


class chhattisgarhSLDC3(scrapy.Spider):
    def start_requests(self):

        yield scrapy.Request(url="https://sldccg.com/gen.php", callback=self.parse3)
        # Currently this url is facing issues with user agent thus this last request is commented out
        # else: yield scrapy.Request(url=urls[i], callback=cbs[i])

    def parse3(self, response):
        object = {}

        gen_names = [
            '//*[@id="Label255"]/text()',
            '//*[@id="Label256"]/text()',
            '//*[@id="Label257"]/text()',
            '//*[@id="Label258"]/text()',
            '//*[@id="Label259"]/text()',
            '//*[@id="Label271"]/text()',
            '//*[@id="Label272"]/text()',
            '//*[@id="Label275"]/text()',
            '//*[@id="Label276"]/text()',
            '//*[@id="Label277"]/text()',
            '//*[@id="Label280"]/text()',
            '//*[@id="Label281"]/text()',
            '//*[@id="Label314"]/text()',
        ]
        gen_amounts = [
            '//*[@id="L4"]/strong/text()',
            '//*[@id="L5"]/strong/text()',
            '//*[@id="L6"]/strong/text()',
            '//*[@id="L7"]/strong/text()',
            '//*[@id="L8"]/strong/text()',
            '//*[@id="L10"]/strong/text()',
            '//*[@id="L11"]/strong/text()',
            '//*[@id="L13"]/strong/text()',
            '//*[@id="L14"]/strong/text()',
            '//*[@id="L15"]/strong/text()',
            '//*[@id="L17"]/strong/text()',
            '//*[@id="L18"]/strong/text()',
            '//*[@id="L21"]/strong/text()',
        ]
        for i in range(len(gen_names)):
            gen = response.xpath(gen_names[0]).extract()
            amount = response.xpath(gen_amounts[0]).extract()
            if gen and amount:
                object["Generator: " + gen] = amount
        yield object


#if "twisted.internet.reactor" in sys.modules:
#    del sys.modules["twisted.internet.reactor"]
# This section is running the multiple spiders at once utilizing Scrapy Crawler Runner
# So far I have tried making a parent function named "chhattisgarhSLDC" and running this section
# That didn't work and neither did calling each chhattisgarhSLDC class
# The csv outputted runs chhattisgarhSLDC1 twice instead of running the other classes
#configure_logging()
#setting = get_project_settings()
#runner = CrawlerRunner(setting)
#runner.crawl(chhattisgarhSLDC1)
#runner.crawl(chhattisgarhSLDC2)
#runner.crawl(chhattisgarhSLDC3)
#d = runner.join()
#d.addBoth(lambda _: reactor.stop())
#reactor.run()
