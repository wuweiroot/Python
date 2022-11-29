#!/usr/bin/env python
# coding: utf-8

# In[7]:


# -*- coding: UTF-8 -*-
'''
代码用途 ：情人节表白
作者     ：阿黎逸阳
博客     :  https://blog.csdn.net/qq_32532663/article/details/106176609
'''
import os
import pygame
import turtle as t 

#播放音乐
print('播放音乐')
pygame.mixer.init()
#pygame.mixer.music.load(r"F:\公众号\520\赵海洋 - 《瞬间的永恒》夜色钢琴曲.mp3") 
pygame.mixer.music.load(r"E:\\culture\\Professional\\Project\\Python\48.永恒心动\\赵海洋 - 《瞬间的永恒》夜色钢琴曲.mp3") 
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play(1, 10)


t.title('送给吕美欣爱心的代码')
t.speed(10)
#t.screensize(1000, 800)
t.setup(startx=0, starty = 0, width=800, height = 600)
t.hideturtle()
print('画爱心')
#画爱心
def heart(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('red')
    t.setheading(50)
    t.circle( -5, 180) 
    t.circle( -45, 12) 
    t.setheading(130) 
    t.circle( -45, 12) 
    t.circle( -5, 180)
heart(-30, 155)
heart(-220, 145)
heart(-210, 60)
heart(-100, 100)
heart(-20, 20)
heart(-70, 130)
heart(-140, -20)
heart(30, 100)
heart(-60, -20)
heart(10, 60)
heart(-100, -70)
heart(20, 145)
heart(-140, -20)
heart(-130, 130)
heart(-180, 20)
heart(-170, 155)
heart(-230, 100)
def write_mes(x, y, size, ss):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor('black')
    t.write(ss, font=('Times New Roman', size, 'normal'))
#画红心
print('画红心')
def heart_fill(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('pink', 'pink')
    t.begin_fill()
    t.setheading(50)
    t.circle( -5, 180) 
    t.circle( -45, 12) 
    t.setheading(130) 
    t.circle( -45, 12) 
    t.circle( -5, 180)
    t.end_fill()
x = 90
y = 110
#右边爱心
write_mes(x, y, 11, '喜 欢 你 的 每 一 天')
heart_fill(-100, 100)
heart_fill(-70, 130)
heart_fill(-30, 155)
heart_fill(20, 145)
heart_fill(30, 100)
write_mes(x, y-30, 11, '爱 意 不 曾 退 减')
heart_fill(10, 60)
heart_fill(-20, 20)
heart_fill(-60, -20)
heart_fill(-100, -70)
#左边爱心
write_mes(x, y-30*2, 11, '时 光 不 曾 走 远')
heart_fill(-140, -20)
heart_fill(-180, 20)
heart_fill(-210, 60)
heart_fill(-230, 100)
write_mes(x, y-30*3, 11, '幸 福 延 续 到 明 天')
heart_fill(-220, 145)
heart_fill(-170, 155)
heart_fill(-130, 130)
write_mes(x, y-30*4, 11, '永 远 不 说 再 见')
t.speed(15)
print('画心动线')
def heart_bit():
    #画心动线
    t.penup()
    t.goto(-170, 40)
    t.pendown()
    t.pencolor('red')
    t.setheading(0)
    t.pensize(2)
    t.forward(10)
    #第一个小波浪
    t.setheading(45)
    t.circle(50, 10)
    t.setheading(0)
    t.circle(-3,90)
    t.circle(50, 5)
    #横线
    t.setheading(0)
    t.forward(10)
    #第一个下尖峰
    t.setheading(-80)
    t.forward(7)
    t.setheading(70)
    t.forward(25)
    t.setheading(-85)
    t.forward(29)
    t.setheading(70)
    t.forward(13)
    t.setheading(0)
    t.forward(15)

    #画心
    t.setheading(150)
    t.circle(-20, 40)
    t.circle(-10, 170)
    t.setheading(70)
    t.circle(-10, 170)
    t.circle(-20, 40)
    t.setheading(0)
    t.forward(15)
    #2
    t.setheading(-80)
    t.forward(7)
    t.setheading(70)
    t.forward(25)
    t.setheading(-85)
    t.forward(29)
    t.setheading(70)
    t.forward(13)
    t.setheading(0)
    t.forward(15)
    t.setheading(0)
    t.forward(10)
    t.setheading(45)
    t.circle(50, 10)
    t.setheading(0)
    t.circle(-3,90)
    t.circle(50, 5)
    t.setheading(0)
    t.forward(10)
def write_name(x, y, size, ss):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor('black')
    t.write(ss, font=('Times New Roman', size, 'normal'))
def undo_back():
    t.undo()
    t.undo()
    t.undo()
    t.undo()
    t.undo()
    t.undo()
    t.undo()
    t.undo()
    t.undo()
    t.undo()
def undo_back2():
    t.undo()
    t.undo()
def name_heart_bit():
    #写两个人的姓名(需替换成真实姓名)
    write_name(-180, 70, 11, '赵许龙')
    write_name(-180, 70, 11, '赵许龙')
    write_name(-180, 70, 11, '赵许龙')
    heart_bit()
    write_name(-60, 70, 11, '吕美欣')
    write_name(-60, 70, 11, '吕美欣')
    write_name(-60, 70, 11, '吕美欣')
    write_name(-60, 70, 11, '吕美欣')
    write_name(-60, 70, 11, '吕美欣')
    undo_back()
    undo_back()
    undo_back()
    undo_back()
    undo_back()
    undo_back()
    undo_back()
    undo_back()
    undo_back()
    undo_back2()
while 1:
    name_heart_bit()


# In[ ]:




