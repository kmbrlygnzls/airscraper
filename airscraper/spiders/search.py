import scrapy
import csv

class SearchSpider(scrapy.Spider):
    name = 'search'

    def start_requests(self):
        oneWayUrl = 'https://book.cebupacificair.com/Flight/Select?o1=' + self.origin + '&d1=' + self.destination + '&dd1=' + self.departureDate

        urls = [
            oneWayUrl
        ]

        with open('items.csv', newline='') as csvfile:
            csvWriter = csv.writer(csvfile, delimiter= ',')
            for url in urls:
                # csvWriter.writerow(scrapy.Request(url=url, callback=self.parse))
                yield (scrapy.Request(url=url, callback=self.parse))

    def parse(self, response):
        fareTable = response.css('tbody')
        for fareRow in fareTable.css('.faretable-row'):
            return {
                'flightNumber': fareRow.css('.flight-number ::text').extract_first(),
                'fare': fareRow.css('.fare-amount ::text').extract_first()
            }
        #next_page_url = response.css('li.next > a::attr(href)').extract_first()
        #if next_page_url is not None:
            #yield scrapy.Request(response.urljoin(next_page_url))

