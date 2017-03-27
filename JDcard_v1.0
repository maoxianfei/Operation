# -*- coding:utf-8 -*-
'''
 *                             _ooOoo_
 *                            o8888888o
 *                            88" . "88
 *                            (| -_- |)
 *                            O\  =  /O
 *                         ____/`---'\____
 *                       .'  \\|     |//  `.
 *                      /  \\|||  :  |||//  \
 *                     /  _||||| -:- |||||-  \
 *                     |   | \\\  -  /// |   |
 *                     | \_|  ''\---/''  |   |
 *                     \  .-\__  `-`  ___/-. /
 *                   ___`. .'  /--.--\  `. . __
 *                ."" '<  `.___\_<|>_/___.'  >'"".
 *               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *               \  \ `-.   \_ __\ /__ _/   .-` /  /
 *          ======`-.____`-.___\_____/___.-`____.-'======
 *                             `=---='
 *          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 *                     佛祖保佑        永无BUG
'''
from tkinter import *
from tkinter.ttk import *
import re
import base64
import requests
from bs4 import BeautifulSoup

def getpoints(user,pasd):
    url='http://www.wolai66.com/sign_in'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
        'Referer':'http://www.wolai66.com/sign_in'
    }
    s1=user
    s2=pasd
    wolaisession=requests.session()
    webData=wolaisession.get(url)
    # <meta content="JSnpUN9vbvGmGDFxmLbDQim6PP51jcO+Nzlkel51kps=" name="csrf-token" /></head><body class="businesses_custom_common_blue" data-current_user="false" style="margin: 0px;">
    pattern_csrf_token=re.compile('<meta content="(.*?)" name="csrf-token" /></head><body class="businesses_custom_common_blue" data-current_user="false" style="margin: 0px;">')
    csrf_token=str(pattern_csrf_token.findall(webData.text))[2:-2]
    postdata={
        'utf8':'✓',
        'authenticity_token':csrf_token,
        'from':'',
        'user_name':s1,
        'user_password':s2
    }
    # 数据请返回302重定向，重新请求网址
    url1='http://www.wolai66.com/login'
    wolaisession.post(url1,data=postdata,headers=headers)
    url='http://www.wolai66.com/user'
    loginPage=wolaisession.get(url,headers=headers)
    # print(loginPage.text)
    pattern_money=re.compile('<em>(.*?)</em></span></div></div><div class="sidebar_list"')
    money=str(pattern_money.findall(loginPage.text))[2:-2]
    if money!='':
    	return money
    else:
    	return False
      
def add_colon():
	try:
		address=[]
		with open('./cache.txt','r') as f:
		    lines=f.readlines()
		    for line in lines:
		        a=line[0:2]
		        b=line[2:4]
		        c=line[4:6]
		        d=line[6:8]
		        e=line[8:10]
		        f=line[10:12]
		        add=a+':'+b+':'+c+':'+d+':'+e+':'+f
		        address.append(add)
		with open('./cache.txt','a+') as f:
		    f.write('\n\nHere are address\n')
		    for i in address:
		        x=str(i)
		        f.write(x+'\n')
		lab_show=Label(root,text='棒棒的，请查看cache.txt文件')
		lab_show.grid(row=6,columnspan=3)
	except Exception:
		lab_show=Label(root,text='兄弟执行失败，我找不到cache.txt文件')
		lab_show.grid(row=6,columnspan=3)
def decode(s1):
   return base64.b64decode(s1)

def getinventory(url):
	webData = requests.get(url)
	soup = BeautifulSoup(webData.text, 'lxml')
	# 定位信息
	title = soup.select(
	    '#commodity_top_wrap > div.commodity_info.clear > div.commodity_info_r > div > div.tb_title > h3')
	inventory = soup.select('#fesco_pro_inventory_quantity')
	prices=soup.select('#fesco_pro_price')
	price=str(prices)
	title1 = str(title)
	inventory1 = str(inventory)
	# print(price)
	# 使用正则筛选
	pattern = re.compile('>(.*)<')#商品名称
	title2 = pattern.findall(title1)
	price=pattern.findall(price)
	inventory2 = pattern.findall(inventory1)#商品库存
	title2=str(title2)[2:-2]
	inventory2=str(inventory2)[2:-2]
	price=str(price)[2:-2]
	cache='名称：%s元电子卡,实际价格%s元，数量：%s'%(title2,price,inventory2)
	return cache
def check():
    urls = {
        '300': 'http://www.wolai66.com/commodity?code=10172061270',
        '100': 'http://www.wolai66.com/commodity?code=10133563152',
        '200': 'http://www.wolai66.com/commodity?code=10152135133',
        '500': 'http://www.wolai66.com/commodity?code=10124884175',
        '107': 'http://www.wolai66.com/commodity?code=11066517741',
        '1070': 'http://www.wolai66.com/commodity?code=10160124842',
        '214': 'http://www.wolai66.com/commodity?code=11063863053',
        '321': 'http://www.wolai66.com/commodity?code=11065010573',

    }
    caches=[]
    for url in urls:
        cache=getinventory(urls[url])
        caches.append(cache)

    return str(caches) 
def opt_string(string):
	rstr="\',"
	valid=re.sub(rstr,'\n',string)
	rstr
	return valid

def get_jdcard():
	inventory_info=check()
	f=Toplevel(root)
	f.title("库存查询结果")
	lf=Label(f,text=opt_string(inventory_info))
	# print(opt_string(inventory_info))
	lf.pack()

def get_infoPerson():
	# global root
	# global lab_show
	#用户体验问题
	
	user=eny_user.get()
	pasd=eny_pasd.get()
	lab_show['text']='别玩我，请输入用户名或密码！'
	if user=='' or pasd=='':
		lab_show['text']='别玩我，请输入用户名或密码！'
		return False
	money=getpoints(user,pasd)
	if  money:
		lab_show['text']='您的T币余额为：'+str(money)
	else:
		lab_show['text']='查询失败！用户名或密码错误'
root=Tk()
root.wm_title('JD-E card query')
root.geometry("500x400+400+200")
# root.resizable(width = False, height = False)
style='Helvetica -20'
#Lable
lab_show=Label(root,text='结果',)
lab_show.grid(row=1,column=3,rowspan=2)
lab_info1=Label(root,text='输入账号密码查询T币').grid(row=0,column=0,columnspan=2)
# lab_info1_right=Label(root,text='查询结果:(别急啊，结果将在下方显示)').grid(row=0,column=3,columnspan=5)
lab_user=Label(root,text='Username:').grid(row=1,column=0)
lab_pasd=Label(root,text='Password:').grid(row=2,column=0)
#Button
but_getinfo=Button(root,text='查询T币余额',command=get_infoPerson,width=15)
but_getinfo.grid(row=3,column=1,columnspan=2)
but_info2=Button(root,text='查询京东E卡库存',command=get_jdcard,width=15)
# but_info2.bind("<Button-1>",get_jdcard)
but_info2.grid(row=4,column=1)
but_addcolon=Button(root,text='增加冒号',command=add_colon,width=15)
# but_addcolon.configure(width=10)
but_addcolon.grid(row=5,column=1)
#Entry
eny_user=Entry(root)
eny_pasd=Entry(root,show='*')
eny_user.grid(row=1,column=1)
eny_pasd.grid(row=2,column=1)
root.mainloop()




		
	




