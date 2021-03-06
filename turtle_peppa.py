# -*- coding: utf-8 -*-
# 绘制小猪佩奇

import turtle

# 绘制鼻子
def nose(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-30)
    turtle.begin_fill()
    a = 0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a = a + 0.08
            turtle.left(3)
            turtle.forward(a)
        else:
            a = a - 0.08
            turtle.left(3)
            turtle.forward(a)
    turtle.end_fill()

    turtle.penup()
    turtle.setheading(90)
    turtle.forward(25)
    turtle.setheading(0)
    turtle.forward(10)
    turtle.pendown()
    turtle.pencolor(255, 155, 192)
    turtle.setheading(10)
    turtle.begin_fill()
    turtle.circle(5, 360)
    turtle.color(160, 82, 45)
    turtle.end_fill()

    turtle.penup()
    turtle.setheading(0)
    turtle.forward(20)
    turtle.pendown()
    turtle.pencolor(255, 155, 192)
    turtle.setheading(10)
    turtle.begin_fill()
    turtle.circle(5, 360)
    turtle.color(160, 82, 45)
    turtle.end_fill()


# 绘制头部
def head(x, y):
    turtle.color((255, 155, 192), 'pink')
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(180)
    turtle.circle(300, -30)
    turtle.circle(100, -60)
    turtle.circle(80, -100)
    turtle.circle(150, -20)
    turtle.circle(60, -95)
    turtle.setheading(161)
    turtle.circle(-300, 15)
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    turtle.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a = a + 0.08
            turtle.left(3)
            turtle.forward(a)
        else:
            a = a - 0.08
            turtle.left(3)
            turtle.forward(a)
    turtle.end_fill()



# 绘制耳朵
def ears(x, y):
    turtle.color((255, 155, 192), 'pink')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(100)
    turtle.circle(-50, 50)
    turtle.circle(-10, 120)
    turtle.circle(-50, 54)
    turtle.end_fill()

    turtle.penup()
    turtle.setheading(90)
    turtle.forward(-12)
    turtle.setheading(0)
    turtle.forward(30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(100)
    turtle.circle(-50, 50)
    turtle.circle(-10, 120)
    turtle.circle(-50, 56)
    turtle.end_fill()



# 绘制眼睛
def eyes(x, y):
    turtle.color((255, 155, 192), 'white')
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(-20)
    turtle.setheading(0)
    turtle.forward(-95)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15, 360)
    turtle.end_fill()

    turtle.color('black')
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(12)
    turtle.setheading(0)
    turtle.forward(-3)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

    turtle.color((255, 155, 192), 'white')
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(-25)
    turtle.setheading(0)
    turtle.forward(40)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15, 360)
    turtle.end_fill()

    turtle.color('black')
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(12)
    turtle.setheading(0)
    turtle.forward(-3)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()



# 绘制腮
def cheek(x, y):
    turtle.color((255, 155, 192))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()



# 绘制嘴
def mouth(x, y):
    turtle.color(239, 69, 19)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-80)
    turtle.circle(30, 40)
    turtle.circle(40, 80)



# 绘制身体
def body(x, y):
    turtle.color('red', (255, 99, 71))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(-130)
    turtle.circle(100, 10)
    turtle.circle(300, 30)
    turtle.setheading(0)
    turtle.forward(230)
    turtle.setheading(90)
    turtle.circle(300, 30)
    turtle.circle(100, 3)
    turtle.color((255, 155, 192), (255, 100, 100))
    turtle.setheading(-135)
    turtle.circle(-80, 63)
    turtle.circle(-150, 24)
    turtle.end_fill()



# 绘制手
def hands(x, y):
    turtle.color((255, 155, 192))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-160)
    turtle.circle(300, 15)
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(15)
    turtle.setheading(0)
    turtle.forward(0)
    turtle.pendown()
    turtle.setheading(-10)
    turtle.circle(-20, 90)

    turtle.penup()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.setheading(0)
    turtle.forward(237)
    turtle.pendown()
    turtle.setheading(-20)
    turtle.circle(-300, 15)
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(20)
    turtle.setheading(0)
    turtle.forward(0)
    turtle.pendown()
    turtle.setheading(-170)
    turtle.circle(20, 90)



# 绘制脚
def foot(x, y):
    turtle.pensize(10)
    turtle.color((240, 128, 128))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(40)
    turtle.setheading(-180)
    turtle.color('black')
    turtle.pensize(15)
    turtle.forward(20)
    
    turtle.pensize(10)
    turtle.color((240, 128, 128))
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(40)
    turtle.setheading(0)
    turtle.forward(90)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(40)
    turtle.setheading(-180)
    turtle.color('black')
    turtle.pensize(15)
    turtle.forward(20)



# 绘制尾巴
def tail(x, y):
    turtle.pensize(4)
    turtle.color((255, 155, 192))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(70, 20)
    turtle.circle(10, 330)
    turtle.circle(70, 30)



# 参数设置
def setting():
    turtle.pensize(4)
    turtle.hideturtle()
    turtle.colormode(255)
    turtle.color((255, 155, 192), 'pink')
    turtle.setup(840, 500)
    turtle.speed(10)



def main():
    # 画布、画笔设置
    setting()
    # 鼻子
    nose(-100, 100)
    # 头
    head(-69, 167)
    # 耳朵
    ears(0, 160)
    # 眼睛
    eyes(0, 140)
    # 腮
    cheek(80, 10)
    # 嘴
    mouth(-20, 30)
    # 身体
    body(-32, -8)
    # 手
    hands(-56, -45)
    # 脚
    foot(2, -177)
    # 尾巴
    tail(148, -155)
    # 结束
    turtle.done()
    
    # main()

main()



