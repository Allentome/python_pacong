#批量抓取小说

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/lunyu.html'
    page_text = requests.get(url=url,headers=headers).text
    #在首页解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到对象中
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页到的url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./lunyu.text','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url,headers=headers).text
        # 解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        # 解析到了章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功')