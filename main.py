import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL = 'https://www.avito.ru/arzamas/transport'

r = requests.get(URL)

print(r.text)