# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 总类别
class LdzXiaoshuoyueduLei(scrapy.Item):
    # 类别
    category = scrapy.Field()
    # 类别链接
    CGurl = scrapy.Field()

    def database_name_table(self,dataDict):
        sql = 'INSERT INTO data_01_zonglei(%s) VALUES (%s)' % (
        ','.join(dataDict.keys()), ','.join(['%s'] * len(dataDict)))

        data = list(dataDict.values())

        return sql, data


# 列表
class LdzXiaoshuoyueduItem(scrapy.Item):
    # 书名
    bookname = scrapy.Field()
    # 图片链接
    img_url = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 类别
    category = scrapy.Field()
    # 状态
    State = scrapy.Field()
    # 字数
    WordNumber = scrapy.Field()
    # 简介
    introduce = scrapy.Field()

    def database_name_table(self, dataDict):
        sql = 'INSERT INTO data_01_liebiao(%s) VALUES (%s)' % (
            ','.join(dataDict.keys()), ','.join(['%s'] * len(dataDict)))

        data = list(dataDict.values())

        return sql, data

# 章节
class LdzXiaoshuoyueduZhangJie(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 链接
    zj_link = scrapy.Field()
    #是否免费
    mf = scrapy.Field()

    def database_name_table(self, dataDict):
        sql = 'INSERT INTO data_01_zhangjie(%s) VALUES (%s)' % (
            ','.join(dataDict.keys()), ','.join(['%s'] * len(dataDict)))

        data = list(dataDict.values())

        return sql, data

# 详情
class LdzXiaoshuoyueduContent(scrapy.Field):
    #章节名称
    title = scrapy.Field()
    #书名
    bookname = scrapy.Field()
    #作者
    author = scrapy.Field()
    #本章字数
    WordNumber = scrapy.Field()
    #发布时间
    FaBuData = scrapy.Field()
    #内容
    content = scrapy.Field()
    def database_name_table(self, dataDict):
        sql = 'INSERT INTO data_01_content(%s) VALUES (%s)' % (
            ','.join(dataDict.keys()), ','.join(['%s'] * len(dataDict)))

        data = list(dataDict.values())

        return sql, data

