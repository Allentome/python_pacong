#kfc

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
import json
if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    param = {
        'cname': '',
        'pid': '',
        'keyword': '深圳',
        'pageIndex': '2',
        'pageSize': '10'
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    response = requests.post(url=url,data=param,headers=headers)

    list_data = response.json()

    fp = open('./kfcct.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('over!!!!!')

