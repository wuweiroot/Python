
from ast import And, Break, Return
import re
from sre_parse import State
from struct import iter_unpack
import pyautogui  #主力库
import time
import xlrd
import pyperclip
import random
import datetime
import os,sys

#定义鼠标事件

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159
""" 
ctype : 2 数字
        1 字符串
        0 空

"""


def mouseClick(clickTimes,lOrR,img,reTry):
    State = 1
    i = 1
    if reTry == 1:
        for i in  range(10):
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)  #根据传入的图片返回屏幕中图片的位置
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)  #操作键盘和鼠标的接口
                if clickTimes == 1:
                    print("单击左键",img)
                if clickTimes == 2:
                    print("双击左键",img)
                State = 0
                break
            print("未找到匹配图片,0.5秒后重试 重试次数：",i)
            time.sleep(0.5)
            i = i+1
    elif reTry == -1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)
    print("mouseClick State:",State)
    return State




# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5
def dataCheck(my1,Start,end):
    checkCmd = True
    #行数检查
    if my1.nrows<2: #行数小于2行
        print("没数据啊哥")
        checkCmd = False
    #每行数据检查
    i = 1
    #while i < my1.nrows:
    for i in  range(Start,end):
        # 第1列 操作类型检查
        cmdType = my1.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0 
        and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0):
            print('第',i+1,"行,第1列数据有毛病")
            checkCmd = False
        # 第2列 内容检查
        cmdValue = my1.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value ==1.0 or cmdType.value == 2.0 or cmdType.value == 3.0:
            if cmdValue.ctype != 1:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        i += 1
    return checkCmd
#时间任务
def time_work(my_sheet,i,hour,minute):
    j = 1
    j = random.randrange(1,25,1)
    if hour == 8 and minute == 0:
            inputValue = my_sheet.row(i)[1].value    
    elif hour == 12 and minute == 0:
            inputValue = my_sheet.row(i)[3].value   
    elif hour == 11 and minute == 0:
            inputValue = my_sheet.row(i)[4].value  
    elif hour ==5 and minute ==21:
            inputValue = "我爱你！"
    elif hour ==13 and minute ==14:
            inputValue = "一生一世，我爱你！"
    elif hour ==0 and minute ==0:
            inputValue = "新的一天依旧爱你哦！"
    elif hour ==99 and minute == 99:
            print("j =",j)
            inputValue = my_sheet.row(j)[6].value  
            print("inputValue:",inputValue)
    return inputValue

#发送消息前添加消息
def add_information(my_sheet):
    j = random.randrange(1,25,1)
    inputValue = my_sheet.row(j)[6].value  
    print(inputValue)
    pyperclip.copy(inputValue)
    pyautogui.hotkey('ctrl','v')
    reTry = 1
    img = my_sheet.row(3)[1].value
    State = mouseClick(1,"left",img,reTry) #左键对匹配图像单击一次，重复: retrys
    if State == 1 :
       print("重试次数超时脚本1退出")  
    return State


#任务
def mainWork(my_sheet,hour,minute,Start,end):
    
    print(Start)
    State = 1
    #while i < my_sheet.nrows:
    for i in  range(Start,end+1):   #前闭后开区间
        #取本行指令的操作类型
        print("指令行i:",i)
        cmdType = my_sheet.row(i)[0]
        print(cmdType)
        print(cmdType.value)
        if cmdType.value == 1.0:
            #取图片名称
            img = my_sheet.row(i)[1].value
            reTry = 1
            if my_sheet.row(i)[2].ctype == 2 and my_sheet.row(i)[2].value != 0: #第三列的内容类型为数字类型，并且不为0
                reTry = my_sheet.row(i)[2].value
            State = mouseClick(1,"left",img,reTry) #左键对匹配图像单击一次，重复: retrys
            if State == 1 :
                print("重试次数超时脚本1退出")  
                return State
        #2代表双击左键
        elif cmdType.value == 2.0:
            #取图片名称
            img = my_sheet.row(i)[1].value
            #取重试次数
            reTry = 1
            if my_sheet.row(i)[2].ctype == 2 and my_sheet.row(i)[2].value != 0:
                reTry = my_sheet.row(i)[2].value
            State = mouseClick(2,"left",img,reTry)
            if State == 1 :
               print("重试次数超时脚本1退出")
               return State
        #3代表右键
        elif cmdType.value == 3.0:
            #取图片名称
            img = img.row(i)[1].value
            #取重试次数
            reTry = 1
            if my_sheet.row(i)[2].ctype == 2 and my_sheet.row(i)[2].value != 0:
                reTry = my_sheet.row(i)[2].value
            mouseClick(1,"right",img,reTry)
            print("右键",img) 
        #4代表输入
        elif cmdType.value == 4.0:
            add_information(my_sheet)
            inputValue =  time_work(my_sheet,i,hour,minute)   #发送消息内容
            pyperclip.copy(inputValue)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            print("输入:",inputValue)                                        
        #5代表等待
        elif cmdType.value == 5.0:
            #取图片名称
            waitTime = my_sheet.row(i)[1].value
            time.sleep(waitTime)
            print("等待",waitTime,"秒")
        #6代表滚轮
        elif cmdType.value == 6.0:
            #取图片名称
            scroll = my_sheet.row(i)[1].value
            pyautogui.scroll(int(scroll))
            print("滚轮滑动",int(scroll),"距离")                      
        i += 1
    return State

#用于给女朋友发早安
def girlfrien_time(hour,minute):
    State = 0
    if hour == 9999:
        return
    print("girlfrien_time:", datetime.datetime.now())
    file = '.\zxl2\cmd.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)  #读exccle
    #通过索引获取表格sheet页
    my1 = wb.sheet_by_index(3)
    #数据检查
    checkCmd = dataCheck(my1,1,5)
    checkCmd = dataCheck(my1,6,11)
    checkCmd = dataCheck(my1,13,18)
    if checkCmd:
        #key=input('选择功能: 1.做一次 2.循环到死 \n')
        key = '1'
        if key=='1':
            #循环拿出每一行指令
            State = mainWork(my1, hour,minute,1,4) #执行自动化脚本1
            if State == 1:          #脚本1执行失败
                 print("脚本1执行失败，进入脚本2")
                 State = mainWork(my1, hour,minute,6,11)  #执行自动化脚本2     
            if State == 1:          #脚本2执行失败
                 print("脚本2执行失败，进入脚本3")
                 State = mainWork(my1, hour,minute,13,18)  #执行自动化脚本3  
            if State == 1:  
                print("任务执行失败,此任务退出")    
                return  
            else:
                print("任务执行成功！")
                print(datetime.datetime.now())
        elif key=='2':
            while True:
                mainWork(my1 , hour,minute)
                time.sleep(0.1)
                print("等待0.1秒")    
    else:
        print('输入有误或者已经退出!')

if __name__ == '__main__': #如果此文件不是作为其他文件的输如文件那么if成立,否则__name__==__文件名__
    girlfrien_time(12,00)
