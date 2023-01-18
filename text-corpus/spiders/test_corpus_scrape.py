import scrapy
from text_corpus.items import TextCorpusItem

class TextCorpus(scrapy.Spider):
	name = "my_scraper"

	# First Start Url
	start_urls = ["https://www.sinhalasongbook.com/category/amarasiri-peiris", "https://www.sinhalasongbook.com/category/milton-mallawarachchi", "https://www.sinhalasongbook.com/category/amaradewa", "https://www.sinhalasongbook.com/category/t-m-jayarathna"]

	npages_1 = 3 
	npages_2 = 2
	npages_3 = 1
	# This mimics getting the pages using the next button. 
	for i in range(2, npages_1 + 2):
		start_urls.append("	https://www.sinhalasongbook.com/category/milton-mallawarachchi/page/"+str(i)+"/")

	for i in range(2, npages_2 + 2):
		start_urls.append("	https://www.sinhalasongbook.com/category/amaradewa/page/"+str(i)+"/")

	for i in range(2, npages_3 + 2):
		start_urls.append("	https://www.sinhalasongbook.com/category/t-m-jayarathna/page/"+str(i)+"/")

	def parse(self, response):
		for href in response.xpath("//h2[contains(@class, 'entry-title')]/a[contains(@class, 'entry-title-link')]//@href"):
			yield scrapy.Request(href.extract(), callback=self.parse_dir_contents)	

	def parse_dir_contents(self, response):
		item = TextCorpusItem()

		# Getting Song Name
		uni_string = response.xpath("//span[contains(@class, 'sinTitle')]/descendant::text()").extract()[0]
		bytes_object = uni_string.encode('utf-8')
		item['songName'] = bytes_object.decode('utf-8')

		# Getting singer
		item['singer']= response.xpath("//span[contains(@class, 'entry-categories')]/descendant::text()").extract()[1].strip()

		# lyricist
		item['lyricist']= response.xpath("//span[contains(@class, 'lyrics')]/descendant::text()").extract()[1].strip()

		# genre
		item['genre'] = response.xpath("//span[contains(@class, 'entry-tags')]/descendant::text()").extract()[1].strip()

		# composer
		item['composer'] = response.xpath("//span[contains(@class, 'music')]/descendant::text()").extract()[1].strip()

		yield item

