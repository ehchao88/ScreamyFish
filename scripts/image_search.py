import requests
import json
#AIzaSyDDISWLsMtifIhV0W6dGu_TyN-fJcQx3Zo
def get_image_url(query):
	search_result = requests.get('https://www.googleapis.com/customsearch/v1?key={insert key}cx=003789856186025432586:pbxx5vdz2go&searchType=image&q=' + query)
	search_result_dict = json.loads(search_result.text)
	return str(search_result_dict['items'][0]['link'])
