# -*- coding: utf-8 -*-
import scrapy


class TtlsaSpider(scrapy.Spider):
    name = 'ttlsa'
    allowed_domains = ['www.ttlsa.com']
    start_urls = ['http://www.ttlsa.com/']

    def ArtileParse(self, response):
        title = response.css("entry-title::a(herf):text").extract.first()

    def parse(self, response):
        pass
