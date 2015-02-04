import scrapy

from oreilly.items import EbookItem
from scrapy.http import Request

#from scrapy.selector.unified import __nonzero__

from oreilly.utils import *

import re

class OreillySpider(scrapy.Spider):
    name = "oreilly"
    #allowed_domains = ["chimera.labs.oreilly.com/"]
    start_urls = [
        "http://chimera.labs.oreilly.com/books"
    ]

    def parse(self, response):
        for sel in response.css('#books .book'):
            item = EbookItem()
            first_page = sel.css('a::attr(href)').extract()
            url = normalizeUrl(first_page[0], response)
            yield Request(url, callback=self.parseFirstPage, meta={'item': item})

    def parseFirstPage(self, response):
        item = response.meta['item']
        item['author']=None
        item['title']=None
        item['content']=None

        print  response.url

        if "index.html" in response.url :
            #because it's the book
            print "index.html"
            return Request(response.url, callback=self.parseFirstEbookPage, meta={'item': item})
        else:
            #item = response.meta['item']
            #item['author']
            for sel in response.css('#splash .span7 a'):
                btn = sel.css('a').extract()
                print "xxx"
                for i in btn:
                    print i
                    if "index.html" in i:
                        print "ok"
                        url = re.search( r'href="(.*?)"', i)
                        url = normalizeUrl(url.group(1), response)
                        return Request(url, callback=self.parseFirstEbookPage, meta={'item': item})

            # link not find
            return item


    def parseFirstEbookPage(self, response):
        item = response.meta['item']
        item['content']={}

        print "parseFirstEbookPage"
        author = ""
        for sel in response.css(".author"):
            if not sel :
                pass
            else:
                if sel.css(".firstname::text").extract() and sel.css(".surname::text").extract():
                    author = author + "," +sel.css(".firstname::text").extract()[0] + sel.css(".surname::text").extract()[0]


        if author == "":
            print "not author"
            pass
        else:
            item['author']= author[0]
            print "auteur" + item['author'][0]

        title = response.css("h1.title::text").extract()
        if not title:
            pass
        else:
            item['title']= title[0]
            print "title" + item['title']

        url = response.css('header a[accesskey="n"]::attr(href)').extract()
        if url:
            url = normalizeUrl(url[0], response)
            return Request(url, callback=self.parseContent, meta={'item': item})
        else :
            return item
        '''
        url = response.css('header a::attr(a)').extract()
        if url :
            print "oohoho"+url
            url = normalizeUrl(url, response)
            return Request(url, callback=self.parseContent, meta={'item': item})
        else:
            return item
        '''

    def parseContent(self, response):
        item = response.meta['item']
        item['content'] = ""
        content = re.search(r'</header>(.*)<footer>' ,response.body, re.DOTALL)       
        item['content']= item['content'] + content.group(1) 

        url = response.css('header a[accesskey="n"]::attr(href)').extract()
        
        if url:
            url = normalizeUrl(url[0], response)
            return Request(url, callback=self.parseContent, meta={'item': item})

        return item