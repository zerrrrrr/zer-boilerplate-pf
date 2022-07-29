from flask import Flask
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app, origin='*')

@app.route("/", methods=["GET"])
def hello():
    return {
        "msg": "ok",
        "status": "success",
    }


if __name__ == "__main__":
    print("server start")
    serve(app, host="0.0.0.0", port=3000)
