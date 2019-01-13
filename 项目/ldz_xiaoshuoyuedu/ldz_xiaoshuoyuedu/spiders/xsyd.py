# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ldz_xiaoshuoyuedu import items


class XsydSpider(CrawlSpider):
    name = 'xsyd'
    allowed_domains = ['readnovel.com']
    start_urls = ['https://www.readnovel.com/all']

    rules = (
        Rule(LinkExtractor(allow=r'.*?all.*?', restrict_xpaths='//ul[@type="category"]/li[@data-id!="-1"]'),
             callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        cg_item = items.LdzXiaoshuoyueduLei()
        cg_item['category'] = response.xpath('//div[@class="selected"]/p/a/text()').extract_first("")
        cg_item['CGurl'] = response.url
        yield cg_item

        # 进行列表页提取
        # https://www.readnovel.com/all?pageSize=10&gender=2&catId=30020&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=1
        # https://www.readnovel.com/all?pageSize=10&gender=2&catId=30020&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=2
        # https://www.readnovel.com/all?pageSize=10&gender=2&catId=30020&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=3
        # https://www.readnovel.com/all?pageSize=10&gender=2&catId=30013&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=1
        # 请求的url
        # https://www.readnovel.com/all?pageSize=10&gender=2&catId=30013
        # 书名

        pattern = re.compile(
            '.*?catId=(\d+).*?', re.S
        )
        catId = re.findall(pattern, response.url)[0]
        req_url = 'https://www.readnovel.com/all?pageSize=10&gender=2&catId=' + catId + '&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=1'
        yield scrapy.Request(req_url, callback=self.list_table_data)

    def list_table_data(self, response):
        # print(response.url)
        lb_item = items.LdzXiaoshuoyueduItem()
        print(response.url)
        li_datas = response.xpath('//div[@class="right-book-list"]/ul/li')
        # print(len(li_datas))
        # 取中文的正则
        pattern = re.compile(
            '[^\x00-\xff]', re.S
        )
        if len(li_datas) > 1:
            for li_data in li_datas:
                # 书名
                lb_item['bookname'] = li_data.xpath('./div[@class="book-info"]/h3/a/text()').extract_first("")
                # 图片链接
                lb_item['img_url'] = response.urljoin(
                    li_data.xpath('./div[@class="book-img"]/a/img/@src').extract_first(""))
                # 作者
                lb_item['author'] = li_data.xpath('./div[@class="book-info"]/h4/a/text()').extract_first("")
                # 类别
                lb_item['category'] = li_data.xpath(
                    './div[@class="book-info"]/p[@class="tag"]/span[1]/text()').extract_first("")
                # 状态
                lb_item['State'] = li_data.xpath('./div[@class="book-info"]/p[@class="tag"]/span[2]/text()').extract_first(
                    "")
                # 字数
                lb_item['WordNumber'] = li_data.xpath(
                    './div[@class="book-info"]/p[@class="tag"]/span[3]/text()').extract_first("").replace('万', '')
                # 简介
                lb_item['introduce'] = ''.join(re.findall(pattern, li_data.xpath(
                    './div[@class="book-info"]/p[@class="intro"]/text()').extract_first(""))).replace('\u3000', '')
                # print(lb_item)
                yield lb_item

                req_url = response.urljoin(li_data.xpath('./div[@class="book-info"]/h3/a/@href').extract_first("")) + '#Catalog'
                yield scrapy.Request(req_url, callback=self.mu_lu_list)
            pattern = re.compile('.*?pageNum=(\d+)',re.S)

            current_limit = re.findall(pattern,response.url)[0]
            print(current_limit)
            next_limit = int(current_limit) + 1
            pattern1 = re.compile('pageNum=\d+',re.S)
            next_url = re.sub(pattern1,'pageNum=' + str(next_limit),response.url)
            yield scrapy.Request(next_url,callback=self.list_table_data)

    def mu_lu_list(self, response):
        # https://www.readnovel.com/chapter/9500446903583303/25615310121292841
        # https://www.readnovel.com/chapter/9500446903583303/26433039675523155
        #https://www.readnovel.com/book/22415464000832702#Catalog
        data_lis = response.xpath('//div[@class="volume-wrap"]/div[@class="volume"]/ul[@class="cf"]/li')
        zj_item = items.LdzXiaoshuoyueduZhangJie()

        for data_li in data_lis:

            # 名称
            zj_item['name'] = data_li.xpath('./a/text()').extract_first("")
            # 链接
            zj_item['zj_link'] = response.urljoin(data_li.xpath('./a/@href').extract_first(""))

            mf_vip = data_li.xpath('./em[@class="iconfont "]/text()').extract_first()
            if mf_vip:
                zj_item['mf'] = '付费'
            else:
                zj_item['mf'] = '免费'
                yield zj_item
                # a = response.urljoin(data_li.xpath('./a/@href').extract_first(""))
                yield scrapy.Request(zj_item['zj_link'],callback=self.xq_content_data)

    def xq_content_data(self,response):
        content_item = items.LdzXiaoshuoyueduContent()


        # 章节名称
        content_item['title'] = response.xpath('//h3[@class="j_chapterName"]/text()').extract_first("")
        # 书名
        content_item['bookname'] = response.xpath('//div[@class="info fl"]/a[1]/text()').extract_first("")
        # 作者
        content_item['author'] = response.xpath('//div[@class="info fl"]/a[2]/text()').extract_first("")
        # 本章字数
        content_item['WordNumber'] = response.xpath('//span[@class="j_chapterWordCut"]/text()').extract_first("")
        # 发布时间
        content_item['FaBuData'] = response.xpath('//span[@class="j_updateTime"]/text()').extract_first("")


        pattern = re.compile(
            '[^\x00-\xff]', re.S
        )
        # 内容
        content_item['content'] = ''.join(re.findall(pattern,str(response.xpath('//div[@class="read-content j_readContent"]//text()').extract())))
        # print(content_item)
        yield content_item