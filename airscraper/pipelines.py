# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don"t forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class AirscraperPipeline(object):
    def process_item(self, item, spider):
        return item

class SearchPipeline(object):
    def process_item(self, item, spider):
        item["flightNumber"] = item["flightNumber"].strip()
        item["fare"] = float(item["fare"].strip().strip("PHP").replace(',', ''))
        print item
        return item