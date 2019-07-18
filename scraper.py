import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    name = 'mmtdigital.co.uk'
    allowed_domains = ['mmtdigital.co.uk']
    start_urls = [
        'https://www.cargopedia.net/europe-fuel-prices',
    ]

    def parse(self, response):
        for td in response.xpath('//tr').getall():
            removeSlash = td.replace("\t", "").replace("\n","")
            removedImage = removeSlash.split("\xa0")

            try :
                namePrice = removedImage[1]
                infoArray = namePrice.split("</td><td>")
                country = infoArray[0].replace(" ","",1)
                petrol = infoArray[1]
                print("---")
                print(country)
                print(petrol)
                print("---")
            except :
                savedVar = "failed"

process = CrawlerProcess()

d = process.crawl(MySpider)
process.start()