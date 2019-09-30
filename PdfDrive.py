# -*- coding: utf-8 -*-
import scrapy


class PdfdriveSpider(scrapy.Spider):
    name = 'PdfDrive'
    allowed_domains = ['www.pdfdrive.com/']
    start_urls = ['http://www.pdfdrive.com//']


    def parse(self, response):
        Books_of_week=response.xpath('/html/body/div[3]/div[1]/div[1]/div[4]/ul/li//a/h2/text()').extract()

        Category=response.xpath('//*[@id="categories"]/div[1]')

        list=Category.xpath('.//ul/li/a/p/text()').extract()

        Books=Category.xpath('.//ul/li/a/@href').extract()
        for Book in Books:
            url = 'http://books.toscrape.com/' + Book

            yield {'Categories of Books': list ,
                            'Best Books of the week':Books_of_week,
                            'links':Books,
                            'URL for Category':url }
