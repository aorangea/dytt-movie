# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MovieItem


class VedioSpider(CrawlSpider):
    name = 'vedio'
    allowed_domains = ['www.ygdy8.com']
    start_urls = ['http://www.ygdy8.com/html/gndy/dyzz/list_23_%d.html' % i for i in range(1,162)]

    rules = (
        Rule(LinkExtractor(allow=r'/html/gndy/dyzz/\d+/\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = MovieItem()
        title = response.xpath("//h1/font/text()").extract_first()
        if response.xpath("//p/img[1]/@src").extract_first():
            pic = response.xpath("//p/img[1]/@src").extract_first()
        else:
            pic = response.xpath("//img/@src").extract()[1]
        string = response.xpath("//div[@class='co_content8']/ul/text()").extract()[0].replace('\r\n','').strip(' ')
        if string:
            showtime = string
        else:
            showtime = response.xpath("//div[@class='co_content8']/ul/text()").extract()[1].replace('\r\n','').strip(' ')
        if response.xpath("//table/tbody/tr/td/a/text()").extract_first():
            dload = response.xpath("//table/tbody/tr/td/a/text()").extract_first()
        else:
            dload = response.xpath("//td/font/a/text()").extract_first()
        item['title'] = title
        item['pic'] = pic
        item['showtime'] = showtime
        item['dload'] = dload
        yield item