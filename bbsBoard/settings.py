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

APP_ID = 'w359bnk9hh7z8fx0hsy6ee7b2tmf5va250hstatnu0a2iqbi'
MASTER_KEY = '6k2z44pax0ueopc4qmbnxa8gzg6inon0t2a7d1fc6czqm1ei'

LOG_LEVEL = 'INFO'
DOWNLOAD_TIMEOUT = 700

CONCURRENT_REQUESTS = 70
CONCURRENT_REQUESTS_PER_DOMAIN = 70

ITEM_PIPELINES = {
    'bbsBoard.pipelines.BoardPipeline': 300,
   # 'zhihut.pipelines.SecondPipline': 800,
}