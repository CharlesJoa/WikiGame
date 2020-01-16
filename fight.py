#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PG avec un param
# forger une url : https://www.ecosia.org/search?q=batman
# scrap la page et recup le nb de resultats id=resultStats
# soup.find("div", {"id": "articlebody"})

# TODO Gérer les titres avec des exposants

from bs4 import BeautifulSoup
import urllib.request
import sys


def recherche(arg): # Je crée la fonction
    links = []
    with urllib.request.urlopen(arg) as response:
        webpage = response.read() #Crée une chaine de caractère avec tout le code source
        soup = BeautifulSoup(webpage, 'html.parser')
        print(soup.title.string[0:len(soup.title.string)-12])
        for toto in soup.find_all('h1', {"class":"firstHeading"}): #get the title of the page
            title = str(toto.contents[0])
            title = title.replace("<i>", "").replace("</i>", "")
            links.append(title)
            
        for anchor in soup.find_all('div', {"class":"mw-parser-output"}):
            for toto in anchor.find_all('a'):
                titi = formatage(str(toto.get('href')))
                if not ('/w/') in titi:
                    if not ('#') in titi:
                        if not ('Fichier:') in titi:
                            if not ('http:') in titi:
                                if not ('https:') in titi:
                                    if not ('Modèle:') in titi:
                                        if not ('/API') in titi:
                                            links.append(titi.replace("/wiki/",""))
                        
        return links

# def getTitleURL(page):
def formatage(arg):
    return arg.replace("%20"," ").replace("%27","'").replace("%C3%A8","è").replace("%C3%A9","é").replace('%C3%AA','ê').replace("%C3%A2","â").replace("%C3%B",'ü').replace("%C3%AC","ì").replace('%C3%A7','ç').replace('%C3%A0','à').replace('%C3%B4','ô').replace('%C3%89','É').replace("%C3%AF","ï")

def formatageInverse(arg):
    return arg.replace(" ","%20").replace("'","%27").replace("è","%C3%A8").replace("é","%C3%A9").replace('ê','%C3%AA').replace("â","%C3%A2").replace('ü',"%C3%B").replace("ì","%C3%AC").replace('ç','%C3%A7').replace('à','%C3%A0').replace('ô','%C3%B4').replace('É','%C3%89').replace("ï","%C3%AF")

def afficheTableau(tab,deb,fin):
    i=1
    for indice in range(deb,fin):

        print('{} - {}'.format(indice,tab[indice]))

        i+=1

try :
    success = False
    r = recherche('https://fr.wikipedia.org/wiki/Capitale_de_la_France')
    origine = r[0]
    r2 = recherche('https://fr.wikipedia.org/wiki/Paris')
    tour = 0
    page=1
    old="NULL"
    
    while not success:

        deb = ((page-1)*20)+1
        fin=deb+20
        print('************************ WikiGame **** tour {}'.format(tour))
        print('Départ :{}'.format(origine))
        print('Cible : {}'.format(r2[0]))
        print('Actuellement : {}'.format(r[0]))
        print('00 - Retour /')
        afficheTableau(r,max(1,deb),min(fin, len(r)))
        print('98 - Voir les liens précédents /')
        print('99 - Voir la suite /')
        nvpage = int(input('Votre choix : '))
        if nvpage == 0:
            if tour == 0:
                print("Vous ne pouvez pas faire retour lors du premier tour")
            else:
                r = recherche('https://fr.wikipedia.org/wiki/{}'.format(old))
        elif nvpage == 99:
            if fin<len(r):
                page+=1
        elif nvpage == 98:
            if deb >1:
                page-=1

        else:
            # reformatage pour repasser dans l'URL
            old = formatageInverse(r[0])
            toto ='https://fr.wikipedia.org/wiki/{}'.format(formatageInverse(r[nvpage]))
            r = recherche('https://fr.wikipedia.org/wiki/{}'.format(formatageInverse(r[nvpage])))
            tour+=1

        if r[0] == r2[0]:
            success=True
            print('Bravo tu as reussi en {} coups'.format(tour))

        
    # afficheTableau(recherche('https://fr.wikipedia.org/wiki/Les_Vacances_de_monsieur_Hulot'))
    # r1 = recherche('https://fr.wikipedia.org/wiki/Les_Vacances_de_monsieur_Hulot')
except:
    print('Saisir correctement les parametres')
    exit(1)
