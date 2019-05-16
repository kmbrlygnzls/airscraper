import csv

class SearchPipeline(object):
    def process_item(self, item, spider):
        item['flightNumber'] = item['flightNumber'].strip()
        item['fare'] = float(item['fare'].strip().strip('PHP').replace(',', ''))
        print item
        return item

class CsvWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.csv', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        csvWriter = csv.writer(self.file, delimiter= ',')
        date = item['date'].strip()
        flightNumber = item['flightNumber'].strip()
        fare = float(item['fare'].strip().strip('PHP').replace(',', ''))
        csvWriter.writerow([date, flightNumber, fare])
        return item