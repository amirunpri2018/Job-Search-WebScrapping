'''
It only searches for Python jobs for now!
v1
This works for Jobs only posted few days back having python as one of the requirement.
It will scrap the jobs only on the first page of the website.
User can enter one skill which she/he doesn't has and the result will have jobs which do not req that skill
Program can run directly from command line
It generates output every 10 minutes
To refer to V1 - visit =

v2
Can scrap from Techgig also
Displays whole output in Command line
'''

from bs4 import BeautifulSoup
import requests
import time


def techgig_find_jobs():
    skills = input("Looking for a job in the field? (python, java, etc) : ")
    location = input("Location ? : ")
    date_posted = input("How recent? 1 - for 1 week, 2 - 2 week, 0 - None : ")
    experience = input("Previous experience : 0 - fresher, 1 for 1 year and so on : ")
    
    print("-----TECHGIG-----")
    skill_unfamiliar = input(f"Enter skill you are not familiar with : ")
    print(f"Filtering job not having skill : {skill_unfamiliar}")
    html_text = requests.get("https://www.techgig.com/job_search?page=1&txtKeyword=python&keyword=&txtLocation=")
    soup = BeautifulSoup(html_text.text, 'lxml')

    jobs = soup.find_all('div', class_='col-md-6 col-sm-12')
    # print(jobs)
    for job in jobs:
        job = job.find('div', class_='job-box-lg')
        company = job.find('div', class_='job-header clearfix').find('div', class_='details full-width').p.text
        contents = job.find('div', class_='job-content').find('dl', class_='description-list').find_all("dd")
        more_details = job.find('div', class_='job-footer clearfix').a['href']
        experience = contents[0].text
        ctc = contents[1].text
        skills = contents[2].text
        posted = job.find('div', class_='job-footer clearfix').span.text.split()
        posted = posted[2] + ' ' + posted[3]
        # print(contents) # For debugging process
        if skill_unfamiliar not in skills:
            print("---" * 18)
            print(f"Company Name : {company}\nExperience  : {experience}\nCTC : {ctc}\nSkills : {skills}\n"
                  f"Posted : {posted}\nMore details : {more_details}")


def times_find_jobs():
    print("-----Timesjobs-----")
    skill_unfamiliar = input("Enter skill you are not familiar with : ")
    print(f"Filtering jobs not having skill : {skill_unfamiliar}")
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                             '=submit&txtKeywords=python&txtLocation=')

    soup = BeautifulSoup(html_text.text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # print(jobs)
    for index, job in enumerate(jobs):  # index for literally the index of the job
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if skill_unfamiliar not in skills:
                '''with open(f'posts/job_{index}.txt', 'w') as f:
                    f.write(f"Company name : {company_name.strip()}\nRequired skills : {skills.strip()}\n")
                    f.write(f"More info : {more_info}")
                print(f"File {index} saved!")'''  # To save data in text file

                print(f"Company name : {company_name.strip()}\nRequired skills : {skills.strip()}")
                print(f"More info : {more_info}\n")


if __name__ == '__main__':
    '''while True:
        times_find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)'''
    techgig_find_jobs()
    times_find_jobs()
