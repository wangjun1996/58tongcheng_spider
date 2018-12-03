# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TongchengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 房屋介绍
    describe = scrapy.Field()
    # 房间情况
    room = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 朝向
    direction = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 小区
    neighbourhood = scrapy.Field()
    # 区域
    district = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 出售总价
    price = scrapy.Field()
    # 单价
    unit = scrapy.Field()
    # 链接
    link = scrapy.Field()