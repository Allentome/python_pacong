#抓取图片

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
if __name__ == "__main__":
    url = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3464254433,3292642093&fm=26&gp=0.jpg'

    img_data = requests.get(url=url).content

    with open('./photo.jpg','wb') as fp:
        fp.write(img_data)


