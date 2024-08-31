from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')
table = soup.find('table').find('tbody').find_all('tr')

countries_list = []

for row in table:
    dic = {}
    country = row.find_all('td')[1].text
    population = row.find_all('td')[2].text

    dic['Country'] = country
    dic['Population'] = population

    countries_list.append(dic)


df = pd.DataFrame(countries_list)
df.to_excel('countries_list.xlsx', index=False)