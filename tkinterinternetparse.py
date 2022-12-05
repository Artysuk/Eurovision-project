import requests
from bs4 import BeautifulSoup

def võitjate_parsimine():
    url = requests.get("http://www.eurovisioon.ee/voitjad.php").text
    soup = BeautifulSoup(url,'lxml')
    tabel = soup.find('div',{'class':'col-md-8'})
    v = []
    #parsimise osa
    for row in tabel.find_all("div", class_="caption"):
        k = row.find_all('h3')[0]
        k = k.text.replace('.',' -').replace(' ',' - ',1)
        k = k.strip().split(" - ")
        k2 = row.find_all('p')[0]
        k.append(k2.text.strip())
        v.append(k)
    #tulemuse parandamise osa
    for i in range(len(v)):
        del v[i][1]
        for e in range(len(v[i])):
            if "\\" in r"%r" % v[i][e]:
                v[i][e] = r"%r" % v[i][e]
                v[i][e] = v[i][e].replace("\\x8a", "Š").replace("\\x9e", "ž")
    return v