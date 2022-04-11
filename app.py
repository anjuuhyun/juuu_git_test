

from flask import Flask, render_template

import first

app = Flask(__name__)
app.register_blueprint(first.blue_first)


# @app.route('/')
# def hello_world():
#     return "<h1>test_flask</h1>"

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
