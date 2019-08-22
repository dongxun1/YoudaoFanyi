import execjs
import requests
headers = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,eu;q=0.7,eo;q=0.6',
            'Connection':'keep-alive',
            'Content-Length':'242',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'OUTFOX_SEARCH_USER_ID=118452452@10.169.0.82; OUTFOX_SEARCH_USER_ID_NCOO=8640035.704335434; UM_distinctid=16b46fe638ea5-007c21e0c9cd04-e353165-100200-16b46fe638f1ea; _ntes_nnid=48895a5dcd4db1caae23c7a45c5a2b28,1560563984307; _ga=GA1.2.1186284290.1563375042; JSESSIONID=aaahTw8_Y4Q8K8LkZkTYw; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcsQKvyTa-b0hdFllTYw; ___rl__test__cookies=1566273541573',
            'Host':'fanyi.youdao.com',
            'Origin':'http://fanyi.youdao.com',
            'Referer':'http://fanyi.youdao.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
        }


def encrpt(e):
    with open('youdao.js', 'r', encoding='utf-8') as fp:
        line = fp.read()

    ctx = execjs.compile(line)
    result = ctx.call('params_all', e) # 调用js文件中的函数 。
    return result


if __name__ == '__main__':
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = encrpt("world")  # 输入单词 翻译。
    resp = requests.post(url, data, headers=headers)

    print(resp.text)





