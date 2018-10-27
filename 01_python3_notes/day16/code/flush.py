import time

f = open("flush.txt", 'w')
f.write("您好！")
f.flush()
time.sleep(60)

f.close()