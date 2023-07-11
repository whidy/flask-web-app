import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import g4f

# print(g4f.Provider.Ails.params)

provider_map = {
    # "Ails": g4f.Provider.Ails,
    # "You": g4f.Provider.You,
    # "Bing": g4f.Provider.Bing,
    # "Yqcloud": g4f.Provider.Yqcloud,
    "Theb": g4f.Provider.Theb,  # ok
    "Aichat": g4f.Provider.Aichat,  # ok
    # "Bard": g4f.Provider.Bard,
    # "Vercel": g4f.Provider.Vercel,
    # "Forefront": g4f.Provider.Forefront,
    # "Lockchat": g4f.Provider.Lockchat,
    # "Liaobots": g4f.Provider.Liaobots,
    # "H2o": g4f.Provider.H2o,
    # "ChatgptLogin": g4f.Provider.ChatgptLogin,
    "DeepAi": g4f.Provider.DeepAi,  # ok
    "GetGpt": g4f.Provider.GetGpt,  # ok
}

from datetime import datetime
import configparser
from flask import (
    Flask,
    request,
    jsonify,
    url_for,
    render_template,
    make_response,
    current_app,
    g,
)
from markupsafe import escape

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.environ.get("MONGO_URI")

client = MongoClient(uri, server_api=ServerApi("1"))
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# 获取所有数据库的名称
db_names = client.list_database_names()
# for name in db_names:
#     print(name)
db = client["gpt"]
messages = db["messages"]
gptRecords = db["gpt_records"]
app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    # return render_template("index.html")
    all_messages = messages.find().sort("timestamp", -1)
    return render_template("index.html", messages=all_messages)


@app.route("/hello/<name>")
def hello_world(name=None):
    return render_template("hello.html", name=name)


@app.route("/gpt", methods=["GET", "POST"])
def gpt():
    if request.method == "POST":
        # time.sleep(2)
        # return {"answer": "test message"}
        question = request.form["question"]
        provider = request.form["provider"]
        model = request.form["model"] or "gpt-3.5-turbo"
        # auth = request.form["auth"] or "m4rxMTa2JqEzE"

        try:
            askTime = datetime.now()
            response = g4f.ChatCompletion.create(
                model=model,
                provider=provider_map.get(provider),
                messages=[{"role": "user", "content": question}],
                # auth=auth,
            )

            # 需要在此处向gpt_records表插入数据
            record = {
                "question": question,
                "answer": response,
                "question_time": askTime,
                "answer_time": datetime.now(),
                "model": model,
                "provider": provider,
                # "auth_key": auth,
            }
            gptRecords.insert_one(record)
            return {"answer": response}

        except Exception as e:
            error_msg = str(e)
            response = make_response({"error": error_msg}, 500)
            response.headers["Content-Type"] = "application/json"
            # 需要在此处向gpt_records表插入数据
            record = {
                "question": question,
                "answer": error_msg,
                "question_time": askTime,
                "answer_time": datetime.now(),
                "provider": provider,
                "model": model,
                # "auth_key": auth,
            }
            gptRecords.insert_one(record)
            return {"answer": "发生错误，请重试，这应该是liaobots的锅~"}
    else:
        return render_template("gpt.html")


@app.route("/about")
def about():
    return "The about page, Nothing more but whidy look at you."


@app.route("/submit_comment", methods=["POST"])
def submit_comment():
    now = datetime.now()
    # 解析表单数据
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # 将数据保存到 MongoDB 数据库中
    result = messages.insert_one(
        {"name": name, "email": email, "message": message, "timestamp": now}
    )

    # 返回成功消息
    return jsonify(
        {"status": "success", "message": "留言提交成功！", "id": str(result.inserted_id)}
    )


config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
