# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AcademyItem(scrapy.Item):
    title = scrapy.Field()
    teacher = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()