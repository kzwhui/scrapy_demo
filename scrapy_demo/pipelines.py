# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
from common.db_wrapper import DBWrapperFactory

class ScrapyDemoPipeline(object):
    def process_item(self, item, spider):
        print item['name'], item['url']
        return item

class MysqlPipeline(object):
    def process_item(self, item, spider):
        print spider.name
        sql = "insert into t_movies_info (c_movie_title, c_movie_url, c_create_time) values('%s', '%s', now())" % (item['name'], item['url'])
        DBWrapperFactory.get_instance('d_crawler_info').execute_sql(sql)
        return item
