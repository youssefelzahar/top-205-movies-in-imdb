import csv
from itertools import zip_longest
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}
url=requests.get("https://www.imdb.com/chart/top/")

src=url.content
soup=BeautifulSoup(src,"lxml")
titles_list=[]
names_diractors=[]
links=[]
gross_list=[]
history_list=[]
nomation_list=[]
budget_list=[]
opne_us_ca_list=[]
gross_us_list=[]
titles=soup.find_all("td",{"class":"titleColumn"})
for i in range(len(titles)):
    titles_list.append(titles[i].find("a").text.strip())
    names_diractors.append(titles[i].find("a").attrs["title"])
    links.append("https://www.imdb.com/"+titles[i].find("a").attrs["href"])
    history_list.append(titles[i].find("span",{"class":"secondaryInfo"}).text.strip())

print(names_diractors)    


for link in links:
    result=requests.get(link,headers=headers)
    src=result.content
    new_soup=BeautifulSoup(src,"lxml")
    nomation=new_soup.find("label",{"class":"ipc-metadata-list-item__list-content-item"}).text
    nomation_list.append(nomation)
    budget=new_soup.find("li",{"class":"ipc-metadata-list__item sc-6d4f3f8c-2 byhjlB","data-testid":"title-boxoffice-budget"}).text
    budget_list.append(budget)
    allgross=new_soup.find("li",{"data-testid":"title-boxoffice-cumulativeworldwidegross"})
    gross_list.append(allgross)
    grossus=new_soup.find("li",{"data-testid":"title-boxoffice-grossdomestic"})
    gross_us_list.append(grossus)
    open=new_soup.find("li",{"data-testid":"title-boxoffice-openingweekenddomestic"})
    opne_us_ca_list.append(open)


    
print(nomation_list,budget_list,gross_list,gross_us_list,opne_us_ca_list)