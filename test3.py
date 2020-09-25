#豆瓣ajax请求

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
import json
if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list'

    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    response = requests.get(url=url,params=param,headers=headers)

    list_data = response.json()

    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('over!!!!!')

