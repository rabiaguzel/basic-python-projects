from bs4 import BeautifulSoup
import requests
import lxml
url="https://www.imdb.com/chart/top/"
request=requests.get(url)

soup=BeautifulSoup(request.content,"lxml")
top_250=soup.find("ul",attrs={"class":"ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base"}).find_all("li")

film_sira=1
for film in top_250:
    adi= film.find("h3",attrs={"class":"ipc-title__text"}).find_all("tr")