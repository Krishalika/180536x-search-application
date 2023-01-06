# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TextCorpusItem(scrapy.Item):
    # define the fields for your item here like:

    # songName = getattr(scrapy, 'Field', 'unknown')
    # lyricist = getattr(scrapy, 'Field', 'unknown')
    # singer = getattr(scrapy, 'Field', 'unknown')
    # genre = getattr(scrapy, 'Field', 'unknown')
    # composer = getattr(scrapy, 'Field', 'unknown')

    songName = scrapy.Field() 
    lyricist = scrapy.Field()
    singer = scrapy.Field()
    genre = scrapy.Field()
    # album = scrapy.Field()
    # year = scrapy.Field()
    composer = scrapy.Field()
    # song = scrapy.Field()
    # url = scrapy.Field()


