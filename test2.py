#百度翻译

#UA伪装,UA: User-Agent(请求载体到身份标识)
import requests
import json
if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    word = input('enter a word:')
    data = {
        'kw':word
    }

    response = requests.post(url=post_url,data=data,headers=headers)

    dic_obj = response.json()

    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)

    print('over!!!')
