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

class BoardPipeline(object):
    def __init__(self):
        leancloud.init('mctfj249nwy7c1ymu3cps56lof26s17hevwq4jjqeqoloaey', master_key='ao6h5oezem93tumlalxggg039qehcbl3x3u8ofo7crw7atok')

    def process_item(self, item, spider):

        Sections = Object.extend('Sections')
        Boards = Object.extend('Boards')
        for index ,link in enumerate(item['link']):
            if 'board' == re.split('/\w*/*',link)[1]:
                board = Boards()
                query = Query(Boards)
                query.equal_to('boardLink',link)
                try:
                    if query.find():
                        pass
                    else:
                        board.set('boardLink',link)
                        board.set('boardName',item['name'][index])
                        try:
                            board.save()
                        except LeanCloudError,e:
                            print e
                except LeanCloudError,e:
                    print e

            else:
                section = Sections()
                query = Query(Sections)
                query.equal_to('sectionLink',link)
                try:
                    if query.find():
                        pass
                    else:
                        section.set('sectionLink',link)
                        section.set('sectionName',item['name'][index])
                        try:
                            section.save()
                        except LeanCloudError,e:
                            print e
                except LeanCloudError,e:
                    print e



        return item
        #DropItem()
