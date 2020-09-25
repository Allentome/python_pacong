#爬取搜狗首页的页面数据，存储成html

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
if __name__ == "__main__":

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    #指定url
    url = 'https://www.sogou.com/web'

    kw = input('enter a word:')
    param = {
        'query':kw
    }

    requests = requests.get(url=url,params=param,headers=headers)

    page_text = requests.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName,'保存成功!!!')
