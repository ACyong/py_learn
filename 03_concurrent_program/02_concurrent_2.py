import time
from concurrent.futures.process import ProcessPoolExecutor

t0 = time.time()


def return_future_result(message1, message2):
    s = 0
    for i in range(50000000):
        s *= i
    return message1, message2


def main():
    with ProcessPoolExecutor(max_workers=3) as pool:  # 创建一个最大可容纳3个task的进程池
        # 往进程池里面加入一个task
        future1 = pool.submit(
            return_future_result, message1="hello", message2='111')
        # 往进程池里面加入一个task
        future2 = pool.submit(
            return_future_result, message2="world", message1='222')

        print(future1.done())  # 判断task1是否结束
        print(future2.done())  # 判断task2是否结束
        print(future1.result())  # 查看task1返回的结果
        print(future2.result())  # 查看task2返回的结果
        print(future1.done())  # 判断task1是否结束
        print(future2.done())  # 判断task2是否结束

        t1 = time.time()
        print(f"total time consumed: {(t1-t0):{2}.{5}}")


if __name__ == '__main__':
    main()
