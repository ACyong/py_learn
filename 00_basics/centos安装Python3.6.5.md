> Linux版本：CentOS7.4 64位, Python版本：Python3.6.5

第一步：准备编译环境：
```
yum groupinstall 'Development Tools'
yum install zlib-devel bzip2-devel  openssl-devel ncurses-devel
```
 
第二步：下载Python3.6.5
```
wget --no-check-certificate https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
```

第三步：创建安装目录
```
sudo mkdir /usr/local/python3
```

第四步：解压
```
tar -zxvf Python-3.6.5.tgz

# 切换到解压后的根目录
cd Python-3.6.5/
```

第五步：编译安装
```
./configure --prefix=/usr/local/python3 
(如果遇到：configure: error: no acceptable C compiler found in $PATH, 解决方法：# yum install gcc)

make
make install
```

第六步：创建Python3链接
```
Linux里原来的python命令还是指向Python2，这里创建python3的软链接指向Python3，这样Python2和Python3就都可以用了。
ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
```

第七步：创建Pip3链接
```
也保留pip指向Pip2，创建pip3的软链接指向Pip3

ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

此时pip3的版本是9.0.3需要升级一下升级到最新

# 在root用户下或使用sudo权限执行
python3 -m pip install --upgrade pip

(如果遇到ModuleNotFoundError: No module named '_sqlite3',就实行yum install sqlite* 然后重新执行第五步)
```
