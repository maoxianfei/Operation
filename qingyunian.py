#coding:utf-8
import requests
import bs4
import chardet
import re

num = 93
while num<=886:
    re_title=re.compile('<h1>.*?</h1>')
    re_text=re.compile('<p>&nbsp;&nbsp;&nbsp;&nbsp;.*?</p>')
    url='http://www.qingyunian.net/%d.html'%num
    html=requests.get(url)
    # detect the real encode
    # print(chardet.detect(html.content)['encoding'])
    html.encoding='utf-8'
    t=('\n').join(re_text.findall(html.text))
    title=('\n').join(re_title.findall(html.text))
    soup=bs4.BeautifulSoup(t,'lxml')
    con=soup.get_text()
    with open('./庆余年.txt','a+',encoding='utf-8') as f:
        f.write('    '+str(title)[4:-5]+'\n')
        f.write(con)
    num=num+1
    print(num)







