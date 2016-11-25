# Tdevice study  
###d.press("")
hard_key=['home','back','left','right','up','down','volume_up','volume_down','volume_mute','power']  
appkey=['search','enter','delete'(or del),'recent'(recent apps),'camera','Center','menu']  
d.wakeup() d.screen.on() d.sleep() d.screenoff()  
###open app
d.start_activity('package_name','service_name')  
###judge
d(text='name').wait.exists(timeout=3000)  



