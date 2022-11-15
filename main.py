
"""Ce fichier contient le jeu du pendu.

Il s'appuie sur les fichiers :
- donnees.py
- fonctions.py"""

import os
from donnees import *
from fonction import *

# Code Malick Tall et Sokhna Yade


Affichage(nombreTentative, point_erreur)
# chargement()

scores = recup_scores()
utilisateur = recup_nom_utilisateur()
if utilisateur not in scores.keys():
    scores[utilisateur] = 0 
    
niveau =  choixNiveau()
perdu = 0
continuer_partie = 0

while continuer_partie != 1:
    numeroParti += 1
    # arret = tempsArret(10)
    print("\t\tJoueur {0}: {1} point(s)".format(utilisateur, scores[utilisateur]))
    mot_a_trouver = choisir_mot(niveau)
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    nb_chances = nombreTentative
    nb_pointErreur = point_erreur

    while mot_a_trouver!=mot_trouve and nb_chances>0:
        print("\t\tMot à trouver {0} \n".format(mot_trouve))
        lettre = recup_lettre()
        if lettre in lettres_trouvees: 
            nb_pointErreur -= 1
            print("\t\tLettre déjà trouvé.\n")
           
            Affichage(nb_chances, nb_pointErreur)
        elif lettre in mot_a_trouver: 
            lettres_trouvees.append(lettre)
            print("\tBravo, lettre correcte")
        elif len(lettre)>1 :
            nb_pointErreur -=1
            print("\t\tVous devez saisir qu'un seul lettre. \n\t\t Vous perdez 1 point erreur.")
            Affichage(nb_chances, nb_pointErreur)
            
        elif not lettre.isalpha():
            nb_pointErreur -=1
            print("\t\tVous n'avez pas saisi une lettre valide,\n\t\t Vous perdez un point erreur\n .")
            
            if nb_pointErreur == 0:
                nb_pointErreur =3
                nb_chances -=1
            Affichage(nb_chances, nb_pointErreur)  
        else:
            if isVoyelle(lettre)==1:
                print("\t\tVous avez saisi une voyelle qui n'est pas dans le mot.\n\t\t Vous perdez deux tentatives\n")
                nb_chances -= 2
                Affichage(nb_chances, nb_pointErreur)
            else:
                print("\t\tVous avez saisi un cosonne qui n'est pas dans le mot.\n\t\t Vous perdez 1 tentative\n")
                nb_chances -=1
                Affichage(nb_chances, nb_pointErreur)
        
            
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    
    if mot_a_trouver!=mot_trouve:
        print("\t\t\t Vous avez perdu le mot a deviner etait {0}.".format(mot_a_trouver))
        continuer_partie = input("Souhaitez-vous continuer la partie taper 0 pour continuer et 1 pour quitter ?")
        continuer_partie = int(continuer_partie)
    else:
        continuer_partie = 1
        print("\t\tFélicitation : Vous avez deviné le mot: {0}.".format(mot_a_trouver))
        
        scoreParti = nb_chances * len(mot_a_trouver)
        
        
    
        perdu = 1
        print("\t\tVous score est {0}. \n\n Votre score total est passer de {1} a {2}".format(scoreParti,scores[utilisateur],scores[utilisateur]+scoreParti))
        
        scores[utilisateur] += scoreParti
        enregistrer_scores(scores)

    
if perdu == 0:
    print("\t\t\t\tVotre score {0} n\'as pas changé ".format(scores[utilisateur]))      
    
print("\t\t\t------------------Merci d'avoir joué à bientot----------------------")      
 




