from flask import Flask, render_template, request, redirect
from scripts.vision_labels import get_labels
from scripts.image_search import get_image_url
from scripts.translate_labels import translate_list
import csv
import random

lang = 'en'
nouns = ['time']
with open('nouns.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		nouns.append(row['time'])
#print(nouns)
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/select_lang", methods=['GET','POST'])
def select_lang():
	if request.method == 'POST':
		language = request.form.get('language')
		return redirect('/game/' + language)
	else:
		return render_template('select_lang.html')

@app.route("/game/<language>")
def game(language):
	image_url = get_image_url(nouns[random.randint(0, len(nouns))])
	print(image_url)
	labels = get_labels(image_url)
	trans_labels = translate_list(language, labels)
	print(labels)
	return render_template('list_labels.html', image_url=image_url, labels=trans_labels)

if __name__ == "__main__":
	app.run()
