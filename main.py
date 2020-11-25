'''
This works for Jobs only posted few days back having python as one of the requirement.
It will scrap the jobs only on the first page of the website.
User can enter one skill which she/he doesn't has and the result will have jobs which do not req that skill
Program can run directly from command line
It generates output every 10 minutes
'''

from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    skill_unfamiliar = input("Enter skill you are not familiar with : ")
    print(f"Filtering jobs not having skill : {skill_unfamiliar}")
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                             '=submit&txtKeywords=python&txtLocation=')

    soup = BeautifulSoup(html_text.text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if skill_unfamiliar not in skills:
                print(f"Company name : {company_name.strip()}\nRequired skills : {skills.strip()}")
                print(f"More info : {more_info}")
                print('')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
