# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.http import Request,FormRequest

import re
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem

from  bbsBoard.items import BbsboardItem
import os

from bbsBoard import settings

class BoarderSpider(scrapy.Spider):
    name = "boarder"
    allowed_domains = ["m.byr.cn"]
    baseUrl = 'http://m.byr.cn'
    start_urls = (
        'http://www.m.byr.cn/',
    )
    def __init__(self,stats):
        self.stats = stats
        leancloud.init(settings.APP_ID, master_key=settings.MASTER_KEY)

        Sections = Object.extend('Sections')
        query = Query(Sections)
        query.exists('sectionLink')
        query.select('sectionLink')
        sections= query.find()
        self.urls = []
        for section in sections:
            self.urls.append(self.baseUrl+section.get('sectionLink'))

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def start_requests(self):
        #print "start_requests ing ......"
        #print self.urls
        for url in self.urls:
            yield Request(url,callback = self.parse)

    def parse(self, response):

        item = BbsboardItem()
      #  inspect_response(response,self)
        item['link'] = response.xpath('//*[@id="m_main"]/ul/li/a/@href').extract()
        item['name'] = response.xpath('//*[@id="m_main"]/ul/li/a/text()').extract()
        item['parentLink'] = re.split('http://m.byr.cn(\w*)',response.url)[2]
      #  print item['sectionListLink']
	#print re.split('http://m.byr.cn(\w*)',response.url)
        return item

    def closed(self,reason):
        #f = open('../../nohup.out')
        #print f.read()
        try:
            nohupOut = open(os.getcwd()+'/nohup.out','r').read()
        except:
            nohupOut = "Cannot read nohup.out file"

        CrawlerLog = Object.extend('CrawlerLog')
        crawlerLog = CrawlerLog()
        crawlerLog.set('crawlerName',self.name)
        crawlerLog.set('crawlerLog',nohupOut)
        crawlerLog.set('closedReason',reason)
        crawlerLog.set('crawlerStats',self.stats.get_stats())
        try:
            crawlerLog.save()
        except:
            pass