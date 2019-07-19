## 0.数据库介绍：

- 数据的存储位置：

1. 内存：存取速度快，不能长期保存，容量小
2. 外存储器：存取速度慢，能长期保存数据，容量大

- 外存储器的存储形式：文件存储，数据库存储
```
文件管理阶段（word，excel，音频，视频）
    优点：数据可以长期保存
         存储容量大
         使用比较简单

    缺点：数据冗余大，数据一致性差，完整性维持困难
         查找修改不方便

数据库管理阶段
    优点：数据可以长期保存
         存储容量大
         数据组织结构好
         冗余度小
         容易扩充
         方便程序自动处理
         查找修改效率高

    缺点：难度和专业度相对文件要求较高
```

- 数据库的几个概念：
```
数据：能够输入到计算机并被识别和处理的信息集合
数据库：是按照数据结构组织、存储和管理的仓库，是在数据库管理系统管理和控制下存放在一定介质上的数据集合
数据库管理系统：管理数据库的软件，用于按照一定的方法建立，使用，维护数据库结构内容
数据库系统：由数据库，数据库管理系统，开发工具等共同构成的一个集合概念
```
---

## 1.数据库分类：

- 关系型数据库
```
采用关系模型来组织数据库的结构的数据库, 如：
Oracle  DB2  SQLServer  MySql  等数据库
SqLite(python提供标准化模块，小巧，多用于嵌入式设备)

优点：容易理解
     使用方便，通过sql语句操作，而sql语句是非常成熟的
     易于维护，完整性好，数据一致性高
     通用化程度高，使用SQL语句，技术成熟，可以进行外联操作

缺点：无法很好满足高并发的需求，每次数据操作都需要执行sql语句，对sql进行解析，导致高并发下读写性能不足
     针对海量数据的爆发，性能不足，因为关系型数据库每一步操作几乎都需要加锁
     扩展型不足，当数据量达到一定程度的时候不方便扩展
```

- 非关系型数据库（NoSQL ---> not only sql）
```
优点：高并发下，读写能力强
     支持分布式存储，易于拓展
     弱化数据结构，让数据结构简单

缺点：缺少join 等复杂的操作
     通用性差
     结构灵活也需要更灵活的操作，容易混乱，没有标准的语句
```
> 面试要求：能够描述关系型数据库和非关系型数据库的优缺点

- Nosql适用情况
```
1、数据模型简单
2、对数据一致性要求低
3、对并发处理要求高
4、对数据库扩展由需求
5、可以比较方便的以键值方式映射数据值
```

- 非关系型数据库分类
```
键值存储数据库
    Redis， Oracle BDB， Tokyo

文档型数据库（是键值型数据库的升级版）
    MongoDB， CouchDB

列存储数据库
    HBase

图形数据库
```
> 要求：知道非关系型数据库分为哪几类，mongodb是哪类的

- MongoDB和关系型数据库的概念对比
```
mysql          mongodb        含义
database       database       数据库
table          collection     表 / 集合
row            document       行、记录 / 文档
column         field          列、字段 / 域
index          index          索引
primary key    primary key    主键

在mongo中：数据库包含多个集合
          集合包含多条文档
          文档中标明域及域对应的值
```
---

## 2.MongoDB
- 介绍：
```
1、分布式的Nosql
2、由C++编写
3、是文档型数据库，支持的数据格式松散，类似于字典（Bson）
4、最类似于关系型数据库的非关系数据库，应用广泛
```

- 特点：
```
1、高性能，易部署，存储方便
2、支持的查询操作相对其他Nosql要丰富
3、支持的Bson数据格式包含数据类型比较全面
4、支持众多语言的编程接口（ruby、python、c++、c#、php）
5、有很好的扩展性
```
---

## 3.MongoDB 安装

- Ubuntu 系统：
```
sudo apt-get install mysql-server   # mysql 安装
sodo apt-get updata                 # 更新软件源
sodo apt-get install mongodb        # 安装mongodb

默认安装路径：/var/lib/mongodb
```

