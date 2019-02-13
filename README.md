## 说明

	Django 2 by example 书中 blog 的实例 
	原文地址http://www.conyli.cc/archives/category/program/django
	
## 运行环境

| Project | Status | Description |
|---------|--------|-------------|
| python          | 3.6.5	| 在这个版本以及以上都可以 |
| django          | 2.1.2   | 在这个版本以及以上都可以 |
| django-taggit   | 0.23.0  | 必须此版本 |

## 安装环境
`pip3 install django`

`pip3 install django-taggit 0.23.0`

使用Pycharm直接运行即可，
或者使用命令
`python manage.py runserver`


## admin后台
默认用户名erhao
密码1234

	
## 目录介绍
./blog
├──static                            	 // 静态文件相关
│
│
├──templates							// HTML模板
│
│
├──templateags							// 自定义模板标签
│
│
├──forms.py								// form表单
│
│
├──urls.py								// url分发
│
│
├──views.py								// 业务处理