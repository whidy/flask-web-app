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

在Heroku部署

* https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/
* https://realpython.com/flask-by-example-part-1-project-setup/



## 模型

参见：g4f/models.py
