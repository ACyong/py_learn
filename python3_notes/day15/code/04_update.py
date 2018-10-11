import sys

find_str = sys.argv[1]
replase_str = sys.argv[2]

f = open("data2.txt", 'r')
f_new = open("data3.txt", "w")

for line in f:
    if find_str in line:
        line = line.replace(find_str, replase_str)
    f_new.write(line)

f.close()
f_new.close()


