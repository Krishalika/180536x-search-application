import scrapy
from text_corpus.items import TextCorpusItem
from datetime import datetime
import re
import json 
import codecs
import html
class TextCorpus(scrapy.Spider):
	name = "my_scraper"

	# First Start Url
	start_urls = ["https://www.sinhalasongbook.com/category/amarasiri-peiris", "https://www.sinhalasongbook.com/category/milton-mallawarachchi", "https://www.sinhalasongbook.com/category/amaradewa", "https://www.sinhalasongbook.com/category/t-m-jayarathna"]

	npages = 3 #original pages 4
	npg = 2
	noPage = 1
	# This mimics getting the pages using the next button. 
	for i in range(2, npages + 2):
		start_urls.append("	https://www.sinhalasongbook.com/category/milton-mallawarachchi/page/"+str(i)+"/")

	for i in range(2, npg + 2):
		start_urls.append("	https://www.sinhalasongbook.com/category/amaradewa/page/"+str(i)+"/")

	for i in range(2, noPage + 2):
		start_urls.append("	https://www.sinhalasongbook.com/category/t-m-jayarathna/page/"+str(i)+"/")
		# start_urls.append("https://fundrazr.com/find?category=Health&page="+str(i)+"")
	def parse(self, response):
		for href in response.xpath("//h2[contains(@class, 'entry-title')]/a[contains(@class, 'entry-title-link')]//@href"):
			# add the scheme, eg http://
			# url  = "https:" + href.extract() 
			# yield scrapy.Request(url, callback=self.parse_dir_contents)	
			yield scrapy.Request(href.extract(), callback=self.parse_dir_contents)	

	def parse_dir_contents(self, response):
		item = TextCorpusItem()

		# Getting Song Name
		# item['songName'] = response.xpath("//h1[contains(@class, 'entry-title')]/descendant::text()").extract()[0]
		uni_string = response.xpath("//span[contains(@class, 'sinTitle')]/descendant::text()").extract()[0]
		bytes_object = uni_string.encode('utf-8')
		item['songName'] = bytes_object.decode('utf-8')
		# item['songName'].decode('utf-8')response.xpath("//span[contains(@class, 'sinTitle')]/descendant::text()").extract()[0]
		# Getting singer
		item['singer']= response.xpath("//span[contains(@class, 'entry-categories')]/descendant::text()").extract()[1].strip()

		# lyricist
		item['lyricist']= response.xpath("//span[contains(@class, 'lyrics')]/descendant::text()").extract()[1].strip()

		# genre
		item['genre'] = response.xpath("//span[contains(@class, 'entry-tags')]/descendant::text()").extract()[1].strip()

		# # album
		# item['album'] = response.xpath("//span[contains(@class, 'sinTitle')]/descendant::text()").extract()[0].strip()

		# # year
		# item['year'] = response.xpath("//span[contains(@class, 'sinTitle')]/descendant::text()").extract()[0].strip()

		# composer
		item['composer'] = response.xpath("//span[contains(@class, 'music')]/descendant::text()").extract()[1].strip()

		# song

		# # Getting Story
		# story_list = response.xpath("//div[contains(@id, 'full-story')]/descendant::text()").extract()
		# story_list = [x.strip() for x in story_list if len(x.strip()) > 0]
		# item['story']  = " ".join(story_list)

		# # Url (The link to the page)
		# item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()

		yield item

