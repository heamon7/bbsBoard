# -*- coding: utf-8 -*-

# Scrapy settings for bbsBoard project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbsBoard'

SPIDER_MODULES = ['bbsBoard.spiders']
NEWSPIDER_MODULE = 'bbsBoard.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbsBoard (+http://www.yourdomain.com)'
LOG_LEVEL = 'INFO'
DOWNLOAD_TIMEOUT = 700

CONCURRENT_REQUESTS = 70
CONCURRENT_REQUESTS_PER_DOMAIN = 70

ITEM_PIPELINES = {
    'bbsBoard.pipelines.BoardPipeline': 300,
   # 'zhihut.pipelines.SecondPipline': 800,
}