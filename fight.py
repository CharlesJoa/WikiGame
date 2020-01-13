# PG avec un param
# forger une url : https://www.ecosia.org/search?q=batman
# scrap la page et recup le nb de resultats id=resultStats
# soup.find("div", {"id": "articlebody"})

from bs4 import BeautifulSoup
import urllib.request
import sys

def recherche(arg): # Je crée la fonction
    links = []
    with urllib.request.urlopen(arg) as response:
        webpage = response.read() #Crée une chaine de caractère avec tout le code source
        soup = BeautifulSoup(webpage, 'html.parser')
        for toto in soup.find_all('h1', {"class":"firstHeading"}): #get the title of the page
            title = str(toto.contents[0])
            print(title.replace("<i>", "").replace("</i>", ""))
            
        for anchor in soup.find_all('div', {"class":"mw-parser-output"}):
            for toto in anchor.find_all('a'):
                links.append(toto.get('href'))
        return links

try :
    r1 = recherche('https://fr.wikipedia.org/wiki/Les_Vacances_de_monsieur_Hulot')
    # r2 = recherche('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
except:
    print('Saisir correctement les parametres')
    exit(1)

print(r1)
# print(r2)