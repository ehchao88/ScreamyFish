import io
import os

#import gcloud client libraries
from google.cloud import vision
from google.cloud.vision import types

def print_labels(path):
	#instantiate client
	client = vision.ImageAnnotatorClient()

	#Name of image file
	if path.startswith('http') or path.startswith('gs:'):
		image = types.Image()
		image.source.image_uri = path
	else:
		#load image into memory
		with io.open(path, 'rb') as image_file:
			content = image_file.read()

		image = types.Image(content = content)

	#Perform label detection on image
	response = client.label_detection(image=image)
	labels = response.label_annotations

	print("Labels:")
	for label in labels:
		print(label.description)

print_labels('resources/fish.jpg')
print_labels('https://cdn.technologynetworks.com/tn/images/thumbs/jpeg/640_360/the-freshwater-fish-crisis-316375.jpg')