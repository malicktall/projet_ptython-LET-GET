import imp
import os
import pickle
from random import choice
from donnees import *
import time

def recup_scores():
    
    # Creer par Malick TALL
    """
        Objectif: Cette fonction récupère les scores enregistrés si le fichier existe.
        Methode: On va ouvrir le le fichier log_gote.txt et on enregistre le score 
        Besoins: le nom du fichier contenant les scores
        Connus: le fichier log_game.txt
        Entrées: fichier score sera donnees pour verifier le score total de l'utilisateur
        Sorties: elle ne retourne rien
        Résultats:on renvoie un dictionnaire, soit l'objet dépicklé, soit un dictionnaire vide.
        Hyphothèses: il faut faudra que le fichier log_game soit bien ouvert 
    
    """
    
    if os.path.exists(fichierScore): 
        
        fichier = open(fichierScore, "rb")
        mon_depickler = pickle.Unpickler(fichier)
        scores = mon_depickler.load()
        fichier.close()
    else: 
        scores = {}
    return scores


    
    
def enregistrer_scores(scores):
    
    # Creer par Malick TALL   
    """  
        Objectif: enregistrer les donnes dans le fichier log_game.txt
        Methode: Elle reçoit en paramètre le dictionnaire des scores à enregistrer
        Besoins: le score du gamer a la fin de la partie
        Connus: le fichier log_game.txt
        Entrées: fichier log_game.txt
        Sorties: pas de sortie
        Résultats: Cette fonction se charge d'enregistrer les scores dans le fichier log_game.txt
        Hyphothèses: il faut faudra que le fichier log_game soit bien ouvert 
    """
    fichier_scores = open(fichierScore, "wb") 
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()
    

    
def recup_lettre():
    # Creer par Sokhna Yade
    """   
      
        Objectif: Récupèrer une lettre saisie par l'utilisateur.
        Methode: on on demande a l'utilisateur d'entrer une lettre
        Besoins: la fonction lower pour ne pas avoir quelque chose de differant dans le fichier mots.txt
        Connus: rien d'avance
        Entrées: pas d'entree
        Sorties: envoie la lettre saisie 
        Résultats:envoie une lettre minuscule a la fonction main
        Hyphothèses: il faut que l'utilisateur emtre une lettre alphabet
    """
    lettre = input("Tapez une lettre: ")
    lettre = lettre.lower()
    return lettre

def choisir_mot(niveau):
    # Creer par Malick TALL
    """  
        Objectif: Recuperer un mot a deviner a partir du fichier mots.py
        Methode: Ouvrir le fichier et recuperer un mot au hazard avec le niveau choisie
        Besoins: le niveau que l'utilisateur souhaite jouer
        Connus: la liste des mots
        Entrées: le niveau
        Sorties: un mot
        Résultats: renvoie un resultat a deviner
        Hyphothèses: il faut faudra que le fichier log_game soit bien ouvert 
    """
    
    # print("le niveau est {0}".format(niveau))
    f = open('mots.txt', 'r' , encoding = 'utf8')
    contenu = f.readlines()
    mot = choice(contenu).lower().replace('\n','')
    # print("le mot est {0}".format(mot))
    if niveau == 1:
        while len(mot)>4:
            f.close()
            return choisir_mot(niveau)
        
        return mot
    elif niveau == 2:
        while len(mot)<5 or len(mot)>7:
            f.close()
            return choisir_mot(niveau)
        
        return mot
    elif niveau == 3:
        while len(mot)<7:
            f.close()
            return choisir_mot(niveau)
        
        return mot
    else:
        return ""
    

    

def recup_mot_masque(mot_complet, lettres_trouvees):  
    # Creer par Sokhna Yade
        
    """  
        Objectif: Obtenir un mot masque tout ou en partie
        Methode: recuperer une lettre et tester si elle est dans le mot ou pas
        Besoins: le mot complet et la lettre trouver 
        Connus: Rien
        Entrées:mot_complet et lettres_trouvees
        Sorties: on retour le mot masques
        Résultats: on montre les parties trouvees dans le mot masque
        Hyphothèses: il faudra que les valeurs envoyer soit un mot et une lettre alphbetique 
    """
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque


