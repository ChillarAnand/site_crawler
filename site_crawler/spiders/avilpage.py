# -*- coding: utf-8 -*-
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from site_crawler.items import SiteCrawlerItem


class AvilpageSpider(CrawlSpider):
    name = 'avilpage'
    allowed_domains = ['www.avilpage.com']
    start_urls = ['http://www.avilpage.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.avilpage.com/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = SiteCrawlerItem()
        i['link'] = response.xpath('//body//a/@href').extract()
        with open('log.txt', 'a') as f:
            f.write(str(i['link']) + '\n')
        return i
