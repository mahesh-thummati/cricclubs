# -*- coding: utf-8 -*-
import scrapy
from helper_methods_srcl import *


class GetDataTestSpider(scrapy.Spider):
    name = 'get_data_test'
    allowed_domains = ['cricclubs.com']
    custom_settings = {'FEED_URI': "../output/srcl_test_data_%(time)s.csv"}

    start_urls = [
        # 'https://cricclubs.com/SRCL/viewScorecard.do?matchId=2&clubId=4781',
        'https://cricclubs.com/SRCL/viewScorecard.do?matchId=60&clubId=4781',
        # 'https://cricclubs.com/SRCL/viewScorecard.do?matchId=250&clubId=4781'
    ]

    def parse(self, response):
        yield scrapy.Request(url=response.request.url, callback=extract_scorecard)