- 手动安装(Linux)：
```
1、下载对应版本的mongodb包
2、将压缩包放到某个目录下（/opt  或  /usr/local）
3、解压压缩包：tar -xvf mongo-linux-x86......-3.4.10.tgz
4、解压后将解压文件夹中的bin目录添加到环境变量，bin中是mongo的相关命令
5、cd /ect       sudo vi rc.local
    或        
   cd /ect       sudo vi bash.bashrc

   在 exit 0 前加入
   PATH=$PATH:/绝对路径/bin
   export PATH
6、reboot 重启
```

- Mac 系统：（推荐使用 homebrew 安装）
```
brew install mongodb
```
---

## 4.启动mongodb 服务

- Linux 系统
```
mongod --dbpath /XX/YY    指定数据库路径
       --port 端口号       指定占用的端口（默认端口为 27017 端口）
```

- Mac 系统
```
brew services start mongodb    # 启动
brew services stop mongodb     # 停止
brew services restart mongodb  # 重启
```

- 启动mongo shell
```
mongo    进入mongo shell 模式
quit()   退出mongo shell
```
> 注：mongo shell下支持JavaScript代码

- 数据库的备份和恢复（在终端中输入）
```
备份：mongodump -h dbhost -d dbname -o dbdir
实例：mongodump -h 127.0.0.1 -d stu -o python

恢复：mongorestore -h 127.0.0.1:27017 -d dbname <path>
实例：mongorestore -h 127.0.0.1:27017 -d student python/stu
```

- 数据库的检测
```
mongostat
insert每秒插入次数 query查找 update更新 delete删除

mongotop
检测每个数据库的读写时长
```
---

## 5.库的管理

- 数据库的创建
```
use databasename

实例：创建一个名字为stu的数据库
> use stu
```
> use 并不会直接创建出数据库，当向数据库中插入数据时数据库才会被真正创建
, use 同时还有在多个数据库直接切换的功能

- 查看数据库：
```
实例：显示当前系统中的数据库
> show dbs
```
> db：是一个全局量，表示当前正在use的数据库。如果没有进行任何use操作，则表示test（系统自动创建）

- 数据库命名规则
```
数据库的名字可以是满足以下条件的任意 utf-8 字符串
    1、不能是空字符串
    2、不能含有：空格(' ')  点('.')  '/'  '\'  '\0'
    3、应全部小写
    4、不要超过64字节
    5、不要使用 admin local config 这三个名字（系统已经定义）
```
> admin：用来存储用户和权限的, local：不会被复制，只能用于本台服务器访问, config：分片处理的时候，保存分片信息

- 删除数据库
```
实例：删除db所代表的数据库
> db.dropDatabase()
```
---

## 6.集合的管理

- 创建集合1
```
db.createCollection('集合名称')

实例：创建一个名字为class的空集合
> use stu
> db.createCollection('class')

命名规则：
    1、不能为空字符串
    2、不能含有'\0'
    3、不能以'system.'开头。(是系统的保留集合前缀)
    4、集合名称不要和保留字重名，不要包含'$'
```

- 创建集合2:
```
当向一个集合中存入一条文档，则集合会被自动创建，这是更加常用的方法
db.collect_name.insert()

实例：自动创建class 这个集合
> db.class.insert({'name':'lucy', 'age':15, 'sex':'w'})
```

- 查看当前`use`的数据库中的所有集合
```
> show collections/tables
```

- 修改集合名称
```
db.collectionName.renameCollection(newName)

实例：
> db.class.renameCollection('class1')
```

- 删除集合
```
db.collectionName.drop()

实例：删除class1集合
> db.class1.drop()
```
---

## 7.文档介绍
> 集合中包含多个文档，集合实际就是文档的集合

- 同一集合中文档的设计原则：
```
同一类文档应当集中存储，便于管理
集合中可以使用不同格式的文档
集合中集中存储格式类似的文档，可以提高访问效率
```

- 文档中对键的要求
```
1、一般来说是 utf-8格式的字符串
2、键中不能有'\0'，不能是空字符
3、通常不会用 . 和 $
4、一般以_开头的键都是系统的保留键，所以尽量不用下划线开头
```

