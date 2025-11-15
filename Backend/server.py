from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def home():
    return "Hello, this is a Flask server!"

if __name__ == "__main__":
    print("Flask server for Gs")
    app.run(port=5000)