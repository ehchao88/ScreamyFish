import requests
import json
#AIzaSyDDISWLsMtifIhV0W6dGu_TyN-fJcQx3Zo
search_result = requests.get('https://www.googleapis.com/customsearch/v1?key=AIzaSyDDISWLsMtifIhV0W6dGu_TyN-fJcQx3Zo&cx=003789856186025432586:pbxx5vdz2go&searchType=image&q=lectures')
search_result_dict = json.loads(search_result.text)
print(search_result_dict)