- 文档中值的要求：
```
mongodb 中值是bson格式的数据是json格式进化版，支持的数据类型如下：
字符串         utf-8 格式的字符串均为合法
整型           32位整型
布尔           真 假
浮点型         存储小数
Arrays        列表或数组
Timestamp     时间戳
Object        内部文档
Null          空值
Symbol        同字符串，多用于存储特殊字符
Date          日期时间
ObjectId      objectid字串
Binary data   二进制数据
code          代码，js代码
regex         正则表达式
```
---

## 8.文档的增

- 插入文档1
```
db.collectionName.insert()
注意在插入文档的时候，键可以不加引号

插入多条数据
db.collectionName.insert([{}, {}, {}, {}])

实例：
> db.city.insert([{中国:'北京'}, {美国:'华盛顿'}, {德国:'柏林'}])
> db.city.find()
> db.city.drop()
```
> 如果插入时自己设置了_id那么系统则会使用设置的_id值，但是_id仍然为主键，不能重复

- 插入文档2
```
db.collectionName.save()

1、如果不加_id 进行插入效果同insert()
2、如果加_id 进行操作，如果_id值不存在则正常插入，如果存在则修改原文档
3、save() 不能同时插入多条数据
```

- 关于null
```
表示给某个域赋值为null
db.class2.insert({name:'Levi', age:null, date:'2017-9-1'})

表示某个域不存在的情况
db.class2.find({sex:null}, {_id:0})
```

- 时间：
```
date 类型
存储 ISODate('2018-02-27 11:45:36')

获取当前时间: new Date()
实例：插入数据包含当前时间
db.class2.insert({name:'Alex', age:13, date:new Date()})
```

- 练习1:
```
1、创建一个名为stu 的数据库
> use stu

2、创建一个名为class 的集合，插入几条记录，域为：name，age，sex，weight，course
> db.class.insert([
    {'name':'lucy', 'age':15, 'sex':'w', weight:85, course:['English', 'Chinese', 'Math', 'music']},
    {'name':'lisi', 'age':11, 'sex':'m', weight:48, course:['Chinese', 'Math', 'music']},
    {'name':'wang', 'age':18, 'sex':'w', weight:100, course:['English', 'Chinese']},
    {'name':'zhang', 'age':10, 'sex':'m', weight:60, course:['Chinese', 'Math']},
    {'name':'ming', 'age':12, 'sex':'w', weight:79, course:['English', 'Chinese', 'music']}
    ])

3、修改集合名class 为class1
> db.class.renameCollection('class1')
```
---

## 9.文档的查

- 格式：
```
db.collectionName.find(query, {filed:0/1})
db.collectionName.findOne(query, {field:0/1})
```

- 功能：
```
find 查找所有符合条件的文档，不加参数默认查找所有文档
findOne 查找第一条符合条件的文档
```

- 参数：
```
query：表示查找条件。相当于mysql中的where语句
field声明：展示指定域，其中0表示不显示该域，1表示显示该域。相当于mysql 中select 和from 间的内容。
```

> 两个参数均以{} 类似字典的方式传入, 如果是空字典, 则与不写一样

> 当设置某几个域值为1，则其他域值默认为0，如：db.class1.find({}, {name:1, age:1})。当设置某几个域值为0，则其他域值默认为1，_id 始终默认为1，如果不想显示_id 则需要手动设置为0。_id 设置为0时，其他的域可以设置为1；除_id 外其他的普通域0和1不能混合设置

- 返回值：
```
返回查找到的结果

实例：
> db.class1.find({name:'lucy'})

返回值：
{ "_id" : ObjectId("5a911a5fcb8d853e775289b2"), "name" : "lucy", "age" : 15, "sex" : "w" }

24个十六进制的数用于系统自动生成的_id的（key）:
    前8位文档创建时间
    6位 机器ID
    4位 进程ID
    6位 计数器
```
```
实例：
查找所有数据记录
> db.class1.find() --> select * from class1;

查找第一条符合条件的记录
> db.class1.findOne() --> select * from class1 where limit=1;

查找一个name为Lei的同学
> db.class1.findOne({name:'Lei'}, {_id:0}) --> select * from class1 where name='Lei' limit = 1;
```

- 使用集合定位方法查找：
```
> db.getCollection('collectionName').find() --> db.collectionName.find()
```
---

### 1.比较运算符：

> 字符串也可以比较大小，按ascii码值逐个比较

