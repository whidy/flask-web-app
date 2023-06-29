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
flask --app ./api/index run

# 生产模式
gunicorn index:app --chdir ./api
```

## 数据库

### MongoDB

* https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-in-a-flask-application
* https://www.mongodb.com/compatibility/setting-up-flask-with-mongodb

## 部署

在一些云容器上进行部署的研究笔记。

### 在Heroku部署

~~Heroku部署已实现，自定义域名，搭配cloudflare，访问<https://flask.agoodboy.xyz/>，问题就是我确实还是不清楚 `dyno` 到底怎么收费，先开着试试看吧。~~

感觉还是要收费，所以最后还是关了，想了解详细的，请阅读下面信息。

#### 关于Heroku收费问题

* https://devcenter.heroku.com/changelog-items/907
* https://devcenter.heroku.com/articles/free-dyno-hours
* **https://blog.heroku.com/next-chapter**

```
Personal accounts are given a base of 550 free dyno hours each month. In addition to these base hours, accounts which verify with a credit card will receive an additional 450 hours added to the monthly free dyno quota. This means you can receive a total of 1000 free dyno hours per month, if you verify your account with a credit card.
```

不确定总结：~~普通个人用户有免费额度（每月550小时），如果添加信用卡则提升到1000小时，故而可以开启dyno。要不然根本无法跑python应用啊！~~

但是看了：

```
Starting October 26, 2022, we will begin deleting inactive accounts and associated storage for accounts that have been inactive for over a year. Starting November 28, 2022, we plan to stop offering free product plans and plan to start shutting down free dynos and data services. We will be sending out a series of email communications to affected users.

We will continue to provide low-cost solutions for compute and data resources: Heroku Dynos starts at $7/month, Heroku Data for Redis® starts at $15/month, Heroku Postgres starts at $9/month. See Heroku Pricing Information for current details. These include all the features of the free plans with additional certificate management and the assurance your dynos do not sleep to help ensure your apps are responsive.
```

我觉得还是要收费，参考 `https://www.heroku.com/pricing` ，弹性的 `Plan Basic` 应该是用于测试的最便宜了（0~7美元）。所以最后我还是把这个heroku的服务停了吧。**做测试没钱付费。**

### Heroku部署研究

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

> Vercel部署已实现。请注意查看 `vercel.json` 。不过这个是运行在开发环境状态中，并且需要科学上网才能访问。

参考了许多资料，Vercel还是老毛病，非要搞个 `api` 目录。但是flask项目只需要配置 `rewrites` 选项即可。

相关阅读：

* https://github.com/vercel/examples/tree/main/python/flask
* https://matiasfuentes.hashnode.dev/how-to-deploy-a-flask-web-app-on-vercel

## 模型

参见：g4f/models.py
