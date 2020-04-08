# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class WangyiPipeline:
    def __init__(self):
        self.file = open('job.json','w')

    def process_item(self, item, spider):
        item = dict(item)     # 选择器对象强转dict，只适用于 scrapy 框架
        str_data = json.dumps(item,ensure_ascii=False) + ',\n'
        self.file.write(str_data)

    def __del__(self):
        self.file.close()
