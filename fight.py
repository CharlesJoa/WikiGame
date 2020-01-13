# PG avec un param
# forger une url : https://www.ecosia.org/search?q=batman
# scrap la page et recup le nb de resultats id=resultStats
# soup.find("div", {"id": "articlebody"})

from bs4 import BeautifulSoup
import urllib.request
import sys

def recherche(arg): # Je crée la fonction
    with urllib.request.urlopen('https://www.ecosia.org/search?q={}'.format(arg)) as response:
        webpage = response.read() #Crée une chaine de caractère avec tout le code source
        soup = BeautifulSoup(webpage, 'html.parser')
        for anchor in soup.find_all("span",{"class":"result-count"}):
            return int(anchor.contents[0].replace("\n","").replace("\r","").replace(" ","").replace(",",""))
    
try :
    r1 = recherche(sys.argv[1].replace(" ","%20").replace("'","%27")) #formatage des espaces et ' pour la recherche
    r2 = recherche(sys.argv[2].replace(" ","%20").replace("'","%27"))
except:
    print('Saisir correctement les parametres')
    exit(1)

if(r1>r2):
    print("{} gagne ({:03.1f}%)".format(sys.argv[1].replace("%20"," ").replace("%27","'"),(r1/(r1+r2)*100))) #deformatage SPACE et '
else:
    print("{} gagne ({:03.1f}%)".format(sys.argv[2].replace("%20"," ").replace("%27","'"),(r2/(r1+r2)*100)))