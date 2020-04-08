import scrapy
from wangyi.items import WangyiItem

class JobSpider(scrapy.Spider):
    name = 'job'
    # 2. check the domain , if different should fix
    allowed_domains = ['163.com']
    # 1. check the start url
    start_urls = ['https://hr.163.com/position/list.do']
    # 网页中的Xpath无法正确定位
    def parse(self, response):
        # 1. 获取节点数据
        node_list = response.xpath('//tbody//tr')
        # print(node_list)  # 发现列表中存在无用对象，下一步解析时需剔除
        for num,node in enumerate(node_list):
            # print(num,node)  # 发现序号为奇数的对象无用，下面开始判断
            if num %2 == 0:
                item = WangyiItem()
                item['name'] = node.xpath('./td[1]/a/text()').extract_first()
                item['type'] = node.xpath('./td[4]/text()').extract_first()
                item['city'] = node.xpath('./td[5]/text()').extract_first()
                item['category'] = node.xpath('./td[3]/text()').extract_first()
                item['num'] = node.xpath('./td[6]/text()').extract_first().strip()  # strip() 语法需和 extract 方法连用
                item['date'] = node.xpath('./td[7]/text()').extract_first()
                yield item

        #  2. 翻页操作
        part_url = response.xpath('//a[contains(text(),">")]/@href').extract_first()  # 提取下一页的部分网址, [contains(text(),"搜索内容"]
        if part_url != 'javascript:void(0)':
        # next_url = 'https://hr.163.com/position/list.do' + part_url   # 构造完整网址
            next_url = response.urljoin(part_url)   # scrapy 库链接自拼接
        # print(next_url)
        # 生成请求，返给引擎
            yield scrapy.Request(
                next_url,
                callback=self.parse  # 可不写，默认为 parse 方法
            )

