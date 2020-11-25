'''
This works for Jobs only posted few days back having python as one of the requirement.
It will scrap the jobs only on the first page of the website

'''

from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                         '=submit&txtKeywords=python&txtLocation=')

soup = BeautifulSoup(html_text.text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
print(jobs)
