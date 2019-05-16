class SearchPipeline(object):
    def process_item(self, item, spider):
        item['flightNumber'] = item['flightNumber'].strip()
        item['fare'] = float(item['fare'].strip().strip('PHP').replace(',', ''))
        print item
        return item