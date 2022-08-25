from http.client import NETWORK_AUTHENTICATION_REQUIRED, SWITCHING_PROTOCOLS
from typing import Text
from xmlrpc.client import Fault
import pyautogui  #主力库
import time
import xlrd
import pyperclip
import datetime
import os,sys
import zxl2.waterRPA as zxl
sys.path.append("E:\culture\Professional\Project\python")
import daily_reminder.main0 as zxl_main0


#sys.path.append(r'.\zxl2')
#import waterRPA

os.chdir(sys.path[0])  #使用相对路径

if __name__ == '__main__': #如果此文件不是作为其他文件的输如文件那么if成立,否则__name__==__文件名__
    #time_flag = 0 
   # path_file = os.path.join('zxl11.txt')
    Text = 1
    Other = False
    print("hello")
    while True:
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute

            if (hour==8 and minute==0)or (hour==12 and minute==0) or(hour==23 and minute==0):  #日常任务
                zxl_main0.main0()
                zxl.girlfrien_time(datetime.datetime.now().hour,datetime.datetime.now().minute)

            elif ((hour==5 or hour == 5+12)and minute==21)or (hour==13 and minute==14) or(hour==0 and minute==0): #添花任务
                zxl.girlfrien_time(hour,minute)  
                         
            elif Text:
                print(datetime.datetime.now())
                zxl_main0.main0()
                zxl.girlfrien_time(5,21)
                
    
            time.sleep(58)















    while Fault:
        if(datetime.datetime.now().hour==8 and datetime.datetime.now().minute==0):
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            waterRPA.girlfrien_time(1,hour,minute)
        elif(datetime.datetime.now().hour==12 and datetime.datetime.now().minute==0):
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            waterRPA.girlfrien_time(2,hour,minute)
        elif(datetime.datetime.now().hour==23 and datetime.datetime.now().minute==8):
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            waterRPA.girlfrien_time(3,hour,minute)


        elif (hour==15 and minute==21) or (hour==17 and minute==20) or (hour==18 and minute==30) or (hour==6 and minute==30) or  (hour==9 and minute==30):
          zxl.girlfrien_time(99,99)