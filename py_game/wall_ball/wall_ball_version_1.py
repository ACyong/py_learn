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