- $eq  等于
```
实例：查找age等于18的同学
> db.class1.find({age:{$eq:18}}, {_id:0}) --> db.class1.find({age:18}, {_id:0})
```

- $lt  小于
```
实例：查找age小于18的同学
> db.class1.find({age:{$lt:18}}, {_id:0})
```

- $lte 小于等于
```
实例：查找age小于等于18的同学
> db.class1.find({age:{$lte:18}}, {_id:0})
```

- $gt  大于
```
实例：查找age大于17的同学
> db.class1.find({age:{$gt:17}}, {_id:0})
```

- $gte 大于等于
```
实例：查找age大于等于17的同学
> db.class1.find({age:{$gte:17}}, {_id:0})
```

- $ne 不等于
```
实例：查找age不于等于18的同学
> db.class1.find({age:{$ne:18}}, {_id:0})
```

- $in 是否包含
```
实例：查找age包含10，11，17的同学
> db.class1.find({age:{$in:[10, 11, 17]}}, 
{_id:0})
```

- $nin 是否不包含
```
实例：查找age不包含10，11，17的同学
> db.class1.find({age:{$nin:[10, 11, 17]}}, 
{_id:0})
```
---

### 2.逻辑运算符

- $and 逻辑与（逗号隔开的即为and关系）
```
实例：查找age等于17，name是wang的同学
> db.class1.find({$and:[{age:17}, {name:'wang'}]}, {_id:0})

更常用：
> db.class1.find({age:17, name:'wang'}, {_id:0})
```
```
查找age大于15，小于18的同学
> db.class1.find({$and:[{age:{$gt:15}}, {age:{$lt:18}}]}, {_id:0})

更常用：
> db.class1.find({age:{$gt:15, $lt:18}}, {_id:0})
```

- $or 逻辑与
```
实例：查找age小于18或weight等于85的同学
> db.class1.find({$or:[{age:{$lt:18}}, {weight:85}]}, {_id:0})
```

- $not 逻辑非
```
实例：用$not 查找age不小于18的同学
> db.class1.find({age:{$not:{$lt:18}}}, {_id:0})
```

- $nor 既不也不
```
实例：查找age既不小于18也不要name为zhang的同学
> db.class1.find({$nor:[{age:{$lt:18}}, {name:'zhang'}]}, {_id:0})
```
---

### 3.混合查找实例
```
实例：name = 'Jame' and (age = 12 or age = 13)
> db.class1.find({name:'Jame', $or:[{age:12}, {age:13}]}, {_id:0})

实例：age > 13 or (name = 'wang' and sex = 'm')
> db.class1.find({$or:[{age:{$gt:13}}, {name:'wang', sex:'m'}]})
```
---

### 4.数组查找  (course的值是一个数组)
```
实例：筛选course 数组中包含'chinese' 的文档
> db.class3.find({course:'Chinese'}, {_id:0})
```

- $all
```
实例：筛选course 数组中包含$all:{'', ''} 子集的文档
> db.class3.find({course:{$all:['Chinese', 'English']}}, {_id:0})
```

- $size
```
实例：筛选course 数组中包含2 个元素的文档
> db.class3.find({course:{$size:2}}, {_id:0})
```
---

### 5.数组显示  (course的值是一个数组)

- $slice 可以和0 或1 搭配
```
实例：显示数组中前两项
> db.class3.find({}, {_id:0, course:{$slice:2}})

实例：显示数组中跳过第一项 显示后面两项
> db.class3.find({}, {_id:0, course:{$slice:[1, 2]}})
```
---

### 6.其他查找命令

- $exits 
```
实例：查找某个域存在与否的文档，true表示存在，false表示不存在
> db.class1.find({weight:{$exists:true}}, {_id:0})
```
  
- $mod 
```
实例：查找某个域的值，匹配给定的除数和余数
> db.class1.find({age:{$mod:[3, 1]}}, {_id:0})
```

- $type 
```
实例：查找某个域是指定类型的文档
> db.class3.find({course:{$type:2}}, {_id:0})
```
> mongo 中每种数据类型对应一个整数
---

### 7.和查找结果相关的函数

- distinct(colName)
```
实例：查看class集合中所有文档age域包含哪些值
> db.class1.distinct('age')
```

