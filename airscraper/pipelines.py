import csv

class SearchPipeline(object):
    def process_item(self, item, spider):
        item['flightNumber'] = item['flightNumber'].strip()
        item['fare'] = float(item['fare'].strip().strip('PHP').replace(',', ''))
        print(item)
        return item

class CsvWriterPipeline(object):
    def open_spider(self, spider):
        self.file_handle = open('items.csv', 'w')
        self.file_handle.write("Date,FlightNumber,Fare")

    def close_spider(self, spider):
        self.file_handle.close()

    def process_item(self, item, spider):
        date = item['date'].strip()
        flightNumber = item['flightNumber'].strip()
        fare = float(item['fare'].strip().strip('PHP').replace(',', ''))
        self.file_handle.write("\n{},{},{}".format(date, flightNumber, fare))
        return item