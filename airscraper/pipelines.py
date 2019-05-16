import csv

class SearchPipeline(object):
    def process_item(self, item, spider):
        item['flightNumber'] = item['flightNumber'].strip()
        item['fare'] = float(item['fare'].strip().strip('PHP').replace(',', ''))
        return item

class CsvWriterPipeline(object):
    def open_spider(self, spider):
        self.file_handle = open('items.csv', 'w')
        # csvWriter = csv.writer(self.file, delimiter= ',')
        self.file_handle.write("Date,FlightNumber,Fare")

    def close_spider(self, spider):
        self.file_handle.close()

    def process_item(self, item, spider):
        flightNumber = item['flightNumber'].strip()
        fare = float(item['fare'].strip().strip('PHP').replace(',', ''))
        self.file_handle.write("\n{},{}".format(flightNumber, fare))
        return item