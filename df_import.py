import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

df = pd.read_csv('indeedlist_uncleaned_mechanicalengineer.csv')
df.dropna(subset = ["Location"], inplace=True)
df.drop(df.columns[0], axis=1, inplace = True)
df = df.join(df['Location'].str.split(',', 1, expand=True).rename(columns={0:'City', 1:'State'}))

def strip_state(x):
    if x != None:
        return x[0:3]
    else:
        None

df['State Initials'] = df['State'].apply(strip_state)
df['Location'] = df['City'].astype(str) + ',' + df['State Initials'].astype(str)

df.to_csv('indeedlist_cleaned_mechanicalengineer.csv', encoding='utf-8')