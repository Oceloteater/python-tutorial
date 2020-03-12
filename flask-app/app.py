from flask import Flask

app = Flask(__name__)


@app.route('/')  # 'http://google.com/' endpoint
def home():
    return 'Hello world!'


app.run(port=5000)
