import hashlib
from uuid import uuid4


def mymd5(password):
    m = hashlib.md5()
    m.update(password.encode('utf8'))
    pwd = m.hexdigest()
    return pwd

def myuuid():
    u=uuid4()
    m = hashlib.md5()
    m.update(u.bytes)
    return m.hexdigest()

