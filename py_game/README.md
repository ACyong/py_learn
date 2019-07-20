# Pygame
tags:python3学习、逻辑训练、陶冶情操
>结合了嵩天教授的课程、《python和pygame游戏开发指南》、个人整理

## pygame 最小游戏框架

```
import sys  # 1、引入pygame 和sys 模块
import pygame

pygame.init()  # 2、初始化init() 及设置
screen = pygame.display.set_mode((480, 700))  # 3、设置游戏窗口大小及标题
pygame.display.set_caption("Hello World!")

# 4、游戏循环，进入游戏循环就以为着游戏的开始
while True:
    # 5、获取事件并逐类响应
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # 卸载pygame 所有模块
            sys.exit()
    pygame.display.update()  # 6、update 更新屏幕显示
```
pygame.display 模块专门用于创建、管理游戏窗口
pygame.display.set_mode(resolution(0, 0), flags=0, depth=0) 创建游戏窗口
>resolution 指定屏幕的宽和高，默认创建的窗口大小和屏幕大小一致
> flgs 参数指定屏幕的附加选项，例如是否全屏等等，默认不需要传递
>depth 参数表示颜色的位数，默认自动匹配
**注：必须使用变量记录set_mode方法的返回窗口对象，因为：后续所有的图像绘制都基于这个返回结果**

## wall ball version 1

功能：小球在游戏窗口中自由移动，撞到窗口边缘，反弹回来
小球下载地址：[https://github.com/ACyong/pygame/blob/master/wall_ball/PYG02-ball.gif](https://github.com/ACyong/pygame/blob/master/wall_ball/PYG02-ball.gif)
```
import sys
import pygame

pygame.init()
size = width, height = 600, 400  # 设置游戏窗口大小，从右向左分别是序列赋值和元组赋值
speed = [1, 1]  # 设置初始速度
BLACK = 0, 0, 0  # 设置背景颜色为黑色
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wall Ball")
ball = pygame.image.load("PYG02-ball.gif")  # 加载小球图片
ballrect = ball.get_rect()  # 获得小球对象的矩形对象

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])  # 让小球开始移动
    # 边缘检测
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(BLACK)  # 背景填充
    screen.blit(ball, ballrect)  # 绘制小球图像到矩形对象上
    pygame.display.update()
```
&emsp;&emsp;使用pygame.image.load("图像路径") 方法加载图片，返回pygame 使用内部定义的Surface 对象表示载入的图像，对象中 .get_rect() 方法返回一个覆盖图像的矩形Rect 对象，在游戏中所有可见的元素都是以矩形区域来展现位置的，Rect 对象有一些重要的属性，如：top、botton、left、right、width=right-left、height=bottom-top。也可以不用Surface 对象来得到举行区域，用pygame.Reck 这个类来描述矩形区域，需要四个参数来确定(x, y, width, height)，如：rect = pygame.Rect(100, 200, 150, 180)，声明的矩形对象左上角x轴：100、左上角y轴：200、宽：150、高：180。<br/>
&emsp;&emsp;使用Rect.move(x, y)方法, 使矩形移动一个偏移量(x, y)，即在横轴方向移动x 像素，纵轴方向移动y 像素，xy 为整数。<br/>
&emsp;&emsp;使用screen.fill(color)方法，显示窗口背景填充color 颜色，采用RGB色彩体系，本例由于小球不断运动，运动后原有位置将默认填充白色，因此需要不断刷新背景色。<br/>
&emsp;&emsp;使用screen.blit(src, dest)方法，将一个图像绘制在另一个图像上，即将src 绘制到dest位置上，本例是将小球绘制到Rect 对象上。


