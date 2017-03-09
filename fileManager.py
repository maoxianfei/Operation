# -*- coding: UTF-8 -*-
"""
This module implements common File manager. Presently there is one class FileManager.
"""
import re
import sys
from common import Common

class FileManager(Common):
    '''FileManager object, Provide File manager functions for all scripts.'''
    def __init__(self, device, logName):
        '''
        Create a instance of FileManager. Must input the parameters:Device instance,logger instance
        device
          Device instance
        logName
          logger instance
        '''
        #Common.__init__(self, device,logName)
        super(FileManager,self).__init__(device,logName)
        self._ssid = None
    
    def backToMainScreen(self):
        '''
        Back to main screen in fileManager .
        
        return True/False
        '''        
        for i in range(10):
            if not self._device(resourceIdMatches='com.jrdcom.filemanager:id/phone_used_info_tv').wait.exists(timeout=2000):
                self._device.press.back()
            else:
                break
        if self._device(resourceIdMatches='com.jrdcom.filemanager:id/phone_used_info_tv').wait.exists(timeout=10000):
            self._logger.debug('Now in Main screen in fileManager .')
            return True
        else:
            self._logger.debug('Fail to back to main screen in fileManger.')
            return False
    
    def checkAPP(self,appName):
        "Check wether app exists"
        app_name = appName.split(".")[0]
        self._device.press.home()
        if self._device(description="Apps").wait.exists:
            self._device(description="Apps").click()
            if self._device(scrollable=True).scroll.to(text=app_name):
                self._logger.debug("Find %s"%app_name)
                return True
            else:
                self._logger.debug("%s is not existed"%app_name)
                return False
        else:
            self._logger.debug("Return home interface failure")
            return False
    
    def checkAudio(self,AudioName):
        "Check appointed audio"
        self._device(scrollable=True).scroll.to(text=AudioName)
        if self._device(text=AudioName).wait.exists(timeout=2000):
            self._logger.debug("Have found %s"%AudioName)
        else:
            self._logger.debug("Cannot found %s"%AudioName)
            return False
        self._device(text=AudioName).click()
        #if self._device(text="Open with").wait.exists(timeout=2000):
        #    self._logger.debug("Will use Gallery to open picture %s"%pitcureName)
        #else:
        #    self._logger.debug("Can not find Will Open with")
        #    return False
        self._logger.debug("Will use Google Play Music to open music %s"%AudioName)
        if self._device(text="Google Play Music",resourceId="android:id/text1").wait.exists(timeout=2000):
            self._logger.debug("Find Google Play Music APP")
            self._device(text="Google Play Music",resourceId="android:id/text1").click()
        elif self._device(textContains="Open with",resourceId="android:id/title").wait.exists(timeout=2000):
            self._logger.debug("Find Google Play Music APP")
        else:
            self._logger.debug("Can not find Google Play Music APP")
            return False
        if self._device(textMatches="(?i:Just once)",enabled=True).wait.exists(timeout=2000):
            self._device(textMatches="(?i:Just once)",enabled=True).click()
            while True:
                if self._device(textMatches="(?i:Allow)").wait.exists(timeout=1000):
                    self._device(textMatches="(?i:Allow)").click()
                    continue
                else:
                    break
        else:
            self._logger.debug("Just once is not enabled or text of Just once is wrong or click Google Play Music failure")
            return False
        for i in range(30):
            if self._device(resourceId="com.google.android.music:id/progress").exists:
                self._logger.debug("Use Google Play Music to open %s successfully"%AudioName)
                self._device.press.back()
                return True
            else:
                self._device.delay(1)
                i+=1
        else:
            self._logger.debug("Fail to use Google Play Music to open %s"%AudioName)
            return  False
    
    def checkHideFile(self,nameFolder,storageType):
        if not self._device(resourceIdMatches='com.jrdcom.filemanager:id/phone_(size|used_info_tv)').wait.exists(timeout=2000):
            self.backToHome()
        self.clickAppIconInAppList('Files')
        if self._device(resourceId='com.jrdcom.filemanager:id/phone_name').wait.exists(timeout=2000):
            if storageType == 'Phone':
                self._device(resourceId='com.jrdcom.filemanager:id/phone_name').click()
            elif self._device(resourceId='com.jrdcom.filemanager:id/sd_name').wait.exists(timeout=2000):
                self._device(text='SD').click()
            else:
                self._logger.debug('The phone have not SD card')
                return False
        if self._device(resourceId='com.jrdcom.filemanager:id/more_btn').wait.exists(timeout=2000):
            self._device(resourceId='com.jrdcom.filemanager:id/more_btn').click()
        if self._device(resourceId='com.jrdcom.filemanager:id/hide_item').wait.exists(timeout=2000):
            self._device(text='Hide hidden files').click()
        if not self.judgeExistsByManual(nameFolder):
            self._logger.debug('the hide file have been hiden sccessful')
            return True
        else:
            self._logger.debug('the hide file have been hiden failed')
            return False
        if self._device(resourceId='com.jrdcom.filemanager:id/show_item').wait.exists(timeout=2000):
            self._device(text='Show hidden files').click()
        if self.judgeExistsByManual(nameFolder):
            self._logger.debug('the hide file :%s have been disply'%nameFolder)
            return True
        else:
            self._logger.debug('the hide file :%s have been disply failed'%nameFolder)
            return False
    
    def checkPicture(self,pitcureName):
        "Check appointed picture"
        if self._device(text=pitcureName).wait.exists(timeout=2000):
            self._logger.debug("Have found %s"%pitcureName)
        else:
            self._logger.debug("Cannot found %s"%pitcureName)
            return False
        self._device(text=pitcureName).click()
        #if self._device(text="Open with").wait.exists(timeout=2000):
        #    self._logger.debug("Will use Gallery to open picture %s"%pitcureName)
        #else:
        #    self._logger.debug("Can not find Will Open with")
        #    return False
        self._logger.debug("Will use Gallery to open picture %s"%pitcureName)
        if self._device(text="Gallery",resourceId="android:id/text1").wait.exists(timeout=2000):
            self._logger.debug("Find Gallery APP")
            self._device(text="Gallery",resourceId="android:id/text1").click()
        elif self._device(textContains="Open with",resourceId="android:id/title").wait.exists(timeout=2000):
            self._logger.debug("Find Gallery APP")
        else:
            self._logger.debug("Can not find Gallery APP")
            return False
        if self._device(textMatches="(?i:Just once)",enabled=True).wait.exists(timeout=2000):
            self._device(textMatches="(?i:Just once)",enabled=True).click()
            while True:
                if self._device(textMatches="(?i:Allow)").wait.exists(timeout=2000):
                    self._device(textMatches="(?i:Allow)").click()
                    continue
                else:
                    break
        else:
            self._logger.debug("Just once is not enabled or text of Just once is wrong or click Gallery failure")
            return False
        if self._device(packageName="com.tct.gallery3d",resourceId="com.tct.gallery3d:id/gl_root_view").wait.exists(timeout=2000):
            self._logger.debug("%s has been opened using Gallery APPS"%pitcureName)
        else:
            self._logger.debug("%s has been opened using Gallery APPS"%pitcureName)
            return False
        if self._device.find(sys.path[0]+"\\resourcefile\\%s"%pitcureName):
            self._logger.debug("%s has been opened successfully"%pitcureName)
            return True
        else:
            self._logger.debug("%s has been opened failure"%pitcureName)
            return False
    
    def checkVideoPlay(self,videoPlayer):
        "Check selected videoPlayer"
        if videoPlayer=="Photos":
            if self._device(resourceId="com.google.android.apps.photos:id/photos_videoplayer_view_video_surface_view").wait.exists(timeout=2000):
                self._logger.debug("The video is playing")
                for i in range(5):
                    self._device.press.back()
                    if not self._device(resourceId="com.google.android.apps.photos:id/photos_videoplayer_view_video_surface_view").wait.exists(timeout=1000):
                        return True
                    i+=1
                else:
                    self._logger.debug("Return back failure when playing video")
                    return False
        if videoPlayer=="Video player":
            if self._device(text="Start over").wait.exists(timeout=1000):
                self._device(text="Start over").click()
            if self._device(resourceId="com.tct.gallery3d:id/surface_view",className="com.tct.gallery3d.app.MovieVideoView").wait.exists(timeout=2000):
                self._logger.debug("The video is playing")
                for i in range(5):
                    self._device.press.back()
                    if not self._device(resourceId="com.google.android.apps.photos:id/photos_videoplayer_view_video_surface_view").wait.exists(timeout=1000):
                        self._device.orientation ="n"
                        return True
                    i+=1
                else:
                    self._logger.debug("Return back failure when playing video")
                    return False

    def clearFillDate(self):
        self._logger.debug('begin to clear data')
        self._device.press.recent()
        if self._device(text='FillData').wait.exists(timeout=3000):
            self._device(text='FillData').click()
        else:
            self._logger.debug('not found FillData in recent app')
            return False
        if self._device(text='清除数据', resourceId='cn.test.filldata:id/btn_clean_data').wait.exists(timeout=3000):
            self._device(text='清除数据', resourceId='cn.test.filldata:id/btn_clean_data').click()
            self._logger.debug('click 清除数据')
            return True
        else:
            self._logger.debug('not found 清除数据')
            return False
    
    def copyAction(self,fileName):
        self._device(text=fileName).right(resourceId='com.jrdcom.filemanager:id/edit_moreMenu').click()
        if self._device(textMatches='(?i:Copy)').wait.exists(timeout=2000):
            self._device(textMatches='(?i:Copy)').click()
        else:
            self._logger.info('Copy Failed')
            return False
    
    def copyActionTwo(self):
        if self._device(resourceId='com.jrdcom.filemanager:id/more_btn').wait.exists(timeout=2000):
            self._device(resourceId='com.jrdcom.filemanager:id/more_btn').click()
        if self._device(resourceId='com.jrdcom.filemanager:id/copy_item_normal').wait.exists(timeout=2000):
            self._device(resourceId='com.jrdcom.filemanager:id/copy_item_normal').click()   
    
    def copyFileOrFolderToDiffDir(self,file_name,folder_name):
        if self.judgeExistsByManual(file_name) and self.judgeExistsByManual(folder_name):
            self.copyAction(file_name)
            self._device(text=folder_name).click()
            self.pasteAction()
            if self.judgeExistsByManual(file_name):
                self._logger.debug("copy file/folder successful")
                return True
            else:
                self._logger.debug("copy file/folder failed")
                return False
        else:
            self._logger.debug("copy file/folder failed..")
            return False
    
    def copyFileOrFolderToSameDir(self,file_name):
        if self.judgeExistsByManual(file_name):
            self.copyAction(file_name)
            self._device(resourceId='com.jrdcom.filemanager:id/floating_action_button').click()
            if self.judgeExistsByManual(file_name+'(0)'):
                self._logger.debug("%s file aleady exists"%file_name+'(0)')
                return True 
            else:
                self._logger.debug("%s file not exists"%file_name+'(0)')
                return False
        else:
            self._logger.debug("%s file not exists" % file_name)
            return False      
     
    def creatMoreFolder(self,num):
        self._logger.debug('creat %d layer floder.',num)
        floder_num=0
        for No in range(num):
            if self.createFolder('test_'+str(No+1)):
                if self.judgeExistsByManual('test_'+str(No+1)):
                    self._device(text='test_'+str(No+1)).click()
                    self._device.delay(2)
                    floder_num+=1
        if floder_num==num:
           return True
        self._logger.debug('creat %d layer floder fail.',num)
        return False
    
    def createFolder(self,folderName):             #If a folder with the same name it will be deleted and then re-created
        '''
        Create a folder.
        folderName
          string, folder name text
        return True/False
        '''
        if self.judgeExistsByManual(folderName):
            self._logger.debug('Find the folder :%s'%folderName)
            self.deleteFileOrFolder(folderName)
        else:
            self._logger.debug('Not found folder:%s'%folderName)
        self._logger.debug('Create a folder %s',folderName)
        if self._device(resourceId='com.jrdcom.filemanager:id/list_view',scrollable=True).exists:
            self._device(resourceId='com.jrdcom.filemanager:id/list_view',scrollable=True).scroll.toBeginning()
        if self._device(resourceId='com.jrdcom.filemanager:id/more_btn').wait.exists(timeout=10000):
            self._device(resourceId='com.jrdcom.filemanager:id/more_btn').click()
            if self._device(text='Create folder').wait.exists(timeout=10000):
                self._device(text='Create folder').click()
                self._device.delay(5)
        if self._device(resourceId='com.jrdcom.filemanager:id/edit_text').wait.exists(timeout=10000):
            self._device.delay(2)
            self._device(resourceId='com.jrdcom.filemanager:id/edit_text').set_text(folderName)
            self._device.delay(5)
            self._device(resourceId='android:id/button1').click()
            self._device.delay(5)
        if self.judgeExistsByManual(folderName):
            self._logger.debug('Creat the folder :%s successful .'%folderName)
            return True
        else:
            self._logger.debug('Fail to create the folder:%s .'%folderName)
            return False
    
    def cutFileOrFolderAction(self):
        if self._device(resourceId='com.jrdcom.filemanager:id/more_btn').wait.exists(timeout=2000):
            self._device(resourceId='com.jrdcom.filemanager:id/more_btn').click()
        if self._device(text='Cut').wait.exists(timeout=2000):
            self._device(text='Cut').click()
    
    def deleteAction(self):
        if self._device(resourceId='com.jrdcom.filemanager:id/more_btn').wait.exists(timeout=2000):
            self._device(resourceId='com.jrdcom.filemanager:id/more_btn').click()
        if self._device(resourceId='com.jrdcom.filemanager:id/delete_item_normal').wait.exists(timeout=2000):
            self._device(resourceId='com.jrdcom.filemanager:id/delete_item_normal').click()
            if self._device(resourceId='android:id/button1').wait.exists(timeout=2000):
                self._device(resourceId='android:id/button1').click()   
     
    def deleteFileOrFolder(self,name):
        '''
        Delete a file or folder.
        name
          string, file/folder name text
        
        '''
        self._logger.debug('Delete file/folder:%s...'%name)
        if self.judgeExistsByManual(name):
            self._device(text=name).long_click()
            self._device.delay(2)
            if self._device(resourceId='com.jrdcom.filemanager:id/delete_btn').wait.exists(timeout=3000):
                self._device(resourceId='com.jrdcom.filemanager:id/delete_btn').click()
                self._device.delay(2)
                if self._device(resourceId='android:id/button1').wait.exists(timeout=3000):
                    self._device(resourceId='android:id/button1').click()
                    self._device.delay(6)
                    if not self.judgeExistsByManual(name):
                        self._logger.debug('File/folder :%s had been deleted .'%name)
                        return True
                    else:
                        self._logger.debug('File/folder :%s delete fail .'%name)
                        return False
                else:
                    return False
            else:
                return False
        else:
            self._logger.debug('File/folder :%s is not exists ,no need to delete .'%name)
            return True
    
    def enterFileManager(self,times=5):
        '''
        Enter fileManager 5 times
        return True/False
        '''
        n=0
        while n<times:
            self._logger.debug('Try %d times to enter fileManager...',n+1)
            if self.enterFileManagerOnce():
                return True
            n+=1
        else:
            return False
    
    def enterFileManagerOnce(self,clearRecentsApp=True):
        '''
        Enter fileManager once time.
        return True/False
        '''
        self.resetWatchers(["AUTO_ALLOW", "AUTO_CANCEL_GPS"])
        if self.clickAppIconInAppList('Files', clearRecentsApp):
            if self.isInFilemanager():
                self._logger.debug('Enter Files successfully!')
                self.removeWatchers()
                return True
        self._logger.debug('Enter Files fail!')
        self.removeWatchers()
        return False

    def enterFolder(self,folderName):
        "Enter folder, such as bluetooth、picture and so on"
        if(self._device(text=folderName,resourceId="com.jrdcom.filemanager:id/edit_adapter_name").wait.exists(timeout=3000)
        or self._device(scrollable=True).scroll.to(text=folderName)):
            self._device(text=folderName,resourceId="com.jrdcom.filemanager:id/edit_adapter_name").click()
        else:
            self._logger.debug("Can not find %s folder"%folderName)
            return False
        if self._device(text=folderName,resourceId="com.jrdcom.filemanager:id/path_text").wait.exists(timeout=2000):
            self._logger.debug("Enter %s folder successfully."%folderName)
            return True
        else:
            self._logger.debug("Enter %s folder failure."%folderName)
            return False
    
    def enterPartition(self,name):
        '''
        Enter partition : Phone storage / SD card
        name 
          string, file partition(Phone storage/SD card)
          
        return True/False
        '''
        if not self.backToMainScreen():
            return False
        self._logger.debug('Enter %s .'%name)
        if name.lower()=='Phone'.lower():
            if self._device(resourceId='com.jrdcom.filemanager:id/phone_name').wait.exists(timeout=3000):
                self._device(resourceId='com.jrdcom.filemanager:id/phone_name').click()
                if self._device(resourceId='com.jrdcom.filemanager:id/path_text').exists and self._device(textMatches='(?i:Phone)').exists:
                    self._logger.debug('Enter %s successfully.'%name)
                    return True
                else:
                    self._logger.debug('Fail to enter %s .'%name)
                    return False
        if name.lower()=='SD'.lower():
            if self._device(resourceId='com.jrdcom.filemanager:id/sd_name').wait.exists(timeout=3000):
                self._device(resourceId='com.jrdcom.filemanager:id/sd_name').click()
                if self._device(resourceId='com.jrdcom.filemanager:id/path_text').exists and self._device(textMatches='(?i:SD CARD)').exists:
                    self._logger.debug('Enter %s successfully.'%name)
                    return True
                else:
                    self._logger.debug('Fail to enter %s .'%name)
                    return False

    def fillData(self, tarPer=50):
        self._logger.debug('begin to fill data %d', tarPer)
        dataPer = float(self._device(resourceId='cn.test.filldata:id/text_use_percent_value').get_text())
        if dataPer > tarPer:
            self._device.shell_adb('shell rm -rf /data/data/cn.test.filldata/files/')
        self._device(resourceId='cn.test.filldata:id/edit_fill_percent_value').clear_text()
        self._device(resourceId='cn.test.filldata:id/edit_fill_percent_value').set_text(str(tarPer))
        self._device(resourceId='cn.test.filldata:id/btn_start_fill').click()
        if self._device(text='Storage is low').exists:
            self._device(resourceIdMatches='.*settings:id/btn_no').click
            self._device(resourceId='cn.test.filldata:id/btn_start_fill').click()
        while True:
            self._device.delay(5)
            if self._device(text='Storage is low').exists:
                self._device(resourceIdMatches='.*settings:id/btn_no').click
            isEnable = self._device(resourceId='cn.test.filldata:id/btn_start_fill').isEnabled()
            if isEnable:
                break
        if self._device(text='IGNORE', resourceId='com.android.settings:id/btn_ignore').wait.exists(timeout=3000):
            self._device(text='IGNORE', resourceId='com.android.settings:id/btn_ignore').click()
        self._logger.debug('finish to fill data %d', tarPer)
    
    def getFileInfo(self,fileName):
        "Return file info, such as size"
        self._device(scrollable=True).scroll.to(text=fileName)
        if self._device(text=fileName).wait.exists(timeout=2000):
            self._device(text=fileName).right(resourceId="com.jrdcom.filemanager:id/edit_moreMenu").click()
        else:
            self._logger.debug("Can not find file")
            return False
        if self._device(text="Details").wait.exists(timeout=2000):
            self._device(text="Details").click()
            if self._device(text="Details",resourceId="android:id/alertTitle").wait.exists(timeout=2000):
                self._logger.debug("Enter Details successfully")
            else:
                self._logger.debug("Fail to enter Details")
                return False
        else:
            self._logger.debug("Can not fild Details key")
            return False
        if self._device(text="Size").wait.exists(timeout=2000):
            file_size_info=self._device(text="Size").down(resourceId="com.jrdcom.filemanager:id/detail_value").get_text()
            if file_size_info!=None:
                self._logger.debug("Size of %s is %s"%(fileName,file_size_info))
                if self._device(textMatches="(?i:Close)",resourceId="android:id/button2").wait.exists(timeout=2000):
                    self._device(textMatches="(?i:Close)",resourceId="android:id/button2").click()
                    return file_size_info
                else:
                    return file_size_info
            else:
                self._logger.debug("Size of %s is NULL"%fileName)
                return False
        else:
            self._logger.debug("Can not Size")
            return Fasle
    
    def installApk(self,apk_name):
        if self.judgeExistsByManual(apk_name):
            self._device(text=apk_name).click()
            if self._device(resourceId='com.android.packageinstaller:id/ok_button').wait.exists(timeout=2000):
                self._device(resourceId='com.android.packageinstaller:id/ok_button').click()
                self._device.delay(2)
        if self._device(text='Install').wait.exists(timeout=2000):
            self._device(text='Install').click()
        if self._device(text='App installed.').wait.exists(timeout=50000):
            self._logger.debug('Install %s successful!',apk_name)
            self._device(text='Done').click()
            return True
        else:
            self._logger.debug('Install %s Failed!',apk_name)
            return False
    def isInFilemanager(self):
        """
        juege now is or not in Filemanager.
        return: True/False
        """
        if self._device(resourceId='com.jrdcom.filemanager:id/path_text').wait.exists(timeout=3000):
            self._logger.debug('The current screen haved Filemanager layout.')
            return True
        else:
            self._logger.debug('The current screen not find Filemanager layout.')
            return False

    def judgeExistsByAdb(self,name,path):
        '''judge the file/folder whether exists use adb command .

        '''
        name_list=self._device.shell_adb("shell ls "+path)
        if name in name_list:
            return True
        else:
            return False

    def judgeExistsByManual(self,name):
        '''
        Judge the file/folder whether exists by manual .
        name
          string, file/folder name text
        
        return True/False
        '''
        if self._device(text='This folder is empty').wait.exists(timeout=3000):
            self._logger.debug("This folder is empty")
            return False
        self._logger.debug("Judge the file/folder %s whether exists "%name)
        if self._device(textMatches=name).wait.exists(timeout=3000):
            self._logger.debug("had found the file %s"%name)
            return True
        if (self._device(resourceId='com.jrdcom.filemanager:id/list_view',scrollable=True).exists
        and self._device(scrollable=True).scroll.to(resourceId='com.jrdcom.filemanager:id/edit_adapter_name',textStartsWith=name)
        and self._device(textMatches=name).wait.exists(timeout=3000)):
            self._logger.debug("had found the file %s"%name)
            return True
        return False
            
        
    def myPushFileToPhone(self,sourceFile,targetPath):
        path=(sys.path[0]+'/ResourceFile/'+sourceFile)
        command='push'+' '+path+' '+targetPath
        self._device.shell_adb(command)
    
    def pasteAction(self):
        self._device(resourceId='com.jrdcom.filemanager:id/more_btn').click()
        if self._device(text='Paste').wait.exists(timeout=2000):
            self._device(text='Paste').click()
        else:
            self._logger.info('Paste failed')
            return False
    
    def readStorageSize(self,storageType):
        '''
        Read and return the storage info and judge it's correct or not.
        storageType
          string, the storage partition type(Phone storage/SD card)
        
        return True/False
        '''
        p_str='(\d*.\d*)[ /a-zA-Z]*(\d*.\d*)[ /a-zA-Z]*'
        p=re.compile(p_str)
        s=''
        self.enterFileManagerOnce()
        if storageType=='Phone storage':
            self._logger.debug("Read phone's size.")
            #if not self._device(text='Phone storage').wait.exists(timeout=3000):
            if not self._device(resourceId="com.jrdcom.filemanager:id/phone_name").wait.exists(timeout=3000):
                self._logger.debug("Can not found 'Phone storage'.")
                return False
            s=self._device(resourceIdMatches='com.jrdcom.filemanager:id/phone_(size|used_info_tv)').get_text()
        elif storageType=='SD card':
            self._logger.debug("Read SD's size.")
            #if not self._device(text='SD storage').wait.exists(timeout=3000):
            if not self._device(resourceId="com.jrdcom.filemanager:id/sd_name").wait.exists(timeout=3000):
                self._logger.debug("Can not found 'SD storage'.")
                return False
            s=self._device(resourceIdMatches='com.jrdcom.filemanager:id/sd_(size|used_info_tv)').get_text()
        
        self._logger.debug("Read the size:%s.",s)
        m=re.match(p,s)
        if not m.group():
            self._logger.debug("Please check the size format mode.")
            return False
        else:
            if 'MB' in s and 'GB' in s:
                s1=m.group(1)
                self._logger.debug('%s is %s.',storageType,s)
                return float(s1)
            elif 'MB' not in s and 'GB' in s:
                s1=m.group(1)
                s2=m.group(2)
                if float(s1)<float(s2):
                    if 'free' in s:
                        s_temp=float(s2)-float(s1)
                    else:
                        s_temp=float(s1)
                    self._logger.debug('%s is %s/%s.',storageType,s_temp,s2)
                    return s_temp
                else:
                    self._logger.debug('%s is Nok: %s',storageType,s)
                    return False
            else:
                self._logger.debug("Please check the size format mode.")
                return False
    
    def renameFolder(self,primitiveName,newName):
        self._logger.debug('rename %s to %s',primitiveName,newName)
        if self._device(resourceId='com.jrdcom.filemanager:id/list_view').isScrollable():
            self._device(scrollable=True).scroll.to(text=primitiveName)
            self._device.delay(1)
            self._device(text=primitiveName).long_click()
        else:
            self._device.delay(1)
            self._device(text=primitiveName).long_click()
        if self._device(resourceId='com.jrdcom.filemanager:id/more_btn').wait.exists(timeout=2000):
            self._device(resourceId='com.jrdcom.filemanager:id/more_btn').click()
        else:
            self._logger.debug("Can not find more_btn")
            return False
        self._device.delay(1)
        self._device(text='Rename').click()
        self._device.delay(2)
        self._device(resourceId='com.jrdcom.filemanager:id/edit_text').set_text(newName)
        self._device.delay(1)
        self._device(resourceId='android:id/button1').click()
        self._device.delay(3)
        if self._device(resourceId='com.jrdcom.filemanager:id/list_view').isScrollable():
            self._device(scrollable=True).scroll.to(text=newName)
        if self._device(text=newName).exists:
            return True
        self._logger.debug('rename %s to %s fail!',primitiveName,newName)
        return False
    def resetWatchers(self,watcherList=[""]):
        """
        reset watchers,and add watcher list
        :param watcherList: list watchers name
        :return: void
        """
        self.removeWatchers()
        if "AUTO_ALLOW" in watcherList:
            self._device.watcher("AUTO_ALLOW").when(resourceId='com.android.packageinstaller:id/permission_message').click(textMatches='(?i:ALLOW)')
        if "AUTO_CANCEL_GPS" in watcherList:
            self._device.watcher("AUTO_CANCEL_GPS").when(textMatches='(?i:GPS off)').click(textMatches='(?i:Cancel)')
        if "AUTO_GOTIT" in watcherList:
            self._device.watcher("AUTO_GOTIT").when(resourceId='android:id/ok',text="GOT IT").click(text="GOT IT")
        if "AUTO_CANCEL_TagLog" in watcherList:
            self._device.watcher("AUTO_CANCEL_TagLog").when(resourceId='android:id/alertTitle',text="Tag Log").click(text="CANCEL")
        self._logger.debug("List watchers:%s",self._device.watchers)

    def removeWatchers(self):
        """
        remove all watches
        :return : void
        """
        self._logger.debug("remove watchers:%s",self._device.watchers)
        self._device.watchers.remove()
    def searchFolder(self,searchName):
        self._logger.debug('search %s ',searchName)
        if self._device(resourceId='com.jrdcom.filemanager:id/list_view',scrollable=True).exists:
            self._device(resourceId='com.jrdcom.filemanager:id/list_view',scrollable=True).scroll.toBeginning()
        if self._device(resourceId='com.jrdcom.filemanager:id/search_btn').click():
            self._device(resourceId='android:id/search_src_text').set_text(searchName)
            
            if self._device(text=searchName).exists:
                self._logger.debug('Search %s successfully.',searchName)
                return True
        else:
            self._logger.debug('Can not search %s ',searchName)
            return False
    
    def selectAllFileSend(self,bt_name):
        "Seclect all files to send via bluetooth"
        fileNumber = ""
        if self._device(description="More options",index=2).wait.exists(timeout=2000):
            self._device(description="More options",index=2).click()
        else:
            self._logger.debug("Can not find More options,index=2")
            return False
        if self._device(text="Select",resourceId="com.jrdcom.filemanager:id/select_item").wait.exists(timeout=2000):
            self._device(text="Select",resourceId="com.jrdcom.filemanager:id/select_item").click()
        else:
            self._logger.debug("Can not find Seclect button")
            return False
        if self._device(resourceId="com.jrdcom.filemanager:id/more_btn",index=0).wait.exists(timeout=2000):
            self._device(resourceId="com.jrdcom.filemanager:id/more_btn",index=0).click()
        else:
            self._logger.debug("Can not find More options,index=0")
            return False
        if self._device(text="Select all").wait.exists(timeout=2000):
            self._device(text="Select all").click()
        else:
            self._logger.debug("Can not find Select all button")
            return False
        if self._device(resourceId="com.jrdcom.filemanager:id/edit_path_text").wait.exists(timeout=2000):
            fileNumber = self._device(resourceId="com.jrdcom.filemanager:id/edit_path_text").get_text()
            if int(fileNumber)>0:
                self._logger.debug("Seclect %s files to send via bluetooth"%fileNumber)
            else:
                self._logger.debug("Seclect files failure")
                return False
        else:
            self._logger.debug("Can not find Select all button")
            return False
        if self._device(resourceId="com.jrdcom.filemanager:id/share_btn").wait.exists(timeout=2000):
            self._device(resourceId="com.jrdcom.filemanager:id/share_btn").click()
            self._device.delay(1)
        else:
            self._logger.debug("Can not find share_btn")
            return False
        if self._device(text='Bluetooth').wait.exists(timeout=2000):
            self._device(text='Bluetooth').click()
            for i in range(20):
                if not self._device(text='Bluetooth').exists:
                    self._logger.debug('Choose Bluetooth to send file')
                    break
                self._device.delay(0.5)
                i+=1
            for i in range(10):
                if self._device(text=bt_name).wait.exists(timeout=5000):
                    self._logger.debug('Have find %s to send file'%bt_name)
                    self._device(text=bt_name).click()
                    self._device.delay(2)
                    return fileNumber
                else:
                    if self._device(description="More options").wait.exists(timeout=2000):
                        self._device(description="More options").click()
                        if self._device(text='Refresh').wait.exists(timeout=2000):
                            self._device(text='Refresh').click()
                            self._device.delay(6)
                            self._logger.debug('Search %s device: %s times'%(bt_name,(i+1)))
                            i+=1
            else:
                self._logger.debug("Send files failure via bluetooth")
                return False
    
    def selectVideoPlay(self,videoFileName,videoPlayer):
        "Select a video player, videoPlayer is Video player or Photos"
        flag = False
        if self._device(scrollable=True):
            self._device(scrollable=True).scroll.to(text=videoFileName)
        if self._device(text=videoFileName).exists:
            self._logger.debug("Find %s video file"%videoFileName)
            self._device(text=videoFileName).click()
        else:
            self._logger.debug("Can not find %s video file"%videoFileName)
            return False
        if self._device(text=videoPlayer).wait.exists(timeout=2000)and \
                not self._device(text="Use a different app").wait.exists(timeout=1000):
            self._logger.debug("Find %s"%videoPlayer)
            self._device(text=videoPlayer).click()
        elif self._device(text="Open with "+videoPlayer).wait.exists(timeout=2000):
            self._logger.debug("Find Open with %s"%videoPlayer)
        elif self._device(text="Use a different app").wait.exists(timeout=2000):
            if self._device(text="Use a different app").down(text=videoPlayer):
                self._logger.debug("Find %s"%videoPlayer)
                self._device(text="Use a different app").down(text=videoPlayer).click()
                flag = True
        else:
            self._logger.debug("Can not find %s"%videoPlayer)
            return False
        if not flag and self._device(text="Just once").wait.exists(timeout=2000):
            if self._device(textMatches="(?i:Just once)").isEnabled():
                self._device(textMatches="(?i:Just once)").click()
            else:
                self._logger.debug("Just once is not enabled")
                return False
        else:
            self._logger.debug("Can not find Just once")
            return False
        n=0
        while n<10:
            if self._device(text="(?i:Allowe)").wait.exists(timeout=1000):
                self._device(text="(?i:Allowe)").click()
                n+=1
            else:
                return True
    
    def shareFile(self,fileName,storage):
        self.enterFileManagerOnce()
        self.enterPartition(storage)
        if self.judgeExistsByManual('DCIM'):
            self._device(text='DCIM').click()
        else:
            self._logger.info('not found DCIM file')
            return False
        if self.judgeExistsByManual('Camera'):
            self._device(text='Camera').click()
        else:
            self._logger.info('not found Camera file,maybe not exists Camera folder')
        if self.judgeExistsByManual(fileName):
            self._device(text=fileName).right(resourceId='com.jrdcom.filemanager:id/edit_moreMenu').click()
        else :
            self._logger.info('not found %s',fileName)
            return False
        self._device(text='Share').click()

        # Share with message
        if self._device(text='Messaging').wait.exists(timeout=2000):
            self._device(text='Messaging').click()
            if self._device(resourceId='com.android.mms:id/image_content').wait.exists(timeout=2000):
                self._device(resourceId='com.android.mms:id/recipients_editor').set_text('911')
                self._device(resourceId='com.android.mms:id/send_button_mms').click()
                if self._device(resourceId='com.android.mms:id/avatar').wait.exists(timeout=2000):
                    self._logger.info('Message shared successful')
                    return True
            else:
                self._logger.info('Message shared failed')
                return False    
    
    def shareFileViaApp(self,appName,fileFormat):
        '''
        Share the File via other app:appName
        appName
          string, App name text
          
        return True/False
        '''
        self._logger.debug('Begin to share the File via :%s',appName)
        # self._device.dump('fileTemp.xml')
        if (not self._device(textMatches='.*'+fileFormat).exists and 
        not (self._device(scrollable=True).exists and 
        self._device(scrollable=True).scroll.to(textMatches='.*'+fileFormat))):
            self._logger.debug('Not find the %s files',fileFormat)
            return False
        self._device(textMatches='.*'+fileFormat).long_click()
        if not self._device(resourceId='com.jrdcom.filemanager:id/share_btn').exists:
            self._logger.debug('Not find the shre button')
            return False
        self._device(resourceId='com.jrdcom.filemanager:id/share_btn').click()
        if not self.enterSubMenuViaText(appName):
            return False
        return True
    
    def showHideFile(self):
        if self._device(resourceId='com.jrdcom.filemanager:id/more_btn').wait.exists(timeout=6000):    
            self._device(resourceId='com.jrdcom.filemanager:id/more_btn').click()
        if self._device(resourceId='com.jrdcom.filemanager:id/show_item').wait.exists(timeout=2000):
            self._device(text='Show hidden files').click()
            self._logger.info('Show hidden files')
            return True
        elif self._device(resourceId='com.jrdcom.filemanager:id/hide_item').wait.exists(timeout=2000):
            self._logger.info('Already show hidden files')
            self._device.press.back()
            return True
        else:
            return False

    def unstallAPK(self,apkName):
        "unstallAPK apk"
        apk_name = apkName.split(".")[1]
        self._device(scrollable=True).scroll.to(resourceId='android:id/title',text=apk_name)
        if self._device(text=apk_name).wait.exists(timeout=2000):
            self._device(text=apk_name).click()
        else:
            self._logger.debug("Can not find %s"%apk_name)
            return False
        if self._device(text="UNINSTALL").wait.exists(timeout=2000):
            self._logger.debug("Find UNINSTALL button")
            if self._device(text="UNINSTALL").isEnabled():
                self._device(text="UNINSTALL").click()
            else:
                self._logger.debug("UNINSTALL is not enabled")
                return False
        else:
            self._logger.debug("Can not find %s"%apk_name)
            return False
        if self._device(text="Do you want to uninstall this app?").wait.exists(timeout=2000):
            self._logger.debug("Enter unstallAPK interface")
            if self._device(text="OK").wait.exists(timeout=2000):
                self._device(text="OK").click()
            else:
                self._logger.debug("Can not find OK button to unstallAPK apk")
                return False
            for i in range(60):
                if self._device(scrollable=True).scroll.to(text=apk_name):
                    self._device.delay(1)
                    i+=1
                else:
                    self._logger.debug("unstallAPK apk successfully")
                    return True
            else:
                self._logger.debug("unstallAPK apk successfully")
                return True
        else:
            self._logger.debug("Can not find %s"%apkName)
            return False
   



