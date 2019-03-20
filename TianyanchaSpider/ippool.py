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


class cookie():
    def process_request(self, request, spider):
        request.cookies = {
            "TYCID": "ff55de60192611e9b304afa27bfa6016",
            "undefined": 'ff55de60192611e9b304afa27bfa6016',
            "ssuid": '4672923470',
            "_ga": "GA1.2.540984583.1547599098",
            "Hm_lvt_e92c8d65d92d534b0fc290df538b4758": "1552549219,1552549889,1552618937,1552618981",
            "aliyungf_tc": "AQAAAPrGDBT5mwsAQoP53mKEdK+son5v",
            "csrfToken": '5M_gdBSlCquVu--i_sIO801R',
            "_gid": 'GA1.2.499897527.1553002672',
            "refresh_page": "null",
            "RTYCID": "3a45acdaa9654d9c97625968c892cbd4",
            "CT_TYCID": '5e5e0bc98e8a4ab4a2a967b208d010c2',
            'bannerFlag': 'true',
            'cloud_token': '68b07db89dc84d1b85bf0ca0246e20b2',
            '_gat_gtag_UA_123487620_1': '1',
            '__insp_wid': '677961980',
            '__insp_nv': 'true',
            '__insp_targlpu': 'aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vbG9naW4%2FZnJvbT1odHRwcyUzQSUyRiUyRnd3dy50aWFueWFuY2hhLmNvbSUyRnNlYXJjaCUzRnNlYXJjaFR5cGUlM0RodW1hbiUyNmtleSUzRCUyNUU0JTI1QjglMjU4QSUyNUU2JTI1QjUlMjVCNyUyNUU2JTI1OTYlMjU5NyUyNUU4JTI1QjElMjVBMSUyNUU0JTI1QkYlMjVBMSUyNUU2JTI1ODElMjVBRiUyNUU3JTI1QTclMjU5MSUyNUU2JTI1OEElMjU4MCUyNUU2JTI1OUMlMjU4OSUyNUU5JTI1OTklMjU5MCUyNUU1JTI1ODUlMjVBQyUyNUU1JTI1OEYlMjVCOA%3D%3D',
            '__insp_targlpt': '5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D',
            '__insp_norec_sess': 'true',
            'tyc-user-info': '%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E6%2585%2595%25E5%25AE%25B9%25E5%258D%259A%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25224%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzI2MDEzNTEwMSIsImlhdCI6MTU1MzA0MjM1OSwiZXhwIjoxNTY4NTk0MzU5fQ.vxrHrr1E9-xu0wz7WeVQsGN6Xww5uHCuy80AaZHfvj1UIC8gz6ElgpkZ3yMYFEEV8TXsGTskTqVf7vkIErgMzw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213260135101%2522%257D',
            'auth_token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzI2MDEzNTEwMSIsImlhdCI6MTU1MzA0MjM1OSwiZXhwIjoxNTY4NTk0MzU5fQ.vxrHrr1E9-xu0wz7WeVQsGN6Xww5uHCuy80AaZHfvj1UIC8gz6ElgpkZ3yMYFEEV8TXsGTskTqVf7vkIErgMzw',
            '__insp_slim': '1553042361111',

        }
