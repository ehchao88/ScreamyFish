import requests
import csv
from bs4 import BeautifulSoup

response = requests.get('https://www.wordexample.com/list/most-common-nouns-english')
soup = BeautifulSoup(response.text, 'html.parser')

words = soup.find_all('span', class_='word-popover')
fin_words = []
alpha = 'qwertyuiopasdfghjklzxcvbnm'
for word in words:
	fin_word = str(word)
	fin_word = fin_word[fin_word.index('>') + 1:]
	char_ind = 0
	while fin_word[char_ind] not in alpha:
		char_ind += 1
	fin_word = fin_word[char_ind:]
	char_ind = 0
	while fin_word[char_ind] in alpha:
		char_ind += 1
	fin_word = fin_word[:char_ind]
	fin_words.append(fin_word)
	print(fin_word)
#print(fin_words)
with open('nouns.csv', 'w') as f:
	data_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	for word in fin_words:
		data_writer.writerow([word])