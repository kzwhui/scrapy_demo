# -*- coding: utf-8 -*-

import urlparse
import scrapy
from bs4 import BeautifulSoup
from scrapy_demo.items import ScrapyDemoItem


class TopmoviesSpider(scrapy.Spider):
    name = "topmovies"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/top250/']

    def start_requests(self):
        for url in self.start_urls:
            hostname = urlparse.urlparse(url).netloc
            header={'Host':hostname, 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/53.0.2785.143 Safari/537.36'}
            yield scrapy.Request(url=url, callback=self.parse, headers=header)

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        divs = soup.find_all('div', {'class':'item'})
    
        items = []
        for div in divs:
            item = ScrapyDemoItem()
            item['name'] = div.find('span').string.strip()
            item['url'] = div.find('div', {'class':'hd'}).a.get('href')
            items.append(item)
        return items
