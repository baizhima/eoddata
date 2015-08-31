# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EoddataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Code = scrapy.Field()
    Name = scrapy.Field()
    High = scrapy.Field()
    Low = scrapy.Field()
    Close = scrapy.Field()
    Volume = scrapy.Field()
    ChangeAbs = scrapy.Field()
    ChangePct = scrapy.Field()
