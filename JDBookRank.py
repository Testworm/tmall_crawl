#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/9/5 12:54
# 京东图书 科技类书籍排行
import getSoup
from bs4 import BeautifulSoup as bs
import logging
import requests
logging.basicConfig(level=logging.INFO)


def getBook(n):
    bookstore = []
    for i in range(1, 6):
        url = 'http://book.jd.com/booktop/0-0-0.html?category=3287-0-0-0-10003-'+str(i)+'#comfort'
        print(url)
        soup = getSoup.getSoup(url)
        books = soup.select('a.p-name')
        # print(books)
        for book in books:
            title = book.get("title")
            # title = book.get_text
            # print(title)
            bookstore.append(title.strip())
    # print(bookstore)
    return bookstore


# 孔夫子搜索图书, 列出前10本: 名字+url+价格+运费+成新
def kfzSearch(books):
    for book in books:
        url = "http://search.kongfz.com/product_result/"
        querystring = {"key": book, "status": "0", "order": "1"}
        headers = {
            'origin': "https://www.kaola.com",
            'x-devtools-emulate-network-conditions-client-id': "C65543F3EED544C2D7A74FCA903B08C1",
            'x-requested-with': "XMLHttpRequest",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            'content-type': "application/x-www-form-urlencoded",
            'accept': "*/*",
            'referer': "https://www.kaola.com/search.html?zn=top&key=%25E9%259F%25A9%25E5%259B%25BD%2520MEDIHEAL%2520NMF%25E5%258F%25AF%25E8%258E%25B1%25E4%25B8%259D(%25E4%25BF%259D%25E6%25B9%25BF)%25E9%259D%25A2%25E8%2586%259C%2520%25E9%2592%2588%25E5%2589%2582%25E8%25A1%25A5%25E6%25B0%25B4%25E9%259D%25A2%25E8%2586%259C%252010%25E7%2589%2587%252F%25E7%259B%2592&searchRefer=searchbutton&oldQuery=%25E9%259F%25A9%25E5%259B%25BD%2520MEDIHEAL%2520NMF%25E5%258F%25AF%25E8%258E%25B1%25E4%25B8%259D(%25E4%25BF%259D%25E6%25B9%25BF)%25E9%259D%25A2%25E8%2586%259C%2520%25E9%2592%2588%25E5%2589%2582%25E8%25A1%25A5%25E6%25B0%25B4%25E9%259D%25A2%25E8%2586%259C%252010%25E7%2589%2587%252F%25E7%259B%2592&timestamp=1535967492452",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9",
            'cookie': "usertrack=CrH3+luM/y+fd252AwRsAg==; _ntes_nnid=1fbbbf8e551dc7c80d0f6cba21595d13,1535967047114; _ga=GA1.2.655674664.1535967047; _gid=GA1.2.825778091.1535967047; __da_ntes_utma=2525167.1045939895.1535967047.1535967047.1535967047.1; davisit=1; __da_ntes_utmb=2525167.1.10.1535967047; __da_ntes_utmz=2525167.1535967047.1.1.utmcsr%3Dwww.kaola.com%7Cutmccn%3D(prom)%7Cutmcmd%3Dprom%7Cutmpclid%3Dtag%3De1999891ea976e2f8c8de7f8c6644fdc%26__da_7cd80f92_578115ae44833c80; __da_ntes_utmfc=utmcsr%3Dwww.kaola.com%7Cutmccn%3D(prom)%7Cutmcmd%3Dprom%7Cutmpclid%3Dtag%3De1999891ea976e2f8c8de7f8c6644fdc%26__da_7cd80f92_578115ae44833c80; _jzqa=1.4471423882085310500.1535967047.1535967047.1535967047.1; _jzqc=1; _jzqy=1.1535967047.1535967047.1.jzqsr=baidu|jzqct=%E8%80%83%E6%8B%89.-; _jzqckmp=1; JSESSIONID-WKL-8IO=UX5SSqSflzogIE1bYUAPSyg%2BCwne5WQWDPx5qvq8m%2FD%2Fwt7woTf1e3MYNu0JsmtwUM41aOjoYjIbbtVJyPed9%2BKQ%2BlbZGkndQ04xT%2Ba34gz0RBHdYhZrbfvbmj7a7NLjsZHLtdtjz07e7ILQG%2Ffq2PLvOzQIHkNpWV0kaWxVX2%2BlVEPT%3A1536053447931; _klhtxd_=31; gtm_dsp_tag=__da_7cd80f92_578115ae44833c80; current_env=online; HTONLINE=fa1748ec2ebfac6f6ce1bb834b9539ea2f187970; kaola_user_key=e92a9355-5191-497f-a0fc-c976e5405b7c; NTESwebSI=3905422D2159BBC1AAF6D87BF62F489C.haitao-web-onlinejd021.v1.kaola.jd1.vpc-8081; __kaola_usertrack=20180903173025779218; _da_ntes_uid=20180903173025779218; WM_NI=Y5aAsZQWpYlE9mX3nHvAFAe%2BhIVTMwdyM1mW7ZADHw2ZFJblTqVDZGoZ4ZzeAx%2FsHdtEVD8jsInvUmJXyaPz4uAbHZUWCYFpq1NEVaqYiglXhVP14wVt6bcU6MPm4AUDVXQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed1f47d9b9ffd92d6429187a499b561ed8ba595c163a2f0a894d35fb8968e8aeb2af0fea7c3b92a9bebafa2f2529389c0baef4ffbb398d4ed44b69f8aa2e821ac979ab5d07da8a783d2f05df5868fa5cb7df2868aabe16898af9aa5d94dad86fcbbf96f83a8e194cb70b89b9aa5bb62b197a297d8678a88b782d372f8ab8f83cb5297898dbac57cb3ef82a6d56bb387a788ef54ac8aa0d2b77d96acfa83e25ff693a08eb74b979c9ab9d437e2a3; WM_TID=kJDQrHzma2yHHvg2e6NB9ISgiTqGCpI9; NTES_KAOLA_ADDRESS_CONTROL=330000|330100|330102|1; davisit=2; _qzja=1.1215927125.1535967047458.1535967047458.1535967047458.1535967075459.1535967348894.0.0.0.3.1; _qzjb=1.1535967047458.3.0.0.0; _qzjc=1; _qzjto=3.1.0; _jzqb=1.3.10.1535967047.1",
            'cache-control': "no-cache",
            'postman-token': "f27fa6f9-a5ee-5060-6457-d85ed84276fe"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
        res = response.text
        soup = bs(res, 'html.parser')
        # url = 'http://search.kongfz.com/product_result/?key='+book+'&status=0&order=1'
        # soup = getSoup.getSoup(url)
        prices = soup.find_all('div', class_='f_right red price')
        # print(prices)
        purls = soup.select('div.title a')
        print(book)
        for price in prices:
            bprice = price.text
            print(bprice)








if __name__ == '__main__':
    books = getBook(2)
    kfzSearch(books)