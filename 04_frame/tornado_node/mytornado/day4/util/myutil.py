import hashlib


def mymd5(password):
    m = hashlib.md5()
    m.update(password.encode('utf8'))
    pwd = m.hexdigest()
    return pwd