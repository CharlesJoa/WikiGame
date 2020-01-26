#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PG avec un param
# forger une url : https://www.ecosia.org/search?q=batman
# scrap la page et recup le nb de resultats id=resultStats
# soup.find("div", {"id": "articlebody"})

# TODO Gérer les titres avec des exposants + Gerer le cas ou on saisit nvpage qui n'a pas d'élément a cet index + test le clear sur Linux

from bs4 import BeautifulSoup
import urllib.request
import sys
import os 
import pickle
from random import randint
from tkinter import *







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
                                                    links.append(titi.replace("/wiki/",""))
                        
        return links

def clears():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')


# def getTitleURL(page):
def formatage(arg):
    return arg.replace("%20"," ").replace("%27","'").replace("%C3%A8","è").replace("%C3%A9","é").replace('%C3%AA','ê').replace("%C3%A2","â").replace("%C5%93","œ").replace("%C3%B",'ü').replace("%C3%AC","ì").replace('%C3%A7','ç').replace('%C3%A0','à').replace('%C3%B4','ô').replace('%C3%89','É').replace("%C3%AF","ï")

def formatageInverse(arg):
    return arg.replace(" ","%20").replace("'","%27").replace("è","%C3%A8").replace("é","%C3%A9").replace('ê','%C3%AA').replace("â","%C3%A2").replace("œ","%C5%93").replace('ü',"%C3%B").replace("ì","%C3%AC").replace('ç','%C3%A7').replace('à','%C3%A0').replace('ô','%C3%B4').replace('É','%C3%89').replace("ï","%C3%AF")

def afficheTableau(tab,deb,fin):
    i=1
    for indice in range(deb,fin):

        tableau=Label(Fenetre,text=('{} - {}'.format(indice,tab[indice])))
        tableau.pack()
        i+=1
        

# Main()

try :
    
    success = False
    if len(sys.argv) == 1:
        r = recherche('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
        r2 = recherche('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
    # Recherche par Portail
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-p':
            with open('donnees.txt', 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                tab_recupere = mon_depickler.load()
            line_max = len(tab_recupere)
            val1 = randint(0, line_max)
            val2 = randint(0, line_max)
            r = recherche('https://fr.wikipedia.org/wiki/{}'.format(tab_recupere[val1]))
            r2 = recherche('https://fr.wikipedia.org/wiki/{}'.format(tab_recupere[val2]))
    elif len(sys.argv) == 3:
        # recherche specifique
        if sys.argv[1] == '-s':
            urls_to_search = sys.argv[2]
            urls_to_search = urls_to_search.split('+')
            r =recherche('https://fr.wikipedia.org/wiki/{}'.format(urls_to_search[0]))
            r2 =recherche('https://fr.wikipedia.org/wiki/{}'.format(urls_to_search[1]))
    
    origine = r[0]
    tour = 0
    page=1
    old=""
    
    while not success:
        deb = ((page-1)*20)+1
        fin=deb+20
        Fenetre = Tk()
        Fenetre.title('************************ WikiGame **** tour {}'.format(tour))
        Fenetre.geometry('900x900+100+100')
        #print('************************ WikiGame **** tour {}'.format(tour))
        
       
        depart=Label(Fenetre,text='Départ :{}'.format(origine))
        depart.pack()
        
        #print('Départ :{}'.format(origine))
        
        
        cible=Label(Fenetre,text='Cible : {}'.format(r2[0]))
        cible.pack()
        
        #print('Cible : {}'.format(r2[0]))
        actu=Label(Fenetre,text='Actuellement : {}'.format(r[0]))
        actu.pack()
        
        #print('Actuellement : {}'.format(r[0]))
        retour=Label(Fenetre,text='0 - Retour /')
        retour.pack()
        #print('0 - Retour /')
        
        afficheTableau(r,max(1,deb),min(fin, len(r)))
        
        precedent=Label(Fenetre,text="98 Voir les liens précédents /")
        precedent.pack()
        
        #print('98 - Voir les liens précédents /')
        suite=Label(Fenetre,text="99 Voir les liens suivants /")
        suite.pack()
       
        #print('99 - Voir la suite /')
        boutonF=Button(Fenetre, text="Fermer", command=Fenetre.quit)
        boutonF.pack(side=BOTTOM)
        Fenetre.mainloop()
        nvpage =input('Votre choix : ')
        
        if nvpage > len(r):
            print('Il n\'y a pas de lien pour ce numéro')
        else:
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
                #Remise à 1 de la page pour afficher la première de la nouvelle recherche et eviter de chercher une page qui n'existe pas
                page=1
                # reformatage pour repasser dans l'URL
                old = formatageInverse(r[0])
                toto ='https://fr.wikipedia.org/wiki/{}'.format(formatageInverse(r[nvpage]))
                r = recherche('https://fr.wikipedia.org/wiki/{}'.format(formatageInverse(r[nvpage])))
                tour+=1
                clears()

        if r[0] == r2[0]:
            success=True
            print('Bravo tu as reussi en {} coups'.format(tour))
        
        
    # afficheTableau(recherche('https://fr.wikipedia.org/wiki/Les_Vacances_de_monsieur_Hulot'))
    # r1 = recherche('https://fr.wikipedia.org/wiki/Les_Vacances_de_monsieur_Hulot')
except:
    print('Saisir correctement les parametres')
    exit(1)


#Generation de la fenetre principale





#Widget 1 Fenetre principale

#Widget 2 Fenetre principale



