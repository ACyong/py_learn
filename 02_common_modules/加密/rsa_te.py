import json

import rsa
import base64


class Rsacrypt:
    def __init__(self):
        self.__pubkey = None
        self.__prikey = None

    # 生成公钥和私钥
    def genKey(self, size):
        self.__pubkey, self.__prikey = rsa.newkeys(size)

    # 获取公钥字符串
    def getPubKey(self):
        pub = self.__pubkey.save_pkcs1()
        return pub.decode('utf-8')

    # 获取私钥字符串
    def getPriKey(self):
        pri = self.__prikey.save_pkcs1()
        return pri.decode('utf-8')

    # 设置公钥
    def setPubKey(self, s_pub):
        self.__pubkey = rsa.PublicKey.load_pkcs1(s_pub.encode('utf-8'))

    # 设置私钥
    def setPrikey(self, s_pri):
        self.__prikey = rsa.PrivateKey.load_pkcs1(s_pri.encode('utf-8'))

    # 公钥加密
    def encrypt(self, text):
        ciphertext = rsa.encrypt(text.encode(), self.__pubkey)
        return base64.b64encode(ciphertext).decode('utf-8')

    # 私钥解密
    def decrypt(self, text):
        decrypt_text = rsa.decrypt(base64.b64decode(text.encode('utf-8')), self.__prikey)
        return decrypt_text.decode()

    # 私钥签名
    def sign_by_private_key(self, data):
        signature = rsa.sign(data, priv_key=self.__prikey, hash_method='MD5')
        return base64.b64encode(signature)

    # 公钥验签
    def verify_by_public_key(self, message, signature):
        signature = base64.b64decode(signature)
        return rsa.verify(message, signature, self.__pubkey)


if __name__ == '__main__':
    rsacrypt = Rsacrypt()
    rsacrypt.genKey(1024)

    print(rsacrypt.getPubKey())
    print(rsacrypt.getPriKey())

    data_list = {
        "customerIds": ['001', '002'],
    }
    message = json.dumps(data_list)
    encryptedData = rsacrypt.encrypt(message)
    print("数据加密结果：>>> ")
    print(encryptedData)

    decryptedData = rsacrypt.decrypt(encryptedData)
    print("数据解密结果：>>> ")
    print(decryptedData)

    signature = rsacrypt.sign_by_private_key(message.encode('utf-8'))
    print("签名结果：>>> ")
    print(signature)

    verify = rsacrypt.verify_by_public_key(message.encode('utf-8'), signature)
    print("验签结果：>>> ")
    print(verify)
