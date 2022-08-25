import pyautogui
import time
import xlrd
import pyperclip
import os,sys
import datetime


os.chdir(sys.path[0])  #使用相对路径
     
if __name__ == '__main__':   
    file = 'cmd.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)  #读exccle
    #通过索引获取表格sheet页
    my1 = wb.sheet_by_index(3)
    my1.nrows
    my1.row

    #my1.value()
    print(my1)
    print(my1.nrows)
   # print(my1.value())
    print(my1.row)

    #datetime.datetime.now().date
