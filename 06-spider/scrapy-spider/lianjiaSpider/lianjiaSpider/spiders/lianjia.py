
import scrapy

from lianjiaSpider.items import LianjiaHouseItem
MAX_PAGE = 101

class LianJiaSpider(scrapy.Spider):
    """爬取链家的 信息"""
    name = 'lianjia'

    # 允许访问的域名，爬取的域名
    allowed_domains = ['lianjia.com']

    """
    北京(bj) 上海(sh) 深圳(sz) 成都(cd) 重庆(cq) 长沙(cs) 大连(dl) 德阳(dy) 广州(gz) 杭州(hz) 
    海口(hk) 合肥(hf) 济南(jn) 昆明(km) 南京(nj) 青岛(qd) 苏州(sz) 石家庄(sjz) 沈阳(sy) 天津(tj)
    太原(ty) 武汉(wh) 厦门(xm) 西安(xa) 郑州(zz)
    """
    # 24 个 目标 城市
    cities = [
        'bj', 'sh', 'sz', 'cd', 'cq', 'cs', 'dl', 'dy', 'gz',
        'hz', 'hk', 'hf', 'jn', 'km', 'nj', 'qd', 'sz', 'sjz',
        'sy', 'tj', 'ty', 'wh', 'xm', 'xa', 'zz',
    ]

    # 测试城市
    # cities = ['cd']

    # 二手房 房源
    ershoufang_url = 'https://{city}.lianjia.com/ershoufang/pg{page}/'
    # 二手房，成交
    chenjiao_url = 'https://{city}.lianjia.com/chengjiao/pg{page}/'
    # 新房
    loupan_url = 'https://{city}.fang.lianjia.com/loupan/pg{page}'
    # 租房
    zufang_url = 'https://{city}.lianjia.com/zufang/pg{page}'

    def start_requests(self):
        for city in self.cities:
            # 二手房
            yield scrapy.Request(self.ershoufang_url.format(city=city, page=1),
                                 callback=self.parse_ershoufang)
            # 二手房成交
            yield scrapy.Request(self.chenjiao_url.format(city=city, page=1),
                                 callback=self.parse_chenjiao)
            # 新房
            yield scrapy.Request(self.loupan_url.format(city=city, page=1),
                                 callback=self.loupan)
            # 租房
            yield scrapy.Request(self.zufang_url.format(city=city, page=1),
                                 callback=self.parse_zufang)

    def parse_ershoufang(self, response):
        """二手房 房源"""
        sel = scrapy.Selector(response)

        lianjia_item = LianjiaHouseItem()
        # url  例：https://cd.lianjia.com/ershoufang/pg1/
        url = response.url
        # # 新房还是二手房
        lianjia_item['type'] = url.split('/')[3]
        # 城市
        city = url.split('/')[2].split('.')[0]
        # 总的页码

        lianjia_item['city'] = city

        lis = sel.xpath('/html/body/div[4]/div[1]/ul/li[@class="clear"]')
        for li in lis:
            try:
                # 房屋编号
                lianjia_item['house_code'] = li.xpath('./a/@data-housecode').extract()[0]
                if li.xpath('./a/img/@src'):
                    # 图片 链接
                    lianjia_item['img_src'] = li.xpath('./a/img/@src').extract()[0]
                # 房屋标题
                lianjia_item['title'] = li.xpath('./div/div/a/text()').extract()[0]
                # 房屋地址
                lianjia_item['address'] = li.xpath('./div/div[2]/div/a/text()').extract()[0]
                #房屋信息
                info = li.xpath('./div/div[2]/div/text()').extract()[0]
                lianjia_item['info'] = [i.strip() for i in info.split('|')[1:]]
                # 楼盘情况 高层底层  建楼时间
                flood = li.xpath('.//div[@class="flood"]/div/text()').extract()[0]
                lianjia_item['flood'] = flood.replace(' ', '').replace('-', '')
                # 关注者情况 发布时间
                follower = li.xpath('.//div[@class="followInfo"]/text()').extract()[0]
                lianjia_item['follower'] = follower.replace(' ', '').split('/')
                # 地理优势 房屋优势
                lianjia_item['tag'] = li.xpath('.//div[@class="tag"]/span/text()').extract()[0]
                # 总价 单位：万
                lianjia_item['totalprice'] = li.xpath('.//div[@class="totalPrice"]/span/text()').extract()[0] + ' 万'
                # 单价 每平米的价钱
                lianjia_item['unitprice'] = li.xpath('.//div[@class="unitPrice"]/span/text()').extract()[0]
            except:
                continue

            yield lianjia_item

        # 下一页
        page = int(url.split('/')[4].replace('pg', ''))
        page += 1
        if page < MAX_PAGE:
            yield scrapy.Request(self.ershoufang_url.format(city=city, page=page),
                             callback=self.parse_ershoufang)

    def parse_chenjiao(self, response):
        """二手房成交"""
        sel = scrapy.Selector(response)

        lianjia_item = LianjiaHouseItem()
        # url  例：https://cd.lianjia.com/ershoufang/pg1/
        url = response.url
        # # 新房还是二手房 等
        lianjia_item['type'] = url.split('/')[3]
        # 城市
        city = url.split('/')[2].split('.')[0]

        lianjia_item['city'] = city

        lis = sel.xpath('//ul[@class="listContent"]/li')
        for li in lis:
            try:
                # 标题
                title = li.xpath('.//div[@class="title"]/a/text()').extract()[0]
                lianjia_item['title'] = title
                lianjia_item['house_code'] = title
                # 房屋编号  从 title 中获取 <a href="https://cd.lianjia.com/chengjiao/106101178880.html" target="_blank">中铁丽景书香 1室0厅 36.97平米</a>
                # 有的房屋没有编号，暂时不用
                # href = li.xpath('./@data-project-name').extract()
                # if href:
                #     lianjia_item['house_code'] = href[0].split('/')[-1].split('.')[0]
                # else:
                #     lianjia_item['house_code'] = title
               # 图片
                lianjia_item['img_src'] = li.xpath('.//img[@class="lj-lazy"]/@src').extract()[0]
                # 楼盘情况 高层底层  建楼时间
                lianjia_item['flood'] = li.xpath('.//div[@class="positionInfo"]/text()').extract()[0]
                # 房屋年限，已近购买满几年
                lianjia_item['house_year'] = li.xpath('.//span[@class="dealHouseTxt"]/span/text()').extract()[0]
                # 地理优势 房屋优势
                tag = li.xpath('.//div[@class="houseInfo"]/text()').extract()[0]
                lianjia_item['tag'] = tag.replace('\xa0','').replace('|', '')
                # 挂牌价格
                lianjia_item['origin_price'] = li.xpath('.//span[@class="dealCycleTxt"]/span[1]/text()').extract()[0]
                # 成交周期
                lianjia_item['trade_time'] = li.xpath('.//span[@class="dealCycleTxt"]/span[2]/text()').extract()[0]

                # 交易价格 暂无
            except:
                continue

            yield lianjia_item

        # 下一页
        page = int(url.split('/')[4].replace('pg', ''))
        page += 1
        if page < MAX_PAGE:
            yield scrapy.Request(self.chenjiao_url.format(city=city, page=page),
                             callback=self.parse_chenjiao)

    def loupan(self, response):
        """新房"""
        sel = scrapy.Selector(response)

        lianjia_item = LianjiaHouseItem()
        # url  例：https://cd.lianjia.com/ershoufang/pg1/
        url = response.url
        # # 新房还是二手房 等
        lianjia_item['type'] = url.split('/')[3]
        # 城市
        city = url.split('/')[2].split('.')[0]

        lianjia_item['city'] = city

        lis = sel.xpath('//li[@class="resblock-list"]')
        for li in lis:
            try:
                # 房屋编号
                lianjia_item['house_code'] = li.xpath('./@data-project-name').extract()[0]
                # 标题
                lianjia_item['title'] = li.xpath('.//a[@class="name"]/text()').extract()[0]
                # 图片
                lianjia_item['img_src'] = li.xpath('.//a/img/@src').extract()[0]
                # 在售，下期开售
                lianjia_item['status'] = li.xpath('.//span[@class="sale-status"]/text()').extract()[0]
                # 房屋类型  住宅 别墅
                lianjia_item['house_kind'] = li.xpath('.//span[@class="resblock-type"]/text()').extract()[0]
                # 房屋建面
                lianjia_item['house_area'] = li.xpath('.//div[@class="resblock-area"]/span/text()').extract()[0]
                # 均价
                number = li.xpath('.//span[@class="number"]/text()').extract()[0]
                desc = li.xpath('.//span[@class="desc"]/text()').extract()[0].replace('\xa0', '')
                lianjia_item['unitprice'] = number + ' ' + desc
                # 总价
                lianjia_item['totalprice'] = li.xpath('.//div[@class="second"]/text()').extract()[0]
            except:
                continue

            yield lianjia_item

        # 下一页
        page = int(url.split('/')[4].replace('pg', ''))
        page += 1
        if page < MAX_PAGE:
            yield scrapy.Request(self.loupan_url.format(city=city, page=page),
                                 callback=self.loupan)

    def parse_zufang(self, response):
        """租房"""
        sel = scrapy.Selector(response)

        lianjia_item = LianjiaHouseItem()
        # url  例：https://cd.lianjia.com/ershoufang/pg1/
        url = response.url
        # # 新房还是二手房等
        lianjia_item['type'] = url.split('/')[3]
        # 城市
        city = url.split('/')[2].split('.')[0]
        total_page = ''
        lianjia_item['city'] = city

        lis = sel.xpath('//ul[@class="house-lst"]/li')
        for li in lis:
            try:
                # 房屋编号
                lianjia_item['house_code'] = li.xpath('./@data-housecode').extract()[0]
                if li.xpath('.//div[@class="pic-panel"]/a/img/@src'):
                    # 图片 链接
                    lianjia_item['img_src'] = li.xpath('.//div[@class="pic-panel"]/a/img/@src').extract()[0]
                # 房屋标题
                lianjia_item['title'] = li.xpath('.//div[@class="info-panel"]/h2/a/text()').extract()[0]
                # 房屋地址
                info = li.xpath('.//div[@class="where"]//text()').extract()
                address = info[0].replace('\xa0','')
                hous_info = ''.join(info[1:]).replace('\xa0',' ')
                lianjia_item['address'] = address
                # 房屋信息
                lianjia_item['info'] = hous_info
                # 租楼情况 高层底层  建楼时间 例：攀成钢租房/低楼层(共33层)/2009年建塔楼
                flood = li.xpath('.//div[@class="con"]//text()').extract()
                lianjia_item['flood'] = ''.join(flood)
                # 关注者情况
                follower = li.xpath('.//div[@class="col-2"]//text()').extract()
                lianjia_item['follower'] = ''.join(follower)
                # 地理优势 房屋优势
                tag = li.xpath('.//div[@class="view-label left"]//text()').extract()
                lianjia_item['tag'] = '#'.join(tag)
                # 单价
                price = li.xpath('.//div[@class="price"]//text()').extract()
                lianjia_item['unitprice'] = ' '.join(price)
            except:
                continue

            yield lianjia_item

        # 下一页
        page = int(url.split('/')[4].replace('pg', ''))
        page += 1
        if page < MAX_PAGE:
            yield scrapy.Request(self.zufang_url.format(city=city, page=page),
                                 callback=self.parse_zufang)
