import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

url_template = "https://www.indeed.com/jobs?q=mechanical+engineer&l={}&sort=date&start={}"

max_results_per_city = 2000 

i = 0
results = []
df = pd.DataFrame(columns=["Title","Location","Salary"])
for city in set(['United+States']):
	for start in range(0, max_results_per_city, 10):

	        url = url_template.format(city, start)

	        html = requests.get(url)
	        soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
	        for each in soup.find_all(class_= "result" ):
	            try: 
	                title = each.find(class_='jobtitle').text.replace('\n', '')
	            except:
	                title = None
	            try:
	                location = each.find('span', {'class':"location" }).text.replace('\n', '')
	            except:
	                location = None
	            try:
	                salary = each.find('span', {'class':'no-wrap'}).text
	            except:
	                salary = None
	            df = df.append({'Title':title, 'Location':location, 'Salary':salary}, ignore_index=True)

df.to_csv('indeedlist_uncleaned_mechanicalengineer.csv', encoding='utf-8')


