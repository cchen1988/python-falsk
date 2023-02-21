from flask import Flask

application = Flask(__name__)
app = application
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run(host='0.0.0.0', port=8000)
