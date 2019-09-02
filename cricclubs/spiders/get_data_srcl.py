# -*- coding: utf-8 -*-
import scrapy
import time
from helper_methods_srcl import *


class GetDataSrclSpider(scrapy.Spider):
    name = 'get_data_srcl'
    allowed_domains = ['cricclubs.com']
    custom_settings = {'FEED_URI': "../output/srcl_data_%(time)s.csv"}

    def start_requests(self):
        urls = [
            'https://cricclubs.com/SRCL/listMatches.do?league=14&teamId=220&clubId=4781',
            'https://cricclubs.com/SRCL/listMatches.do?league=11&teamId=147&clubId=4781',
            'https://cricclubs.com/SRCL/listMatches.do?league=1&teamId=4&clubId=4781',
        ]
        for url in urls:
            # print "Season: {}".format(url)
            # time.sleep(2)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print response.status
        # print "Season: {}".format(response.request.url)
        for href in response.css('div.schedule-all div.row div.col-lg-2 li a::attr("href")'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url=url, callback=extract_scorecard)
