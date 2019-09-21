from google.cloud import translate

def translate_list(lang, labels):
	translate_client = translate.Client()
	trans_labels = []
	target = lang

	for label in labels:
		translation = translate_client.translate(label, target_language=target)
		trans_labels.append(translation['translatedText'])
	return trans_labels