- pretty() 
```
实例：格式化显示结果
> db.class1.find().pretty()
```

- limit(num) 
```
实例：显示查找结果的前num项
> db.class1.find({}, {_id:0}).limit(3)
```

- skip(num) 
```
实例：跳过前num条记录进行显示
> db.class1.find({}, {_id:0}).skip(2)
```

- count() 
```
实例：统计查询到的文档个数
> db.class1.find({}, {_id:0}).count()
```

- sort({}, {}, {}, .......) : 
```
实例：按照指定的域值进行排序（指定某个域的值如果是1表示升序、-1表示降序）
> db.class1.find({}, {_id:0}).sort({age:1})
```

- query 
> 结果调用函数是可以连续调用的
```
实例：查找年龄最小的三个文档
> db.class1.find({}, {_id:0}).sort({age:1}).limit(3)
```
---

## 10.文档的改

- 格式：
```
db.collectionName.update(query, update, upset, multi)
update tablename set.... where....
```

- 功能：更新文档数据

- 参数：
```
query  定位要更新的文档，相当于where用法同查找
update 将数据更新为什么，相当于set，update需要配合修改器使用，如果不使用修改器，就是替换文本，而不是更新某个字段

upset  是boolean值，默认为false，如果query存在修改，不存在则不做任何改变，如果设置为true，表示如果query的文档不存在则根据update插入一条新的文档，如果存在则修改

multi  是boolean值，默认为false，如果query匹配到多个，只修改第一个，如果设置为true，表示修改所有query的文档
```

### 1.修改器：
- $set：修改某一个或多个域的值，如果该域不存在则添加这个域
```
实例：将名为Han 的性别修改为女
> db.class1.update({name:'Han'}, {$set:{sex:'w'}})
```

- $inc 将某个域的值，增加或者是减少
```
实例：所有年龄小于20 的人年龄加3
> db.class1.update({age:{$lt:18}}, {$inc:{age:3}}, false, true)
```

- $mul 乘法修改器，将某个域的值乘以多少
```
实例：将第一个人的年龄乘以2
> db.class1.update({}, {$mul:{age:2}})
```

- $unset 删除某一个或多个域，域后面加什么数字无所谓
```
实例：将第一个人的性别删除
db.class1.update({}, {$unset:{sex:1}})
```

- $rename 修改域名
```
实例：将所有存在sex域的文档的sex域名改为gender
db.class1.update({sex:{$exists:true}}, {$rename:{'sex':'gender'}}, false, true)
```

- $min 若匹配到的文档的指定域的值小于给定值则不做任何修改，如果大于给定的值则修改为给定值
```
实例：将所有age大于20的改为20
db.class1.update({}, {$min:{age:20}}, false, true)
```

- $max 若匹配到的文档指定域的值大于给出的值则不做修改，如果小于给出的值则改为指定值
```
实例：将所有age小于17的改为17
db.class1.update({}, {$max:{age:17}}, false, true)
```
---

### 2.数组修改器
- $push 向数组中添加一项元素
```
实例：向数组course添加一个python
> db.class3.update({name:'wang'}, {$inc:{age:1}, $push:{course:'python'}})
```

- $pushAll 向数组中添加多项元素
```
实例：向数组score添加
> db.class3.update({name:'li'}, {$pushAll:{score:[100, 99]}})
```

$each
```
> db.class3.update({name:'li'}, {$push:{score:{$each:[100, 99]}}})
```

- $pull 从数组中删除一项
```
实例：删除score数组中的78
> db.class3.update({name:'li'}, {$pull:{score:88}})
```

- $pullAll 从数组中删除多项
```
db.class3.update({name:'li'}, {$pullAll:{score:[99, 100]}})
```

- $pop 从数组两侧弹出数据, 1 从右侧弹出， -1 从左侧弹出
```
db.class3.update({name:'li'}, {$pop:{score:1}})
```

- $addToSet 同push 但是不能有重复项
```
实例：用$addToSet更新可以避免重复，将它与$each组合起来，可以一次性添加多条（就算后添加的值已存在也没有关系）
> db.user.update({"name":"li"},{"$addToSet":{"course":{"$each":["singing","dancing"]}}})
```
---

