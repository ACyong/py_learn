def fry_egg():
    print("打开天然气！")
    print("开始煎鸡蛋！")
    try:
        n = int(input("请输入蛋的个数")) # 肯触发异常
        print("完成煎蛋！， 共煎了%d个鸡蛋" % n)
    finally:
        print("关闭天然气！")

fry_egg()