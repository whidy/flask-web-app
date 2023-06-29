# Python Web Application

参考：

* https://github.com/xtekky/gpt4free
* https://flask.palletsprojects.com/en/2.3.x/quickstart/
* https://liaobots.com/zh

* https://matiasfuentes.hashnode.dev/how-to-deploy-a-flask-web-app-on-vercel

## 运行

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# 本地运行
flask --app index run

# 生产模式
gunicorn wsgi:app
```

## 部署

在一些云容器上进行部署的研究笔记。

### 在Heroku部署

* https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/
* https://realpython.com/flask-by-example-part-1-project-setup/

> 似乎gunicorn是收费的（按照运行时间），参考：https://devcenter.heroku.com/articles/usage-and-billing#dyno-usage-and-costs，所以我将 `Procfile` 改为`web: python3 wsgi.py`（原：`web: gunicorn wsgi:app`）
>
> 当然这个wsgi名称可能造成困扰，暂时先这样吧。

关于Heroku部署相关的资料

* https://devcenter.heroku.com/articles/python-gunicorn
* https://devcenter.heroku.com/articles/getting-started-with-python

关于Flask的部署说明：

* https://flask.palletsprojects.com/en/2.3.x/deploying/

### 在Vercel上进行部署

研究实验中。。。

## 模型

参见：g4f/models.py