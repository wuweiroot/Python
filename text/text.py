
print("hellow word!")  #单行程序脚本运行 shift+entry

# 字面量
""" 
66
13.13
-11
"对对对"
 """
print(666)
print(13.13)
print("对对对")

money = 50
print("money=",money)

money = money-10
print("money =",money,"元")

""" 01
    python关键字
        import keyword
        print(keyword.kwlist)


"""

a =1 
b =2 
c =3
# 换行符
ddd = a + \
      b + \
      c
print(ddd)

#带括号的不需要换行符号
eee = [1,2,
       3,4]

fff = (12,32,
        22,33)
xxx = {
    "名字":"无为",
    "年龄":"十八岁"
}

""" 
    02
    python 引号 --字符串
    python 注释
    python 空格和空行

 """

abc = "rrrrrrtt\
      tttrr"

aa = input("请输入你的密码")
print("密码是:",aa)

print("请输入你的\n密码")  #\n换行
print("制表符四个空格一组\t制表符")  #\t制表符  补齐至 四个空格一组 
print("后面的覆盖前面\r内容")             #\r后面的覆盖前面内容
print("删除一个字aew\b符")            #\b ->键盘 backspace 删除一个字符
print("\\")    # // =>/
print(r"请输入你的\n密码")  #r 转义失效

""" 
    03
    变量 ：字母数字下划线，变量名区分大小写
    常量 ：大写变量约定为常量
"""
abc = 00

import keyword
print(keyword.kwlist)

a = 1
b = 2

a , b = 3 , 4 #多行变量赋值

PI = 3.1415926  #大写变量约定为常量


""" 
    04
    数据类型
        Int  : 整形
        float : 浮点数
        bool  : 布尔
"""
a = 100
b = -99 #int
c = 99.22 #float
dd = True #bool

""" 
    05
    数字运算
        // :向下取整
        % ：取余
        ** ：乘方
"""

print(2//3)
print(2%3)
print(2**3)

print(1>2)

# b00l : true == 1 fauls == 0

""" 
    06
    1 python 的空值 -- None //什么都没有 单独存在的数据类型
    2 内置函数的返回值 ->> None

"""

r = print("hellow word!") 
print(r)

""" 
    07
    字符串
        切片：【开始：结束】取左不取右
              【：】整个字符串

 """
name = "小仙女温柔且善良"

print(name[-1])
print(name[1:3]) #切片：【开始：结束】取左不取右
print(name[-3:-1]) #切片：【开始：结束】取左不取右 从右往左数是-3 -> -1

print(name[0:6:3]) #【开始：结束:步长】
 
print(name[::-1]) #【开始：结束:步长】 反转字符串

""" 
    08
    字符串拼接 +
    字符串格式化 format()
"""
a = "我爱你"+"中国"
print(a)

a = "我爱你"
b = "中国"
print(a+b)

f = ",".join((a,b))
print(f)

s = "名字:{} \n年龄:{} \n爱好:{}".format("蔡徐坤","18","唱跳rap篮球")
s2 = "名字:{1} \n年龄:{0} \n爱好:{2}"
s3 = s2.format("蔡徐坤","18","唱跳rap篮球")
print(s)
print(s3)

"""  
    09
    project
    
"""