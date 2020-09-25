#批量抓取图片

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
import re
import os
if __name__ == "__main__":

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    if not os.path.exists('./PhotoList'):
        os.mkdir('./PhotoList')

    url = 'https://www.qiushibaike.com/imgrank/page/%d/'

    for pageNum in range(1,3):
        new_url = format(url%pageNum)


        page_text = requests.get(url=new_url,headers=headers).text

        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)

        # print(img_src_list)
        for src in img_src_list:
            src = 'https:'+src
            img_data = requests.get(url=src,headers=headers).content
            img_name = src.split('/')[-1]
            imgPath = './PhotoList/'+img_name
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功!!!')