def recup_nom_utilisateur():
    # Creer par Sokhna Yade
    """Fonction chargée de récupérer le nom de l'utilisateur.
    Le nom de l'utilisateur doit être composé de 4 caractères minimum,
    chiffres et lettres exclusivement.
    Si ce nom n'est pas valide, on appelle récursivement la fonction
    pour en obtenir un nouveau"""
    nom_utilisateur = input("Tapez votre nom: ")
    
    
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() :
        print("Ce nom est invalide.")
        
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur
    

def isVoyelle(lettre):
    # Creer par Malick TALL
        
    """  
        Objectif: Tester si une lettre est  une voyelle ou un consonne
        Methode: recuperer une lettre et tester si c'est une voyelle ou nom
        Besoins:un lettre 
        Connus: la liste des voyelles
        Entrées: pas d'entree
        Sorties: 0 ou 1
        Résultats: renvoie 1 si c'est une voyelle 0 le cas contraire
        Hyphothèses: il faudra envoyer une lettre
    """
    
    voyelles = ['a', 'o', 'i', 'u', 'y', 'e']
    for voyelle in voyelles:
        if lettre==voyelle:
            return 1
    return 0    
            
            
            
def choixNiveau():
    # Creer par Malick TALL
    
   """  
        Objectif: Savoir quel niveau que l'utilisateur veut jouer
        Methode: on demande un chiffre a l'utilisateur et on lui affiche le niveau choisi
        Besoins:Un Chiffre 
        Connus: les trois niveaux
        Entrées: Un chiffre qui le niveau
        Sorties: le niveau
        Résultats: le niveau choisi
        Hyphothèses: il faudra que l'utilisateur entre un entier
   """

   niveau=input("\n\tchoississez un niveau: \n\t Niveau 1: 2-4 lettres à deviner \n\t Niveau 2: 5-7 lettre à deviner \n\t Niveau 3: plus de 7 lettres à deviner :")
   
   if niveau.isalpha():
       print("\n\t\t- Entrer un nombre !\n")
       return choixNiveau()
   
   niveau = int(niveau)
   if niveau<1 or niveau>3 :
        print("\t\t Ce niveau n'\existe pas !!!")
        return choixNiveau()
  
   if niveau == 1:
       print("Vous avez choisie le niveau {0}".format(niveau))
       chargementdesdonnes()
       return 1
   elif niveau ==2:
       print("Vous avez choisie le niveau {0}".format(niveau))
       chargementdesdonnes()
       return 2
   else:
       print("Vous avez choisie le niveau {0}".format(niveau))
       chargementdesdonnes()
       return 3
   
   
   
def chargementdesdonnes():
    # Creer par Sokhna Yade
    
    print("\nChargement des donnees", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1) 
    print("\n")
    chargement() 
   
