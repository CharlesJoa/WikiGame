#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import sys
import os 
import pickle

def recherche(arg): # Je crée la fonction
    links = []
    with urllib.request.urlopen(arg) as response:
        webpage = response.read() #Crée une chaine de caractère avec tout le code source
        soup = BeautifulSoup(webpage, 'html.parser')
        # print(soup.title.string[0:len(soup.title.string)-12])
        for toto in soup.find_all('h1', {"class":"firstHeading"}): #get the title of the page
            title = str(toto.contents[0])
            # S'il y a des valeurs en exposants (ex:1er)
            if 'abbr' in str(toto.contents[0]):
                title = str(toto.contents[0].contents[0])+str(toto.contents[0].contents[1].contents[0])+str(toto.contents[1])

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
                                            if not ('Spécial:') in titi:
                                                if not ('Catégorie:') in titi:
                                                    if not ('Portail:') in titi:
                                                        links.append(titi.replace("/wiki/",""))
                        
        return links

# def getTitleURL(page):
def formatage(arg):
    return arg.replace("%20"," ").replace("%27","'").replace("%C3%A8","è").replace("%C3%A9","é").replace('%C3%AA','ê').replace("%C3%A2","â").replace("%C5%93","œ").replace("%C3%B",'ü').replace("%C3%AC","ì").replace('%C3%A7','ç').replace('%C3%A0','à').replace('%C3%B4','ô').replace('%C3%89','É').replace("%C3%AF","ï")

try:
    r=recherche('https://fr.wikipedia.org/wiki/{}'.format(sys.argv[1]))
    with open('donnees.txt', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(r)


except:
    print("saisir correctement les paramètres")