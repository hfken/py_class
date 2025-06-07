import requests
url='https://www.cumt.edu.cn'
headers={'user-agent':'Mozilla/5.0'}
try:
    r=requests.get(url,headers=headers,timeout=10)
    with open(r'./request/out.txt','w',encoding='utf-8') as f:
        f.write(r.text)
except:
    print('bu')