def Affichage(nbr_chances, nbr_pointErreur):
    # Creer par Sokhna Yade
        
    """  
        Objectif: Afficher l'etat des points de l'utilisateur
        Methode: On recupere le nonbre de point de tentative et de point-ereeur puis on l'affiche.
        Besoins: On a besoin la valeur de nombre de tentative et de celle du poit-erreur
        Connus: Rien
        Entrées: nbr_chances et nb_pointErreur
        Sorties: Affichage des points
        Résultats: Affichage des oint
        Hyphothèses: il faudra envoyer des valeur correct de point tentative et de point erreur
    """
    print("\t\t\t##############################################\t\t\t")
    print("\t\t\t\tVous avez {0} point-erreur\t\t\t\t\t".format(nbr_pointErreur))
    print("\t\t\t##############################################\t\t\t")
    print("\t\t\t\tVous avez {0} tentative\t\t\t\t\t".format(nbr_chances))
    print("\t\t\t##############################################\t\t\t\n\n")
    var  = 'o'
  
    if nbr_chances == 5:
        print("   \t\t\t\t\t+----+\t\t\t\t")
        print("   \t\t\t\t\t|    |\t\t\t\t")
        print("   \t\t\t\t\to    |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t     ===========\t\t\t\t")
    elif nbr_chances == 4:
        print("   \t\t\t\t\t+----+\t\t\t\t")
        print("   \t\t\t\t\t|    |\t\t\t\t")
        print("   \t\t\t\t\to    |\t\t\t\t")
        print("   \t\t\t\t\t/    |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t\t     |\t\t\t\t")
        print("   \t\t\t\t     ===========\t\t\t\t")
    elif nbr_chances ==3:
        
        print("    \t\t\t\t\t +----+\t\t\t\t")
        print("    \t\t\t\t\t |    |\t\t\t\t")
        print("    \t\t\t\t\t o    |\t\t\t\t")
        print("  \t\t\t\t\t/|    |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print(" \t\t\t\t     ===========\t\t\t\t")
    elif nbr_chances == 2:
        print("    \t\t\t\t\t +----+\t\t\t\t")
        print("    \t\t\t\t\t |    |\t\t\t\t")
        print("    \t\t\t\t\t o    |\t\t\t\t")
        print("\t\t\t\t\t/|\   |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print(" \t\t\t\t     ===========\t\t\t\t")
    elif nbr_chances ==1:
        print("    \t\t\t\t\t +----+\t\t\t\t")
        print("    \t\t\t\t\t |    |\t\t\t\t")
        print("    \t\t\t\t\t o    |\t\t\t\t")
        print("\t\t\t\t\t/|\   |\t\t\t\t")
        print("  \t\t\t\t\t/     |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print("    \t\t\t\t\t      |\t\t\t\t")
        print(" \t\t\t\t     ===========\t\t\t\t")
    elif nbr_chances ==0 or nbr_chances==-1:
        print("    \t\t\t\t\t +---+\t\t\t\t")
        print("    \t\t\t\t\t |   |\t\t\t\t")
        print("    \t\t\t\t\t o   |\t\t\t\t")
        print("\t\t\t\t\t/|\  |\t\t\t\t")
        print(" \t\t\t\t\t/ \  |\t\t\t\t")
        print("    \t\t\t\t\t     |\t\t\t\t")
        print("    \t\t\t\t\t     |\t\t\t\t")
        print("    \t\t\t\t\t     |\t\t\t\t")
        print("    \t\t\t\t\t     |\t\t\t\t")
        print(" \t\t\t\t     ===========\t\t\t\t")
    else:
        print(" \t\t\t\t\t+---+\t\t\t\t")
        print(" \t\t\t\t\t|   |\t\t\t\t")
        print(" \t\t\t\t\t    |\t\t\t\t")
        print(" \t\t\t\t\t    |\t\t\t\t")
        print(" \t\t\t\t\t    |\t\t\t\t")
        print(" \t\t\t\t\t    |\t\t\t\t")
        print(" \t\t\t\t\t    |\t\t\t\t")
        print(" \t\t\t\t\t    |\t\t\t\t")
        print(" \t\t\t\t\t    |\t\t\t\t")
        print(" \t\t\t\t     ===========\t\t\t\t")
    
    
    
def chargement():
    # Creer par Malick TALL
        
    """  
        Objectif: Compter les nombre de la fichier
        Methode: Ouvrir le fichier et les donnes ligne par ligne
        Besoins:Le fichier mots.txt
        Connus:mots.txt
        Entrées:Rien
        Sorties:le nombre de mots dans le fichier
        Résultats: nombreMots
        Hyphothèses: il faudra bien ouvrir le fichier mots.txt
    """
    nombreMots = 0
    
    f = open('mots.txt', 'r' , encoding = 'utf8')
    contenus = f.readlines()
    for contenu in contenus:
        nombreMots +=1
    print("\n\t\t {0} mots charges".format(nombreMots))
      