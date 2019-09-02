# -*- coding: utf-8 -*-
import scrapy
from helper_methods_non_srcl import *


class GetDataNonSrclSpider(scrapy.Spider):
    name = 'get_data_non_srcl'
    allowed_domains = ['cricclubs.com']
    custom_settings = {'FEED_URI': "../output/non_srcl_data_%(time)s.csv"}

    start_urls = ['https://cricclubs.com/GCRA/listMatches.do?league=11&teamId=67&clubId=3933',
                  'https://cricclubs.com/GCRA/listMatches.do?league=9&teamId=51&clubId=3933',
                  'https://cricclubs.com/GCRA/listMatches.do?league=2&teamId=23&clubId=3933',
                  'https://cricclubs.com/GCRA/listMatches.do?league=1&teamId=9&clubId=3933',
                  'https://cricclubs.com/ACL2018/listMatches.do?league=3&teamId=25&clubId=3890',
                  'https://cricclubs.com/ACL2018/listMatches.do?league=3&teamId=56&clubId=3890',
                  'https://cricclubs.com/ACL2018/listMatches.do?league=2&teamId=3&clubId=3890',
                  'https://cricclubs.com/CharlottePremierLeagueGaneshCup2017/listMatches.do?league=3&teamId=80&clubId=3568',
                  'https://cricclubs.com/CharlottePremierLeagueGaneshCup2017/listMatches.do?league=4&teamId=95&clubId=3568',
                  'https://cricclubs.com/Super8League/listMatches.do?league=1&teamId=20&clubId=6347'
                  ]

    def parse(self, response):
        for href in response.css('table#myTable td a::attr("href")').extract():
            if "viewScorecard" in href:
                url = response.urljoin(href)
                yield scrapy.Request(url=url, callback=extract_scorecard)
