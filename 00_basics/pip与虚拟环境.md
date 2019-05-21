# python 工具

## 1、pip 软件包管理器：

- 安装pip：
> 如果安装的Python 2 >=2.7.9 或者Python 3 >=3.4 那么Python自带了pip,所以不用安装。

```
$ wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
```
```
$ sudo python get-pip.py   # 安装pip
```
```
$ sudo python3 get-pip.py  # 安装pip3
```

- 使用pip：
```
使用python2 的pip - pip 指令
```
```
使用python3 的pip3 - pip 指令
```

- 安装python 包
```
sudo pip3 install SomePackage
```

ex：
```
sudo pip3 install pymysql==0.7.11
sudo pip3 install Pillow
sudo pip3 install Django==1.11.8
```

- 下载python 包
```
sudo pip3 download SomePackage
```

- 删除python 包
```
sudo pip3 uninstall SomePackage
```

- 升级python 包
```
sudo pip3 upgrade SomePackage
```

- 查看当前环境中所安装的包
```
pip3 list
```

- 升级pip
```
pip3 install --upgrade pip
```

- 记录/安装现有环境中的python 包
```
pip3 freeze > requirements.txt  # 记录当前环境中所安装的python 工具包

pip3 install -r requirements.txt  # 允许在当前环境下，逐一安装requirements.txt 中所列出的内容
```
---

## 2、virtualEnv 虚拟环境：
> 根据python 的大环境虚拟出来的一套开发环境，虚拟环境是相互独立的，在虚拟环境中安装的包不影响真实的python 环境，也不会影响其他的虚拟环境

- 安装VirtualEnv：
```
sudo pip3 install virtualenv
```

- 准备工作
```
mkdir MyEnv
cd MyEnv
```

- 创建虚拟环境
```
virtualenv 虚拟环境名称
```
ex：
```
virtualenv default
```

> 创建指定版本的虚拟环境
```
virtualenv -p /usr/bin/python2.7 名称
```
```
virtualenv -p /usr/bin/python3.6 名称
```
> 注意：在虚拟环境中使用pip 安装python 包的时候不能使用sudo 授权， 否则的话，会安装到真实的python 环境中

- 启动虚拟环境
```
虚拟环境目录中 bin/activate
执行activate 就可以启动虚拟环境命令如下：
    source bin/activate  # 注意：不能在bin 目录中启动虚拟环境
启动成功：(default) default shouei$
```

- 退出虚拟环境
```
在任何地方输入命令：deactivate
```

- 删除虚拟环境
```
rm -rf 虚拟环境文件名
```
---

## 3、virtalEnvWrapper 虚拟环境管理工具
> 能够快速的、方便的管理虚拟环境

- 安装virtalEnvWrapper：
```
sudo pip3 install virtualenvwrapper
```

- 配置 virtalEnvWrapper：
```
在～目录下，有一个终端管理文件 .bashrc (在～ 目录下输入ll)
修改.bashrc 最底部增加以下内容：

1、export WORKON_HOME=~/MyEnv
将~/MyEnv 作为虚拟环境管理目录，所以使用 virtualenvwrapper 创建的虚拟环境默认都保存于此

2、如果系统中包含多个python 环境的话，则不需增加以下内容
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2

3、source /usr/local/bin/virtualenvwrapper.sh
4、在～目录下，执行一遍 .bashrc: source .bashrc
```

- mac 下的配置：
```
1、创建目录用来存放虚拟环境
mkdir $HOME/.virtualenvs

2、在 .bash_profile 或者 .zshrc 追加两行
export WORKON_HOME=$HOME/.virtualenvs  （默认存放路径）
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3  (默认python版本)
source /usr/local/bin/virtualenvwrapper.sh

3、运行：
source ~/.bash_profile 或
source ~/.zshrc

4、此时virtualenvwrapper就可以使用了。
```

- 使用虚拟环境
```
1、创建并进入到虚拟环境
mkvirtualenv 虚拟环境名称
mkvirtualenv --python=/Users/zyz/.pyenv/versions/2.7.8/bin/python2.7 虚拟环境名称

2、查询当前所维护的所有虚拟环境
workon

3、切换虚拟环境
workon 虚拟环境名称

4、退出虚拟环境
deactivate

5、删除虚拟环境
rmvirtualenv 虚拟环境名称
```
---

## 4、pipenv

## 5、pyenv
