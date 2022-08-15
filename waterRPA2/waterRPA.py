
import pyautogui  #主力库
import time
import xlrd
import pyperclip

#定义鼠标事件

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159
""" 
ctype : 2 数字
        1 字符串
        0 空

"""


def mouseClick(clickTimes,lOrR,img,reTry):
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)  #根据传入的图片返回屏幕中图片的位置
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)  #操作键盘和鼠标的接口
                break
            print("未找到匹配图片,0.5秒后重试")
            time.sleep(0.5)
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




# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5
def dataCheck(my1):
    checkCmd = True
    #行数检查
    if my1.nrows<2: #行数小于2行
        print("没数据啊哥")
        checkCmd = False
    #每行数据检查
    i = 1
    while i < my1.nrows:
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

#任务
def mainWork(my_sheet,flag):
    
    i = 1
    time_flag = flag
    while i < my_sheet.nrows:
        #取本行指令的操作类型
        cmdType = my_sheet.row(i)[0]
        if cmdType.value == 1.0:
            #取图片名称
            img = my_sheet.row(i)[1].value
            reTry = 1
            if my_sheet.row(i)[2].ctype == 2 and my_sheet.row(i)[2].value != 0: #第三列的内容类型为数字类型，并且不为0
                reTry = my_sheet.row(i)[2].value
            mouseClick(1,"left",img,reTry) #左键对匹配图像单击一次，重复: retrys
            print("单击左键",img)
        #2代表双击左键
        elif cmdType.value == 2.0:
            #取图片名称
            img = my_sheet.row(i)[1].value
            #取重试次数
            reTry = 1
            if my_sheet.row(i)[2].ctype == 2 and my_sheet.row(i)[2].value != 0:
                reTry = my_sheet.row(i)[2].value
            mouseClick(2,"left",img,reTry)
            print("双击左键",img)
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
            if time_flag == 1:
                 inputValue = my_sheet.row(i)[1].value    
            elif time_flag == 2:
                 inputValue = my_sheet.row(i)[3].value   
            elif time_flag == 3:
                 inputValue = my_sheet.row(i)[4].value  
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

#用于给女朋友发早安
def girlfrien_time(time_flag,hour,minute):
    if time_flag == 0:
        return
    print("girlfrien_time:",hour,":",minute)
    file = '.\zxl2\cmd.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)  #读exccle
    #通过索引获取表格sheet页
    my1 = wb.sheet_by_index(3)
    #数据检查
    checkCmd = dataCheck(my1)
    if checkCmd:
        #key=input('选择功能: 1.做一次 2.循环到死 \n')
        key = '1'
        if key=='1':
            #循环拿出每一行指令
            mainWork(my1, time_flag)
        elif key=='2':
            while True:
                mainWork(my1 , time_flag)
                time.sleep(0.1)
                print("等待0.1秒")    
    else:
        print('输入有误或者已经退出!')

if __name__ == '__main__': #如果此文件不是作为其他文件的输如文件那么if成立,否则__name__==__文件名__
    girlfrien_time(1)
