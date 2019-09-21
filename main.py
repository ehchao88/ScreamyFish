from flask import Flask, render_template
from scripts.vision_labels import get_labels
from scripts.image_search import get_image_url

app = Flask(__name__)

@app.route("/")
def hello():
	image_url = get_image_url('George_W_Bush')
	print(image_url)
	labels = get_labels(image_url)
	print(labels)
	return render_template('list_labels.html', image_url=image_url, labels=labels)

@app.route("/select_lang")
def select_lang():
	return "Select your language"

@app.route("/game/<language>")
def game(language):
	return "You are playing in " + language  

if __name__ == "__main__":
	app.run()
