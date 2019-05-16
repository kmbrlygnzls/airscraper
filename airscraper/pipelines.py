import csv

class SearchPipeline(object):
    def process_item(self, item, spider):
        item['flightNumber'] = item['flightNumber'].strip()
        item['fare'] = float(item['fare'].strip().strip('PHP').replace(',', ''))
        print(item)
        return item

class CsvWriterPipeline(object):
    def open_spider(self, spider):
        self.depart_file_handle = open('depart.csv', 'w')
        self.depart_file_handle.write("Date,FlightNumber,Fare")
        self.return_file_handle = open('return.csv', 'w')
        self.return_file_handle.write("Date,FlightNumber,Fare")

    def close_spider(self, spider):
        self.depart_file_handle.close()
        self.return_file_handle.close()

    def process_item(self, item, spider):
        date = item['date'].strip()
        flightNumber = item['flightNumber'].strip()
        fare = float(item['fare'].strip().strip('PHP').replace(',', ''))
        if item['type'] == 'depart':
            file_handle = self.depart_file_handle
        elif item['type'] == 'return':
            file_handle = self.return_file_handle
        file_handle.write("\n{},{},{}".format(date, flightNumber, fare))
        return item