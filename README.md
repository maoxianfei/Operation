# Tdevice study  
###按键事件
d.press("")
hard_key=['home','back','left','right','up','down','volume_up','volume_down','volume_mute','power']  
appkey=['search','enter','delete'(or del),'recent'(recent apps),'camera','Center','menu']  
d.wakeup() d.screen.on() d.sleep() d.screenoff()  

###模拟用户操作
####click(x,y)
.click.wait(timeout=3000)点击等待出现，超时
.click.bottomright()点击对象右下角
.click.topleft()点击对象左上角
####long_click(x,y)  
.long_click.bottomright()长按对象右下角
.long_click.topleft()长按对象左上角
####drag(startX,startY,endX,endY,steps)  
####swipe('directioin',steps=10) direction滑动方向:up,down,right,left
dump(filename) save_path:/data/local/tmp
####手势操作
d.pinch.In(perent=100,steps=10)
d.pinch.Out(percent=100,steps=10)
###输入
set_text(text)输入文本
clear_text()清空文本
###打开操作
d.open(action) action:notification,quick_settings
d.start_activity('package_name','service_name')  
###等待窗口出现
d(text='name').wait.exists(timeout=3000)
###获取设备信息
get_device_serial() 设备ID  
get_current_packagename() 当前包名  
get_device_brand() 商标名
get_device_name() 设备名
get_device_manufacturer() 厂商名称
get_device_model() 设备模块
get_current_lang() 当前语言
get_data_connected_status() 数据服务连接状态
get_data_service_state() 当前数据服务类型（2G/3G/LTE/unknown）
get_call_state() 当前通话状态
get_incomingcall_number() 来电号码
get_qcom_log() 日志
get_cpuinfo() CPU
get_meninfo() 内存
###获取对象属性
child()
sibling()
###判断出现与消失
wait(action,timeout=10000) action=idle等待应用程序处于空闲状态
wait(action,timeout=1000,package_name=None) action=upgrade等待窗口内容更新事件
>>>案例
d(text='Incoming call').wait.exists(timeout=1000)
d(text='Incoming call').wait.gone(timeout=1000)
###选择器
####文本类
text 文本
textContains 文本包含
textMatches 文本正则
textStarsWith 文本开始字符
####描述类
descriptioin 描述
descriptionContains 描述包含
descriptioinMatches 描述正则
descriptioinStarsWith 描述开始字符
####包类
packageName
packageNameMatches
####索引
index 
instance
####资源
resourceld 资源Id
resourceldMatches 资源id正则
###特有属性
checked 选择属性
clickable 点击属性
enabled 
focusable 焦点属性
focused 当前焦点属性
longClickable长按属性
scrollable 滚动属性
selected 选择属性
###获取对象属性
child() 获取子类
sibling() 获取兄弟类
getChildCount() 子类数量
getClassName() 属性的类名
getContentDescription() 属性的描述文本
getPackageName() 属性的包名文本
get_text() 文本属性中的文本
###属性判断(检查是否为true)
isCheckable() 
isChecked()
isClickable() 
isEnabled()
isFocusable()
isFocused()
isLongClickable()
isScrollable()
isSelected()
