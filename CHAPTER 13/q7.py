#pip install flask
#search for flask module on chrome

# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

app.run()