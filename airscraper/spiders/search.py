import scrapy
import csv

class SearchSpider(scrapy.Spider):
    name = 'search'

    def start_requests(self):
        if self.option == 'oneWaySingleDate':
            urls = ['https://book.cebupacificair.com/Flight/Select?o1=' + self.origin + '&d1=' + self.destination + '&dd1=' + self.departureDate]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        dateBox = response.css('.active.flights-schedule-col')
        dateYear = dateBox.css('a ::attr(data-curdateyear)').extract_first()
        dateMonth = dateBox.css('a ::attr(data-curdatemonth)').extract_first()
        dateDay = dateBox.css('a ::attr(data-curdateday)').extract_first()
        date = dateYear + '-' + dateMonth + '-' + dateDay

        fareTable = response.css('tbody')
        for fareRow in fareTable.css('.faretable-row'):
            yield {
                'date': date,
                'flightNumber': fareRow.css('.flight-number ::text').extract_first(),
                'fare': fareRow.css('.fare-amount ::text').extract_first()
            }

