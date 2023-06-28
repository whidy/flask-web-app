import g4f
import time
from flask import Flask, request, url_for, render_template, make_response
from markupsafe import escape

# url_for('static', filename='style.css')

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<name>")
def hello_world(name=None):
    return render_template("hello.html", name=name)


@app.route("/gpt", methods=["GET", "POST"])
def gpt():
    if request.method == "POST":
        # time.sleep(2)
        # return {"answer": "test message"}
        question = request.form["question"]
        auth = request.form["auth"] or "4PT9JqBJscqCw"
        model = request.form["model"] or "gpt-3.5-turbo"

        try:
            response = g4f.ChatCompletion.create(
                model=model,
                provider=g4f.Provider.Liaobots,
                messages=[{"role": "user", "content": question}],
                auth=auth,
            )
            return {"answer": response}

        except Exception as e:
            error_msg = str(e)
            response = make_response({"error": error_msg}, 500)
            response.headers["Content-Type"] = "application/json"
            return {"answer": "发生错误，信息：" + response}
    else:
        return render_template("gpt.html")


@app.route("/about")
def about():
    return "The about page, Nothing more but whidy look at you."
