import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.idescat.cat/indicadors/?id=conj&n=10261&tema=PREUS&col=1'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div_espanya = soup.find('div', id='Espanya')
table = div_espanya.find('table')
df = pd.read_html(str(table))[0]

df.to_csv('output.csv', index=False)


