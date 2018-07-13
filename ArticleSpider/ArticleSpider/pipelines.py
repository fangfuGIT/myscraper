# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from scrapy.exporters import CsvItemExporter
import MySQLdb
import pymongo


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonExporterPipeline(object):
    # 调用scarpy提供的json export导出json文件
    def __init__(self):
        self.file = open('JsonExporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class CsvExporterPipeline(object):
    def __init__(self):
        self.file = open('CsvExporter.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding="utf8")
        self.exporter.start_exporting()

    def close_spider(self):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ArticleImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for key, vault in results:
            image_file_path = vault["path"]
        item["front_image_path"] = image_file_path

        return item


    pass


