# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.http import Request,FormRequest

import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem

from  bbsBoard.items import BbsboardItem

class BoarderSpider(scrapy.Spider):
    name = "boarder"
    allowed_domains = ["m.byr.cn"]
    baseUrl = 'http://m.byr.cn'
    start_urls = (
        'http://www.m.byr.cn/',
    )
    def __init__(self):
        leancloud.init('mctfj249nwy7c1ymu3cps56lof26s17hevwq4jjqeqoloaey', master_key='ao6h5oezem93tumlalxggg039qehcbl3x3u8ofo7crw7atok')

        Sections = Object.extend('Sections')
        query = Query(Sections)
        query.start_with('sectionLink')
        query.select('sectionLink')
        sections= query.find()
        self.urls = []
        for section in sections:
            self.urls.append(self.baseUrl+section.get('sectionLink'))

    def start_requests(self):
        print "start_requests ing ......"
        print self.urls
        for url in self.urls:
            yield Request(url,callback = self.parse)

    def parse(self, response):

        item = BbsboardItem()
      #  inspect_response(response,self)
        link = response.xpath('//*[@id="m_main"]/ul/li/a/@href').extract()
        name = response.xpath('//*[@id="m_main"]/ul/li/a/text()').extract()

      #  print item['sectionListLink']
        return item
