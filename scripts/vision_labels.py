import io
import os

#import gcloud client libraries
from google.cloud import vision
from google.cloud.vision import types

def get_labels(path):
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
	str_labels = []
	for label in labels:
		str_labels.append(str(label.description))

	return str_labels