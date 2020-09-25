#批量抓取58信息

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
from lxml import etree
if __name__ == "__main__":

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    url = 'https://sz.58.com/chuzu/?PGTID=0d000000-0000-00d5-614d-fdbadef6bf5d&ClickID=1'
    fp = open('./58.text','w',encoding='utf-8')
    page_text = requests.get(url=url,headers=headers).text

    # 数据解析
    tree = etree.HTML(page_text)
    # 存储的就是li标签对象
    li_list = tree.xpath('//ul[@class="house-list"]/li')
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        price = li.xpath('./div[3]/div[@class="money"]/b/text()')[0]
        fp.write(title+price)
        print(title+price)