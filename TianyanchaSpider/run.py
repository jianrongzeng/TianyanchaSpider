from scrapy import cmdline

cmdline.execute("scrapy crawl TianyanchaSpider -o trs.json".split())
