import random
import requests

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class ippool(HttpProxyMiddleware):

    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        # proxy = requests.get("http://127.0.0.1:5010/get_all/").json()

        proxy = requests.get("http://127.0.0.1:5010/get_all/").json()
        ip = random.choice(proxy)
        print("当前使用IP是：" + ip)
        request.meta["proxy"] = "https://" + ip