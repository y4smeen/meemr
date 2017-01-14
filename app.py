from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

@app.route("/")
def index():
	retun "hey"


if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=8000)