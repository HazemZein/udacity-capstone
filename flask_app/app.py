from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    returnn "<p>Hello World! My name is Hazem</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)