from http.client import NETWORK_AUTHENTICATION_REQUIRED, SWITCHING_PROTOCOLS
from xmlrpc.client import Fault
import pyautogui  #主力库
import time
import xlrd
import pyperclip
import datetime
import os,sys
import waterRPA

os.chdir(sys.path[0])  #使用相对路径

if __name__ == '__main__': #如果此文件不是作为其他文件的输如文件那么if成立,否则__name__==__文件名__
    #time_flag = 0 
   # path_file = os.path.join('zxl11.txt')
   # print(path_file)
    while True:
        #not_time = datetime.datetime.now()
        #hour = not_time.hour
        #minute = not_time.minute
        #print(hour,":",minute)
        #if(datetime.datetime.now().hour==8 or datetime.datetime.now().hour==12 or datetime.datetime.now().hour==23):
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            print(hour,":",minute)
            if hour==8 and minute==0:
                waterRPA.girlfrien_time(1,hour,minute)
            elif hour==12 and minute==0: 
                waterRPA.girlfrien_time(2,hour,minute) 
            elif hour==23 and minute==16: 
                print("晚安")
                waterRPA.girlfrien_time(3,hour,minute)
            else:
                print(datetime.datetime.now())
                waterRPA.girlfrien_time(3,hour,minute)
                #time.sleep(10)





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