#爬取搜狗首页的页面数据
import requests
if __name__ == "__main__":
    #指定url
    url = 'https://www.bilibili.com/'


    requests = requests.get(url=url)

    page_text = requests.text
    print(page_text)

    # with open('./bilibili.html','w',encoding='utf-8') as fp:
    #     fp.write(page_text)
    print('爬取数据结束')
