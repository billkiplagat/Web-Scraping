import requests
from bs4 import BeautifulSoup

print('Write some unfamiliar skills you dont want')
unfamiliar_skills = input('>')
print(f'Filtering out unfamiliar skills')

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_='joblist-comp-name').text
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        link = job.header.h2.a['href']

        if unfamiliar_skills not in skills:
            print(f"Company Name: {company_name.strip()}")
            print(f"Skills: {skills.strip()}")
            print(f'More info: {link}')
            print('')