## 11.文档的删

- 格式：
```
db.collectionName.remove(query, justOne)
```

- 功能：删除文档

- 参数：
```
query：  定位要删除的记录，类似mysql中where，具体写法同查找
justOne：赋一个布尔类型值，如果不写则表示删除所有符合query条件的文档，如果赋值为true或者1，表示只删除第一条符合query条件的文档
```
```
实例：
删除所有age 小于13 的文档
db.class1.remove({age:{$lt:13}})

实例：
删除第一条age 大于17 的文档
db.class1.remove({age:{$gt:17}}, true)

删除第一条文档
db.collectionName.remove({}, 1)

删除所有文档
db.collectionName.remove({})
```
---

## 12.练习：
1.创建一个数据名库字为 grade
```
use grade
```
2.数据库中创建集合名称为 class
```
db.createCollection('class')
```
3.向集合插入文档，格式结构为：name age sex hobby[画画，唱歌，跳舞，篮球，足球]
```
```
4.查找练习
```
查看班级所有学生的信息
db.class.find({}, {_id:0})

查看班级所有年龄为4 岁的学生信息
db.class.find({age:4}, {_id:0})

查看班级所有年龄大于4 岁的学生
db.class.find({age:{$gt:4}}, {_id:0})

查看班级所有年龄4-7 岁之间的学生
db.class.find({age:{$gte:4, $lte:7}}, {_id:0})

查看所有年龄大于4 岁的女同学
db.class.find({age:{$gt:4}, sex:'g'}, {_id:0})

查看所有小于4 岁或者大于7岁的学生
db.class.find({$or:[{age:{$lt:4}}, {age:{$gt:7}}]}, {_id:0})

查看年龄是4 岁或者6岁的学生
db.class.find({age:{$in:[4, 6]}}, {_id:0})

查看有两项爱好的学生
db.class.find({hobby:{$size:2}}, {_id:0})

查看喜欢画画的学生
db.class.find({hobby:'画画'}, {_id:0})

查看既喜欢画画有喜欢跳舞的学生
db.class.find({hobby:{$all:['画画', '跳舞']}}, {_id:0})

统计有三项爱好的学生人数
db.class.find({hobby:{$size:3}}, {_id:0}).count()

查看本班第二位学生信息
db.class.find({}, {_id:0}).skip(1).limit(1)

将学生按年龄升序，年龄相同按姓名升序排序
db.class.find({}, {_id:0}).sort({age:1, name:1})

统计学生兴趣都覆盖哪些范围
db.class.distinct('hobby')

删除所有年龄小于4和大于9的学生
db.remove({$or:[{age:{$lt:4}}, {age:{$gt:9}}]}, {_id=0})
```
---

## 13.内部文档操作

```
在文档中，某个域的值也是文档，把这个文档称为内部文档

db.class2.insert({book:{'title':'python黑客编程从入门到入狱', 'prince':45.8}})
db.class2.find({'book.title':'python黑客编程从入门到入狱'})
```

```
使用外层文档的域 点 的方法引用内部文档域的值时，必须加引号
db.class2.update({book:{$exists:true}}, {$set:{'book.prince':99}})
```

通过数组域名应用索引序号的方式，修改查找数组中具体某一项
实例：查找course第一项是Chinese的
db.class3.find({'course.0':'Chinese'},{_id:0})

修改name=li 的文档score数组中的一个数为76
db.class3.update({name:'li'}, {$set:{'score.0':76}})

- 引深：
```
db.class2.insert({name:'book message', book:[{title:'Python入门', price:46}, {title:'Html入门', price:47}, {title:'Java入门', price:48}]})

查询1: 数组包含项查询
db.class2.find({book:{title:'Python入门', price:46}}, {_id:0}).pretty()

查询2:
db.class2.find({'book.title':'Python入门', 'book.price':46}, {_id:0}).pretty()

查询3：出现问题
db.class2.find({'book.title':'Python入门', 'book.price':47}, {_id:0}).pretty()
```

- $elemMatch 操作符解决上面的问题, 专门用于查询数组中的元素是否满足指定条件:
```
db.class2.find({book:{$elemMatch:{title:'Python入门', price:47}}}).pretty()
```
---

