from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello")
def hell():
    return "Hi"


if __name__ == "__main__":
    app.run(debug=True)
