f = open("data.bin", "r+b")
f.seek(15)
f.write(b'ABCD')
f.close()