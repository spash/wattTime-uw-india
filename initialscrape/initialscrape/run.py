from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.manipurSLDC_Spider import ManipurSLDC
from spiders.manipurSLDC_Spider2 import ManipurSLDC2
from spiders.manipurSLDC_Spider3 import ManipurSLDC3

def run():
    configure_logging()
    # importing project settings for further usage
    # mainly because of the middlewares
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    # running spiders sequentially (non-distributed)
    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(ManipurSLDC)
        yield runner.crawl(ManipurSLDC2)
        yield runner.crawl(ManipurSLDC3)
        reactor.stop()

    crawl()
    reactor.run() # block until the last call

run()