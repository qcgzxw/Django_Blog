# Django_Blog
A simple django blog demo.

## 部署说明
### Django环境
拉取最新代码
```shell script
git pull https://github.com/qcgzxw/Django_Blog.git
```
安装依赖
```shell script
pip install -r requirement.txt
```

### 项目初始化
复制并编辑配置文件
```shell script
cp .env.example .env
```
编辑.env文件，更改数据库、域名等信息

初始换数据库
```shell script
python manage.py makemigrations blog
python manage.py makemigrations comments
python manage.py migrate
```

创建后台管理员
```shell script
python manage.py createsuperuser
```

### 本地运行调试
```shell script
python manage.py runserver
```
打开http://127.0.0.1:8000/查看首页内容

### 后台管理
打开http://127.0.0.1:8000/admin使用你创建的后台管理员账号登录

然后插入一些新的字段

**1. 整站设置**
![UTOOLS1588167761324.png](https://qcgzxw-utools.oss-cn-shenzhen.aliyuncs.com/UTOOLS1588167761324.png)
**2. 文章分类和标签**

参照WordPress开发，仅有功能，需手动指定分类标签
![UTOOLS1588167851836.png](https://qcgzxw-utools.oss-cn-shenzhen.aliyuncs.com/UTOOLS1588167851836.png)
![UTOOLS1588167870873.png](https://qcgzxw-utools.oss-cn-shenzhen.aliyuncs.com/UTOOLS1588167870873.png)
**3. 文章**

可选择已存在的分类、标签
![UTOOLS1588167697850.png](https://qcgzxw-utools.oss-cn-shenzhen.aliyuncs.com/UTOOLS1588167697850.png)

## 目录结构说明
todo
## 线上部署说明
todo
## todo list
- [ ] 升级Django、依赖到最新版本
- [ ] 模板完全抽离
- [ ] 错误页面优化
- [ ] 管理员页面优化
- [ ] 丰富设置
- [ ] 测试

## 版本更新日志
- Ver1.0
项目初始化。

该项目是两年前博主在学习Django的时候的练手项目，内容可能有很多雷同，仅供学习，勿喷。

模板是在模板网找的一个比较顺眼的皮，现在已经找不到地址，如果作者看到希望我挂来源链接，请提issue。

没完全分离，以后会慢慢优化。

仅供学习，如果真正要用做线上项目，可以在GitHub搜另一个Django_Blog的项目