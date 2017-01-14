#!flask/bin/python
from flask import Flask, render_template, jsonify
import urllib2, json
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
	retun "hey"

@app.route("/memes", methods=['GET'])
def get_meme_text(emotion):
	with open('DankMemeStash.json') as data_file:
		data = json.load(data_file)
	m_index = randint(0, len(data[emotion])-1)
	meme = data[emotion][m_index]
	return meme

if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0", port=8000)
