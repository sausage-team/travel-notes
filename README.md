![django](https://img.shields.io/pypi/pyversions/django.svg)

[前端源码地址](https://github.com/sausage-team/travel-notes-web)

## 描述:

游记服务端

## 环境依赖:

1. python == 3.6
2. pip3 == 9.0.1
3. docker

## 安装:
安装前请预留8000, 8088, 13306端口

0.  命令行进入`project`根目录下依次执行
1.  `pip install -r requirements.txt`
2.  `docker-compose up -d`
3.  `python manage.py makemigrations`
4.  `python manage.py migrate`
5.  `python manage.py loaddata user`
5.  启动服务 `python manage.py runserver 0.0.0.0:8000`

## 默认管理员账号

* username: admin
* password: 123456

## TODO:
[Providing init data with fixtures](https://docs.djangoproject.com/en/1.10/howto/initial-data/)

