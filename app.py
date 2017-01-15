#!flask/bin/python
from flask import Flask, render_template, jsonify
import urllib2, json
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
	return "hey"

@app.route("/memes/<emotion>")
def get_meme_text(emotion):
	with open('DankMemeStash.json') as data_file:
		data = json.load(data_file)
	emotion_top = emotion + " Top"
	emotion_bottom = emotion + " Bottom"
	m_index = randint(0, len(data[emotion_top]) - 1)
	top = data[emotion_top][m_index]
	bottom = data[emotion_bottom][m_index]
	return jsonify({'top': top, 'bottom': bottom})

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
