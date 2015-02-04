# -*- coding: utf-8 -*-

# Scrapy settings for oreilly project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'oreilly'

SPIDER_MODULES = ['oreilly.spiders']
NEWSPIDER_MODULE = 'oreilly.spiders'

AUTOTHROTTLE_ENABLED = True

ITEM_PIPELINES = {
    'oreilly.pipelines.OreillyPipeline': 300,
  }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'oreilly (+http://www.yourdomain.com)'
