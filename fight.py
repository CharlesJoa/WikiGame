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
            title = title.replace("<i>", "").replace("</i>", "")
            links.append(title)
            
        for anchor in soup.find_all('div', {"class":"mw-parser-output"}):
            for toto in anchor.find_all('a'):
                titi = str(toto.get('href')).replace("/wiki/","").replace("%27","'").replace("%C3%A8","è").replace("%C3%A9","é").replace('%C3%AA','ê').replace('%C3%A7','ç').replace('%C3%A0','à').replace('%C3%B4','ô').replace('%C3%89','É')
                if not ('/w/') in titi:
                    if not ('#') in titi:
                        if not ('Fichier') in titi:
                            if not ('http') in titi:
                                if not ('Modèle') in titi:
                                    links.append(titi)
                        
        return links

def afficheTableau(tab,deb,fin):
    i=1
    for indice in range(deb,fin):
        print('{} - {}'.format(indice,tab[indice]))
        i+=1

try :
    success = False
    r = recherche('https://fr.wikipedia.org/wiki/Les_Vacances_de_monsieur_Hulot')
    tour = 0
    deb=1
    fin=21
    while not success:
        print('************************ WikiGame **** tour {}'.format(tour))
        print('Actuellement : {}'.format(r[0]))
        print('00 - Retour /')
        afficheTableau(r,deb,fin)
        print('98 - Voir les liens précédents /')
        print('99 - Voir la suite /')
        nvpage = int(input('Votre choix : '))
        if nvpage == 0:
            # do retour
            i=0
        elif nvpage == 99:
            if deb+20 > len(r):
                deb = fin+1
                fin += len(r)-fin
            else:
                deb+=20
                fin+=20
            afficheTableau(r,deb,fin)
        elif nvpage == 98:
            if not deb==1 :
                deb-=20
                fin-=20
            afficheTableau(r,deb,fin)
        else:
            rn = recherche('https://fr.wikipedia.org/wiki/{}'.format(r[nvpage]))
            tour+=1
        
    # afficheTableau(recherche('https://fr.wikipedia.org/wiki/Les_Vacances_de_monsieur_Hulot'))
    # r1 = recherche('https://fr.wikipedia.org/wiki/Les_Vacances_de_monsieur_Hulot')
    # r2 = recherche('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
except:
    print('Saisir correctement les parametres')
    exit(1)

# print(r1)
# print(r2)