# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class Pachongday12Pipeline(object):
    def process_item(self, item, spider):
        return item

class MEIJU(object):
    def process_item(self, item, spider):
        # fp = open('Meiju.txt','a',encoding='utf-8')
        with open("Meiju.txt",'a',encoding='utf-8')as fp:
            # json.dump(dict(item),fp,ensure_ascii=False)
            fp.write("名称：" + dict(item)['name'] + '\n')
            fp.write("导演：" + dict(item)['dy'] + '\n')
            fp.write("主演：" + dict(item)['zy'] + '\n')
            fp.write("类型：" + dict(item)['type'] + '\n')
            fp.write("排名：" + dict(item)['num'] + '\n')
            fp.write("电视台："+dict(item)['tv']+'\n')
            fp.write("路径："+ dict(item)['url']+'\n')

            fp.write('\n')
        return item
