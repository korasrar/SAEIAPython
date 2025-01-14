# coding: utf-8
"""
            SAE1.02 SERPIUT'O
        BUT1 Informatique 2024-2025

    Module IA.py
    Ce module implémente toutes les fonctions ainsi que l'IA de votre serpent
"""

import partie
import argparse
import client
import random
import arene
import serpent
direction_prec='X' # variable indiquant la décision précédente prise par le joueur. A mettre à jour soi-même

####################################################################
### A partir d'ici, implémenter toutes les fonctions qui vous seront 
### utiles pour prendre vos décisions
### Toutes vos fonctions devront être documentées
####################################################################

def directions_possibles(l_arene:dict,num_joueur:int,coordone:tuple=())->str:
    """Indique les directions possible pour le joueur num_joueur
        c'est à dire les directions qu'il peut prendre sans se cogner dans
        un mur, sortir de l'arène ou se cogner sur une boîte trop grosse pour sa tête

    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur

    Returns:
        str: une chaine composée de NOSE qui indique les directions
            pouvant être prise par le joueur. Attention il est possible
            qu'aucune direction ne soit possible donc la fonction peut retourner la chaine vide
    """    
    res = ''
    if coordone != ():
        for direction in arene.DIRECTIONS.keys():
            if not arene.est_mur(l_arene, coordone[0] + arene.DIRECTIONS[direction][0], coordone[1] + arene.DIRECTIONS[direction][1]):
                res += direction
    else:
        position = arene.get_serpent(l_arene, num_joueur)[0]
        for direction in arene.DIRECTIONS.keys():
            if not arene.est_mur(l_arene, position[0] + arene.DIRECTIONS[direction][0], position[1] + arene.DIRECTIONS[direction][1]):
                res += direction
    return res

def objets_voisinage(l_arene:dict, num_joueur, dist_max:int):
    """Retourne un dictionnaire indiquant pour chaque direction possibles, 
        les objets ou boites pouvant être mangés par le serpent du joueur et
        se trouvant dans voisinage de la tête du serpent 

    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur considéré
        dist_max (int): le nombre de cases maximum qu'on s'autorise à partir du point de départ
    Returns:
        dict: un dictionnaire dont les clés sont des directions  et les valeurs une liste de triplets
            (distance,val_objet,prop) où distance indique le nombre de cases jusqu'à l'objet et id_objet
            val_obj indique la valeur de l'objet ou de la boite et prop indique le propriétaire de la boite
    """
    dir_possibles = directions_possibles(l_arene,num_joueur)
    val_obj = 0
    prop = 0
    coordo = ()
    coordo_serpent = ()
    dict_voisins = {}
    for direction in dir_possibles :
        coordo_serpent = arene.get_serpent(l_arene,num_joueur)[0]
        coordo = (coordo_serpent[0]+arene.DIRECTIONS[direction][0],coordo_serpent[1]+arene.DIRECTIONS[direction][1])
        val_obj = arene.get_val_boite(coordo)
        prop = arene.get_proprietaire(l_arene,coordo[0],coordo[1])
        distance = ...
        dict_voisins[direction] = [distance,val_obj,prop]
    return dict_voisins

distance = 0

