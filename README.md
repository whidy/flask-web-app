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
gunicorn index:app --chdir ./api
```

## 部署

在一些云容器上进行部署的研究笔记。

### 在Heroku部署

Heroku部署已实现，自定义域名，搭配cloudflare，访问<https://flask.agoodboy.xyz/>，问题就是我确实还是不清楚 `dyno` 到底怎么收费，先开着试试看吧。

关于收费问题：

* https://devcenter.heroku.com/changelog-items/907
* https://devcenter.heroku.com/articles/free-dyno-hours

```
Personal accounts are given a base of 550 free dyno hours each month. In addition to these base hours, accounts which verify with a credit card will receive an additional 450 hours added to the monthly free dyno quota. This means you can receive a total of 1000 free dyno hours per month, if you verify your account with a credit card.
```

不确定总结：普通个人用户有免费额度（每月550小时），如果添加信用卡则提升到1000小时，故而可以开启dyno。要不然根本无法跑python应用啊！

* https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/
* https://realpython.com/flask-by-example-part-1-project-setup/

> ~~似乎gunicorn是收费的（按照运行时间），参考：https://devcenter.heroku.com/articles/usage-and-billing#dyno-usage-and-costs，所以我将 `Procfile` 改为 `web: python3 wsgi.py` （原： `web: gunicorn wsgi:app` ）~~
>
> ~~当然这个wsgi名称可能造成困扰，暂时先这样吧。~~
>
> `Procfile` ，由于需要适配vercel，所以最后写成了： `web: gunicorn index:app --chdir ./api`

关于Heroku部署相关的资料

* https://devcenter.heroku.com/articles/python-gunicorn
* https://devcenter.heroku.com/articles/getting-started-with-python

关于Flask的部署说明：

* https://flask.palletsprojects.com/en/2.3.x/deploying/

### 在Vercel上进行部署

Vercel部署已实现。请注意查看 `vercel.json` 。

参考了许多资料，Vercel还是老毛病，非要搞个 `api` 目录。但是flask项目只需要配置 `rewrites` 选项即可。

相关阅读：

* https://github.com/vercel/examples/tree/main/python/flask
* https://matiasfuentes.hashnode.dev/how-to-deploy-a-flask-web-app-on-vercel

## 模型

参见：g4f/models.py
