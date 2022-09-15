# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TransformerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Transformer_name = scrapy.Field()
    Transformer_load = scrapy.Field()
class LineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Line_name = scrapy.Field()
    Line_load = scrapy.Field()