## 14.练习：接上练习文档grade
```
1、将该班上名为小红的同学年龄变为8岁，兴趣爱好变为跳舞、画画
2、追加小明的兴趣爱好：唱歌
3、增加小王爱好：吹牛和打篮球
4、增加小李爱好：吹牛、唱歌，要保证不要和以前的重复
5、给该班所有同学都增加1岁
6、删除小明sex属性
7、删除小明爱好中的第一项
8、删除小红爱好中的画画
```
---

## 15.索引：
> 指的是建立指定键值所在文档中存储闻之的对应关系清单。使用索引进行查找可以方便快速查找，减少遍历，提高效率。如果不使用索引，往往进行大量扫描，效率低

- 创建索引：(过去的方法：createIndex()）
```
db.collection.ensureIndex()

实例：以name域创建索引
db.class1.ensureIndex({'name':1})  1 表示正向索引， -1 表示逆向索引
```

- 查看当前集合中的索引
```
db.class1.getIndexes()
```

- 创建复合索引
```
实例：同时为两个域创建索引
db.class1.ensureIndex({'name':1, 'age': -1})
```

- 设置过期时间:
```
expireAfterSeconds: 秒
db.test_timer.ensureIndex({"timer":1}, {expireAfterSeconds: 10})
```

- 删除索引
```
db.class1.dropIndex(name:1)
```

- 删除复合索引
```
db.class1.dropIndex({name:1, age:-1})
```

- 删除全部索引
```
db.class1.dropIndexes()
不会删除 _id 索引
```


其他索引
    数组索引：如果对某个域创建索引，这个域的值为数组，那么会对数组的值也会创建索引，提高数组中值的查找效率
    db.class3.find('bobby':'足球')

    子文档索引：如果某个域的值时文档，那么可以单独对这个子文档中的域创建索引
    db.class2.ensureIndex({'book.title':1})

    唯一索引：如果希望索引拥有不重复的值可以通过创建唯一索引来约束对应的值
    db.class1.ensureIndex({age:1}, {'unique':true})

    覆盖索引：查找时不获取具体文档，仅从索引中就可以获取到全部要查询的数据
             具体使用：查询时，限定返回的数据仅包含索引数据

    稀疏索引：只针对存在指定域的文档建立索引表，跳过不存在指定域的文档，使索引表更小巧，提高效率
    db.class2.ensureIndex({age:1}, {sparse:true})

    文本索引：使用文本索引可以较快速的进行文本检索，文本索引可以建立在任意格式的字符串上
    实例：给python这个域创建索引
    db.class2.ensureIndex({python:'text', description:'text'})
    查找python域中的字符串，如果包含search的内容则查找出来
    db.class2.find({$text:{$search:'python html css'}})
    * search 后的字符串以空格分割为多个部分，只要查找到其中一部分就会返回相应的文档
    * 如果查找的字符串中本身包含空格，则需要用引号作为一个整体饮用，此时内部引号需要转译字符
    db.class2.find({$text:{$search:"\"learn java\""}})

    不包含Linux 包含learn
    db.class2.find({$text:{$search:'learn -Linux'}})

    删除文本索引
    1、使用getIndexes() 查看索引名称
    2、dropIndex() 按照索引名称
    根据名称删除索引


索引约束：
    1、影响插入删除修改操作的效率，当数据发生修改时，不仅需要更新文档，还需要更新索引
    2、占用了一定的存储空间
    综上：当数据库较小，或者数据需要频繁的修改而不是查询的时候不宜创建索引


固定集合
    mongo中固定集合指的是性能出色且有着固定大小的集合
    作用：处理日志， 处理暂存， 做临时缓存区
    特点：插入数据快，顺序查询速度快，能够及时淘汰早期数据

    创建
    db.createCollection('collectionName', {capped:true, size:10000, max:10000})
    参数：capped：true 表示固定集合
         size： 空间大小 单位 KB
         max：  可以存放文档的个数上限

    检查一个集合是否是固定集合
    db.log.isCapped()


聚合：用于对文档查找结果的统计或者加工
    统计一个集合中文档数量
    db.class1.count()

    聚合函数配合聚合标识符来使用
    db.collectionName.aggregate()

    统计方法：
    $sum: 求和
    $avg: 求平均数
    $min: 最小值
    $max: 最大值
    $first: 获取第一个值
    $last:  获取最后一个值

    聚合标识符
    1、$group 分组
    {$group:{_id:'$name', num:{$sum:1}}}
      分组     按照姓名     统计结果名称

    统计每一个姓名人数
    db.class4.aggregate({$group:{_id:'$name', num:{$sum:1}}})

    统计每一个姓名的年龄之和
    db.class4.aggregate({$group:{_id:'$name', num:{$sum:'$age'}}})

    统计每个名字人的平均年龄
    db.class4.aggregate({$group:{_id:'$name', avg:{$avg:'$age'}}})

    可以同时统计多项内容
    db.class4.aggregate({$group:{_id:'$name', num:{$sum:'$age'}, avg:{$avg:'$age'}}})

    统计同名中年龄最大的
    db.class4.aggregate({$group:{_id:'$name', max:{$max:'$age'}}})

    统计每个性别中的第一个人
    db.class4.aggregate({$group:{_id:'$sex', name:{$first:'$name'}}})

    2、$project: 用于修改文档显示结构
    db.class4.aggregate({$project:{_id:0, name:1, age:1, sex:1}})

    更灵活的增加显示内容
    db.class4.aggregate({$project:{_id:0, name:1, age:1, realName:'$name'}})

    3、$match： 过滤
    db.class4.aggregate({$match:{'age':{$gt:13}}})

    4、$limit：取多少条数据
    db.class4.aggregate({$limit:3})

    5、$skip：跳过多少条数据
    db.class4.aggregate({$skip:3})

    6、$sort：排序
    db.class4.aggregate({$sort:{age:1}})


聚合管道：将前一个聚合的结果传给后一个聚合操作继续执行
    统计年龄大于13 的男女人数
    db.class4.aggregate([{$match:{age:{$gt:13}}}, {$group:{_id:'$sex', num:{$sum:1}}}])


GridFS：mongo提供的文件存储方式
    当文件大小大于16M的时候可以使用这种方式进行存储
    将文件存储在mongo的集合中，通过两个集合共同确定该文件的存储

    fs.files: 存储和文件有关的内容信息，比如filename，文件类型content_type等
    fs.chunks:实际存储文件的内容，以二进制方式分块存储，将文件分割为多个小块，每块作为chunks集合中的文档进行存储

    mongofiles -d dbName put fileName
    * db.Name :要存储的数据库，如果不存在自动创建
    * fileName:要存储的文件名

    查看文件信息：
    db.fs.files.find({}, {_id:0}).pretty()

    查看文件：
    db.fs.chunks.find({files_id:Object()})

    优缺点：
    优点：1、存储方便
         2、文件没有个数限制，方便管理
    缺点：读写效率低，中能整体替换不能部分更新


游标：
    * 防止网络拥塞，造成数据传输慢
    * 避免客户端
    var cursor = db.student.find()
    cursor.hasNext() 查看是否有下一项
    cursor.next()   获取下一项

    实例：js创建游标
    var cursor = db.class1.find()
---

python 的mongodb接口模块

- 安装：
```
sudo pip3 install pymongo
```

- 插入操作
```
insert()
insert_many()
insert_one()
save()
```

- 查找操作
```
find()
find_one()
```

> 注意游标操作变动，会对后续游标的使用产生一定的影响
```
cursor = my_set.find()
print(cursor.count())
print(cursor.next())  # 会影响排序操作
for i in my_set.find().sort([('age', 1)]):  # 不能用游标，去掉上一句 next 才可以
    print(i['name'], ':', i['age'])

for i in cursor.skip(3).limit(3):
    print(i['name'], ':', i['age'])
```

> 同样支持
$and $or $not $nor
$gt $gte $lt $lte $ne $nin $eq $in
---

rs.slaveOk();

MONGDB_SERVERS = 'mongodb://39.97.162.149:27018/?replicaSet=rs0&' \
                 'socketTimeoutMS=1000&connectTimeoutMS=1000&socketKeepAlive=true&' \
                 'w=majority&j=true&readPreference=secondaryPreferred'
