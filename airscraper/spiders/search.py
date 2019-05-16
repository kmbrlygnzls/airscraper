import scrapy
import csv

class SearchSpider(scrapy.Spider):
    name = 'search'

    def start_requests(self):
        if self.option == 'oneWaySingleDate':
            urls = ['https://book.cebupacificair.com/Flight/Select?o1=' + self.origin + '&d1=' + self.destination + '&dd1=' + self.departureDate]

        if self.option == 'multipleSingleDate':
            urls = []
            destinations = self.destinations.split(',')
            for destination in destinations:
                url = 'https://book.cebupacificair.com/Flight/Select?o1=' + self.origin + '&d1=' + destination + '&dd1=' + self.departureDate
                urls.append(url)

        if self.option == 'roundTripDateRange':
            urls = ['https://book.cebupacificair.com/Flight/Select?o1=' + self.origin + '&d1=' + self.destination + '&dd1=' + self.departureDate + '&dd2=' + self.returnDate + '&r=true']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        flightTypeIDMap = {
            'depart-table': 'depart-flight-schedule',
            'return-table': 'return-flight-schedule'
        }

        fareContainer = response.css('.select-flight-container')
        for fareTable in fareContainer.css('.flight-table'):
            flightType = fareTable.css('table ::attr(id)').extract_first().strip()
            dateBox = response.css('.' + flightTypeIDMap[flightType])
            dateBox = dateBox.css('.active.flights-schedule-col')
            dateYear = dateBox.css('a ::attr(data-curdateyear)').extract_first()
            dateMonth = dateBox.css('a ::attr(data-curdatemonth)').extract_first()
            dateDay = dateBox.css('.day ::text').extract_first()
            date = dateYear + '-' + dateMonth + '-' + dateDay
            for fareRow in fareTable.css('.faretable-row'):
                yield {
                    'date': date,
                    'flightNumber': fareRow.css('.flight-number ::text').extract_first(),
                    'fare': fareRow.css('.fare-amount ::text').extract_first()
                }

