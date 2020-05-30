import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

ranks = soup.select('tr.list > td.number')
titles = soup.select('tr.list > td.info > a.title')
artists = soup.select('tr.list > td.info > a.artist')


for rank, title, artist in zip(ranks, titles, artists):
    print(rank.text.split('\n')[0], title.text.strip(), artist.text)


