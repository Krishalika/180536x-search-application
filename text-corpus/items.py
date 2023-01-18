import scrapy

class TextCorpusItem(scrapy.Item):
    # define the fields for song item 

    songName = scrapy.Field() 
    lyricist = scrapy.Field()
    singer = scrapy.Field()
    genre = scrapy.Field()
    composer = scrapy.Field()


