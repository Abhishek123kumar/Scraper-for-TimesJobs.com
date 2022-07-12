#install all the requirements Step0
# import requests
# from bs4 import BeautifulSoup
# url="https://www.codewithharry.com/"
# with open('index1.html','r') as html_file:
#     content=html_file.read()
#     print(content)
#     soup=BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    # tags=soup.find_all('h1')
    # for course in tags:
    #     print(course.text)
    # print(tags)

#step 1:get the html
#r=requests.get(url)
#htmlContent=r.content
#print(htmlContent)
#step2:parse the html
#soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup)
#step3 :html tree traversal
from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not familiar with")
unfamiliar_skill= input('>')
print(f'Filtering out :{unfamiliar_skill}')
def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for job in jobs :
        published_date=job.find('span',class_="sim-posted").span.text.replace(' ','')
        if 'few' in published_date:
            company_name=job.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skills=job.find('span',class_="srp-skills").text.replace(' ','')
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                print(f"Company Name:{company_name.strip()}")
                print(f"Required Skills:{skills.strip()}")
                print(f'More Info:{more_info}')
                print(' ')


if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10;
        print(f"Waiting {time_wait} secondes...")
        time.sleep(time_wait)
