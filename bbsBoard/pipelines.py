# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import leancloud
from leancloud import Object
from leancloud import LeanCloudError
from leancloud import Query
from scrapy import log
from scrapy.exceptions import DropItem
from bbsBoard import settings

class BoardPipeline(object):
    def __init__(self):
        leancloud.init(settings.APP_ID, master_key=settings.MASTER_KEY)

    def process_item(self, item, spider):

        Sections = Object.extend('Sections')
        Boards = Object.extend('Boards')
        for index ,link in enumerate(item['link']):
            if 'board' == re.split('/(\w*)/*',link)[1]:
                board = Boards()
                query = Query(Boards)
                boardId = re.split('/board/',link)[1]
                query.equal_to('boardId',boardId)
                try:
                    if query.find():
                        pass
                    else:
                        board.set('boardId',boardId)
                        board.set('boardLink',link)
                        board.set('boardName',item['name'][index])
                        board.set('parentLink',item['parentLink'])
                        try:
                            board.save()
                        except LeanCloudError,e:
                            print e
                except LeanCloudError,e:
                    print e

            else:
                section = Sections()
                #sectionId = re.split('/section/',link)
                query = Query(Sections)
                query.equal_to('sectionLink',link)
                try:
                    if query.find():
                        pass
                    else:
                        section.set('sectionLink',link)
                        section.set('sectionName',item['name'][index])
                        section.set('parentLink',item['parentLink'])
                        try:
                            section.save()
                        except LeanCloudError,e:
                            print e
                except LeanCloudError,e:
                    print e



        #return item
        DropItem()
