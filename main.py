from flask import Flask, render_template
from scripts.vision_labels import get_labels

app = Flask(__name__)

@app.route("/")
def hello():
	image_url = 'https://www.miamiherald.com/latest-news/45pxfx/picture229650079/alternates/LANDSCAPE_1140/toadfish.jpg'
	labels = get_labels(image_url)
	return render_template('list_labels.html', image_url=image_url, labels=labels)

@app.route("/select_lang")
def select_lang():
	return "Select your language"

@app.route("/game/<language>")
def game(language):
	return "You are playing in " + language  

if __name__ == "__main__":
	app.run()
