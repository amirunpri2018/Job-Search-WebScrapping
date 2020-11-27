from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/scrap', methods=['POST'])
def index():
    if request.method == 'POST':
        skills = request.form['skills'].split()
        location = request.form['location']
        date_posted = int(request.form['dateposted'])
        experience = int(request.form['experience'])
        print(f"{skills}")
        techgig_find_jobs(skills, location, date_posted, experience)
        times_find_jobs(skills, location, date_posted, experience)

def techgig_find_jobs(skills, location, date_posted, experience):
    
    url = f"https://www.techgig.com/job_search?page=1&txtKeyword={'+'.join(skills)}&cboWorkExp1={experience}&NoOfDaysSincePosted={date_posted * 7}&keyword=&txtLocation={location}"
    print(url)
    # print("URL : "+url)
    print("-----TECHGIG-----")

    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'lxml')

    jobs = soup.find_all('div', class_='col-md-6 col-sm-12')
    # print(jobs)
    for job in jobs:
        job = job.find('div', class_='job-box-lg')
        company = job.find('div', class_='job-header clearfix').find('div', class_='details full-width').p.text
        title = job.find('div', class_='job-header clearfix').find('div', class_='details full-width').h3.text
        contents = job.find('div', class_='job-content').find('dl', class_='description-list').find_all("dd")
        more_details = job.find('div', class_='job-footer clearfix').a['href']
        experience = contents[0].text
        ctc = contents[1].text
        skills = contents[2].text
        posted = job.find('div', class_='job-footer clearfix').span.text.split()
        posted = posted[2] + ' ' + posted[3]
        # print(contents) # For debugging process

        print(f"Job title : {title}\nCompany Name : {company}\nExperience  : {experience}\nCTC : {ctc}\n"
              f"Skills : {skills}\nPosted : {posted}\nMore details : {more_details}")
        print("\n")


def times_find_jobs(skills, location, date_posted, experience):
    print("-----Timesjobs-----")

    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&f" \
          f"rom=submit&txtKeywords={'+'.join(skills)}&txtLocation={location}&cboWorkExp1={experience}"
    html_text = requests.get(url)

    soup = BeautifulSoup(html_text.text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # print(jobs)
    for index, job in enumerate(jobs):  # index for literally the index of the job
        published_date = job.find('span', class_='sim-posted').span.text
        title = job.find('header', class_='clearfix').h2.a.text
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']

        print(f"Job Title : {title.strip()}\nCompany name : {company_name.strip()}\nRequired skills : {skills.strip()}")
        print(f"Publihsed on : {published_date}\nMore info : {more_info}\n")



if __name__ == "__main__":
    app.run(port=5500,debug=True)