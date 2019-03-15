# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyanchaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shareholder = scrapy.Field()
    holding_company = scrapy.Field()
    company_status = scrapy.Field()
