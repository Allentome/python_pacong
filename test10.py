#批量抓取图片(循环网页)

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
from lxml import etree
import os
if __name__ == "__main__":

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    if not os.path.exists('./meinv'):
        os.mkdir('./meinv')

    old_url = 'http://www.netbian.com/meinv/index_%d.htm'

    for pageNum in range(3,5):
        url = format(old_url%pageNum)
        page_text = requests.get(url=url, headers=headers).text

        # 数据解析：src的属性值 alt属性
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="list"]/ul/li')
        if not os.path.exists('./meinv'):
            os.mkdir('./meinv')
        for li in li_list:
            try:
                # img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
                img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
                img_name = img_name.encode('iso-8859-1').decode('gbk')
                img_page = 'http://www.netbian.com/' + li.xpath('./a/@href')[0]
                img_page_text = requests.get(url=img_page, headers=headers).text
                tree = etree.HTML(img_page_text)
                img_big_src = tree.xpath('//div[@class="pic"]/p/a/img/@src')[0]

                # print(img_big_src)
                # print(img_name,img_src)
                img_data = requests.get(url=img_big_src, headers=headers).content
                img_path = 'meinv/' + img_name
                with open(img_path, 'wb') as fp:
                    fp.write(img_data)
                    print(img_name, '下载成功')

            except IndexError as e:
                print("IndexError Details : " + str(e))
                pass

