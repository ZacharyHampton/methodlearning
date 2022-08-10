import os
import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
import time

print('Logging in...')
session = requests.Session()
response = session.get('https://methodize.methodlearning.com/login')
soup = BeautifulSoup(response.text, features='html.parser')
csrf = soup.find('meta', attrs={'name': "csrf-token"})

response = session.post('https://methodize.methodlearning.com/login', data={'_token': csrf['content'], "email": os.environ['username'], "password": os.environ['password']})

os.system('clear')
print('Logged in.')
time.sleep(2)
os.system('clear')

while True:
	link = input("Link to lesson/quiz: ")
	os.system('clear')

	print('Getting answers...')

	response = session.get(link)
	soup = BeautifulSoup(response.text, features='html.parser')
	questions = json.loads(urllib.parse.unquote(soup.find('segment-questions')[':questions']))

	os.system('clear')
	
	y = 1 #: Question
	k = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #: Answer List
	for x in questions: #: For each question
		for z in x['questionable']['choices']: #: For each answer in each question
			if z['correct'] == 1: #: if correct
				print('{}. {}'.format(y, k[z['order_id']]))
				y += 1
				break
	input('\n\nPress enter to continue.')
	os.system('clear')