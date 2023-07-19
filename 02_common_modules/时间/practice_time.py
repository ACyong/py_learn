import time

t = time.time()
# 1. 原始时间数据
print(t)

# 2. 秒级时间戳
print(int(t))

# 3. 毫秒级时间戳
print(int(round(t * 1000)))

# 4. 毫秒级时间戳, 基于 lambda
now_time = lambda: int(round(t * 1000))
print(now_time())

# 5. 打印当前时间
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(current_time)
