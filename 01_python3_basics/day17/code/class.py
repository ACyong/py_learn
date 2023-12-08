class Dog(object):
    """c创建一个类叫 Dog"""
    pass


dog1 = Dog()  # 类名() <<===== 构造函数，用来创建对象（实例）
dog1.kinds = "京巴"  # 为dog1 绑定的对象添加kinds实例变量
dog1.color = "白色"

dog2 = Dog()  # dog2 绑定一个Dog类型的对象
dog2.kinds = "哈士奇"
dog2.color = "黑白相间"

print("dog1.kinds = ", dog1.kinds)  # 访问dog1的实例变量kinds
print("dog2.kinds = ", dog2.kinds)  # 访问dog1的实例变量kinds

print("dog2.color = ", dog2.color)
del dog2.color
print("dog2.color = ", dog2.color)







