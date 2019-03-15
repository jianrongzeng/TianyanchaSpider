# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from TianyanchaSpider.spiders.TianyanchaSpider import cursor, conn


class TianyanchaspiderPipeline(object):
    def process_item(self, item, spider):
        keys = item.keys()
        values = tuple(item.values())
        field = ','.join(keys)
        temp = ','.join(['%s'] * len(keys))
        sql = 'insert into t_unit_relation (%s) values (%s)' % (field, temp)
        cursor.execute(sql, values)
        conn.commit()
        return item
