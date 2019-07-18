import scrapy
from scrapy.crawler import CrawlerProcess

countryFuelPrices = {"fuelPrices": []}

class MySpider(scrapy.Spider):
    name = 'Petrol Prices'
    allowed_domains = ['cargopedia.net']
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
                diesel = infoArray[2]
                countryFuelPrices['fuelPrices'].append({
                    "country": country,
                    "petrol": petrol,
                    "diesel": diesel
                })
            except :
                savedVar = "failed"


def handelProcess():
    process = CrawlerProcess()
    d = process.crawl(MySpider)
    process.start()

def getFuelPrices():
    return countryFuelPrices