def inondations(l_arene:dict,num_joueur:int,direction_possibles:str,dist_max:int):
    arene_calque = arene.copy_arene(l_arene)
    set_position = set()
    #for direction in direction_possibles:   
    """while distance < dist_max and direction_possibles != direction_prec :
        for direction in direction_possibles:
            coordo_serpent = arene.get_serpent(l_arene,num_joueur)[0]
            coordone_direction = (coordo_serpent[0]+arene.DIRECTIONS[direction][0],coordo_serpent[1]+arene.DIRECTIONS[direction][1])
            direction_prec = (coordone_direction[0],coordone_direction[1])
            inondations(l_arene,num_joueur,direction_possibles(l_arene,num_joueur,coordone_direction))
    """
    list_direction_possible = direction_possibles
    list_new_direction = []
    val_obj = 0
    dico_voisins = {}
    while distancle != 5:
        distance += 1
        for direction in list_direction_possibles:
            coordo_serpent = arene.get_serpent(l_arene,num_joueur)[0]
            coordo = (coordo_serpent[0]+arene.DIRECTIONS[direction][0],coordo_serpent[1]+arene.DIRECTIONS[direction][1])
            val_obj = arene.get_val_boite(coordo)
            if arene.est_bonus(l_arene,coordo[0],coordo[1]):
                dico_voisins[]


    for direction in direction_possibles :
        coordo_serpent = arene.get_serpent(l_arene,num_joueur)[0]
        coordone_direction = (coordo_serpent[0]+arene.DIRECTIONS[direction][0],coordo_serpent[1]+arene.DIRECTIONS[direction][1])
        direction_prec = (coordone_direction[0],coordone_direction[1])
            val_obj = arene.get_val_boite(coordo)
            if val_obj > 0:
                dict_inondation[direction].append((distance, val_obj, prop))
        while distance < dist_max :
            inondations


    arene_calque = arene.copy_arene(l_arene)
    dict_inondation = {}
    for direction in direction_possibles:
        coordo_serpent = arene.get_serpent(l_arene, num_joueur)[0]
        coordo = coordo_serpent
        distance = 0
        val_obj = arene.get_val_boite(coordo)
            if val_obj > 0:
                dict_inondation[direction].append((distance, val_obj, prop))

        while distance < dist_max:
            inondations
            
    return dict_inondation

    direction_possibles = []
    str_past_direction = ''
    distance
    for direction in new_dir_possible:
        coordo_serpent = arene.get_serpent(l_arene,num_joueur)[0]
        coordone_direction = (coordo_serpent[0]+arene.DIRECTIONS[direction][0],coordo_serpent[1]+arene.DIRECTIONS[direction][1])
        new_dir_possible = direction_possibles(l_arene,num_joueur,coordone_direction[0],coordone_direction[1])
        str_past_direction += direction
        while distance < dist_max :
            inondations()
            

    val_obj = 0
    prop = 0
    distance = 0
    str_direction_possible = direction_possibles(le_plateau,position_depart)
    coordo_serpent = arene.get_serpent(l_arene,num_joueur)[0]
    str_ancienne_direction = ''
    set_future_voisins = set()
    dict_voisinages = {}
    check = False
    while not check:
        distance += 1
        for direction in str_direction_possible:
            coordone_direction = (coordo_serpent[0]+arene.DIRECTIONS[direction][0],coordo_serpent[1]+arene.DIRECTIONS[direction][1])
            val_obj = arene.get_val_boite(coordone_direction)
            str_ancienne_direction += direction
            if arene.est_bonus(val_obj) :
                dict_voisinages[str_ancienne_direction] = [distance,val_obj,prop]
                set_future_voisins = directions_possibles(l_arene,num_joueur,coordone_direction) 
            if distance < dist_max or :
                    check = True
        set_position_voisins = set_future_voisins
        set_future_voisins = set()
    return plateau_claque
print(fabrique_le_calque(plateau_test,(4,2)))
ind

def mon_IA2(num_joueur:int, la_partie:dict)->str:
    return 'N'

def mon_IA(num_joueur:int, la_partie:dict)->str:
    """Fonction qui va prendre la decision du prochain coup pour le joueur de numéro ma_couleur

    Args:
        num_joueur (int): un entier désignant le numero du joueur qui doit prendre la décision
        la_partie (dict): structure qui contient la partie en cours

    Returns:
        str: une des lettres 'N', 'S', 'E' ou 'O' indiquant la direction que prend la tête du serpent du joueur
    """
    direction=random.choice("NSEO")
    direction_prec=direction #La décision prise sera la direction précédente le prochain tour
    dir_pos=arene.directions_possibles(partie.get_arene(la_partie),num_joueur)
    if dir_pos=='':
        direction=random.choice('NOSE')
    else:
        direction=random.choice(dir_pos)
    return direction

if __name__=="__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("--equipe", dest="nom_equipe", help="nom de l'équipe", type=str, default='Non fournie')
    parser.add_argument("--serveur", dest="serveur", help="serveur de jeu", type=str, default='localhost')
    parser.add_argument("--port", dest="port", help="port de connexion", type=int, default=1111)
    
    args = parser.parse_args()
    le_client=client.ClientCyber()
    le_client.creer_socket(args.serveur,args.port)
    le_client.enregistrement(args.nom_equipe,"joueur")
    ok=True
    while ok:
        ok,id_joueur,le_jeu,_=le_client.prochaine_commande()
        if ok:
            la_partie=partie.partie_from_str(le_jeu)
            actions_joueur=mon_IA(int(id_joueur),la_partie)
            le_client.envoyer_commande_client(actions_joueur)
    le_client.afficher_msg("terminé")