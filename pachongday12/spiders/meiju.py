# -*- coding: utf-8 -*-
import scrapy
from pachongday12.items import Pachongday12Item

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']


    def parse(self, response):
        print(response.body.decode('gb2312'))
        obj_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for obj in obj_list:
            item = Pachongday12Item()

            #排名：
            num = obj.xpath('.//div[@class="lasted-num fn-left"]/i/text()').extract()[0]
            item['num']=num
            #电影名称：
            name = obj.xpath('.//h5//text()').extract()[0]
            item['name'] = name
            #小分类：
            type = obj.xpath('.//span[@class="mjjq"]/text()').extract()[0]
            item['type'] = type
            #电视台：
            tv = obj.xpath('.//span[@class="mjtv"]/text()').extract()[0]
            item['tv'] = tv
            #更新时间：
            time = obj.xpath('.//div[@class="lasted-time new100time fn-right"]//text()').extract()[0]
            item['time'] = time
            #路径：
            base_url = obj.xpath('.//h5/a/@href').extract()[0]
            url = 'https://www.meijutt.com'+base_url
            item['url'] = url

            yield scrapy.Request(url=url,callback=self.pares_detail,meta={'data':item,'phjs':True},dont_filter=False)

    def pares_detail(self,response):
        item = response.meta['data']
        info_list = response.xpath('//div[@class="o_r_contact"]/ul')
        for info in info_list:
            #导演：
            dy = info.xpath('./li[4]/span/text()').extract()[0]
            item['dy']=dy
            #主演：
            zy = info.xpath('./li[5]/span/text()').extract()[0]
            item['zy'] = zy
            yield item


