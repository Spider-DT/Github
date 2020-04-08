# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    type = scrapy.Field()
    city = scrapy.Field()
    category = scrapy.Field()
    num = scrapy.Field()
    education = scrapy.Field()
    needs = scrapy.Field()
    date = scrapy.Field()