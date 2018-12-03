# -*- coding: utf-8 -*-
import scrapy
import re
from tongcheng.items import TongchengItem


class TongchengSpiderSpider(scrapy.Spider):
    name = 'tongcheng_spider'
    allowed_domains = ['dl.58.com']
    start_urls = ['https://dl.58.com/ershoufang/pn1/']

    def parse(self, response):
        # print(response.text)
        house_list = response.xpath("//div[@class='content-side-left']/ul/li")
        for i_item in house_list:
            tongcheng_item = TongchengItem()

            content = i_item.xpath(".//h2[@class='title']/a/text()").extract()
            for i_content in content:
                conten_s = ".".join(i_content.split())
                tongcheng_item['describe'] = conten_s

            room = i_item.xpath(".//p[@class='baseinfo'][1]/span[1]/text()").extract_first()
            if room != 'None':
                tongcheng_item['room'] = room

            area = i_item.xpath(".//p[@class='baseinfo'][1]/span[2]/text()").extract_first()
            if area != 'None':
                tongcheng_item['area'] = "".join(area.split())[:-1]

            direction = i_item.xpath(".//p[@class='baseinfo'][1]/span[3]/text()").extract_first()
            tongcheng_item['direction'] = direction

            floor = i_item.xpath(".//p[@class='baseinfo'][1]/span[4]/text()").extract_first()
            tongcheng_item['floor'] = floor

            address = i_item.xpath(".//p[@class='baseinfo'][2]//a[3]/text()").extract_first()
            if address is None:   # 此处代码作用是去除每页数据间隔的空行
                break
            tongcheng_item['address'] = address

            neighbourhood = i_item.xpath(".//p[@class='baseinfo'][2]//a[1]/text()").extract_first()
            if neighbourhood != 'None':
                tongcheng_item['neighbourhood'] = neighbourhood

            district = i_item.xpath(".//p[@class='baseinfo'][2]//a[2]/text()").extract_first()
            tongcheng_item['district'] = district

            price = i_item.xpath(".//p[@class='sum']/b/text()").extract_first()
            tongcheng_item['price'] = price

            unit = i_item.xpath(".//p[@class='unit']/text()").extract_first()
            tongcheng_item['unit'] = unit

            link = i_item.xpath(".//h2/a/@href").extract_first()
            tongcheng_item['link'] = link

            yield tongcheng_item
            # print(tongcheng_item)

        next_link = response.xpath("//div[@class='pager']/strong/span/text()").extract()
        # for i in range(5):
        if next_link:
            next_link[0] = int(next_link[0]) + 1
            # print(next_link[0])
            yield scrapy.Request('https://dl.58.com/ershoufang/pn' + str(next_link[0]), callback=self.parse)
