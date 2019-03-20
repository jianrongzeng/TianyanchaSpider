import pymysql
import scrapy
from scrapy import Spider

from TianyanchaSpider.dbutils import DBConfig
from TianyanchaSpider.items import TianyanchaspiderItem

conn = pymysql.connect(host=DBConfig.HOST_1,
                       port=DBConfig.PORT,
                       user=DBConfig.USER,
                       password=DBConfig.PASSWORD_1,
                       database=DBConfig.DATABASE_1)
cursor = conn.cursor()


def get_units():
    units = set()
    sql = 'SELECT unit FROM expert_new'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        unit = row[0]
        units.add(unit)
    # cursor.close()
    return units


def get_start_urls():
    start_urls = []
    units = get_units()
    for unit in units:
        start_url = 'https://www.tianyancha.com/search?searchType=human&key=' + ''.join(unit)
        start_urls.append(start_url)
    return start_urls


class TianyanchaSpider(Spider):
    name = 'TianyanchaSpider'
    allow_domains = ['tianyancha.com']
    start_urls = get_start_urls()

    def start_requests(self):
        # start_urls = []
        units = get_units()
        for unit in units:
            start_url = 'https://www.tianyancha.com/search?searchType=human&key=' + unit
            # start_urls.append(start_url)
            yield scrapy.Request(start_url, meta={'unit': unit, 'dont_redirect': True,
                                                  'handle_httpstatus_list': [302]})
        # return start_urls
        # for url in start_urls:
        #     yield scrapy.Request(url, meta=)

    def parse(self, response):
        shareholder = response.meta['unit']
        divs = response.xpath("//div[@class='content']//div[@class='header']")
        for div in divs:
            holding_company = div.xpath("string(.//a)").extract_first().replace("<em>", '').replace("</em>", '')
            company_status = div.xpath(".//div//text()").extract_first()

            item = TianyanchaspiderItem()
            item['shareholder'] = shareholder
            item['holding_company'] = holding_company
            item['company_status'] = company_status

            yield item


# print(cursor)
