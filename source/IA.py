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
import case
import random
import arene
import serpent
direction_prec='X' # variable indiquant la décision précédente prise par le joueur. A mettre à jour soi-même

####################################################################
### A partir d'ici, implémenter toutes les fonctions qui vous seront 
### utiles pour prendre vos décisions
### Toutes vos fonctions devront être documentées
####################################################################

def est_pas_mur(l_arene, lgn, col, direction):
    if not arene.est_mur(l_arene, lgn + arene.DIRECTIONS[direction][0], col + arene.DIRECTIONS[direction][1]):
        return True
    return False

def est_pas_sortie(lgn_tete, col_tete, lgn_are, col_are, direction):
    if lgn_tete + arene.DIRECTIONS[direction][0] > 0 and lgn_tete + arene.DIRECTIONS[direction][0] < lgn_are:
        if col_tete + arene.DIRECTIONS[direction][1] > 0 and col_tete + arene.DIRECTIONS[direction][1] < col_are:
            return True
    return False

def directions_possibles(l_arene:dict,coordonnees:tuple)->str:
    """Indique les directions possible pour le joueur num_joueur
        c'est à dire les directions qu'il peut prendre sans se cogner dans
        un mur, sortir de l'arène ou se cogner sur une boîte trop grosse pour sa tête

    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur

    Returns:
        dict: 
    """ 
    lgn = arene.get_dim(l_arene)[0]
    col = arene.get_dim(l_arene)[1]
    res = ''
    tete_lgn = coordonnees[0]  
    tete_col = coordonnees[1]
    for direction in arene.DIRECTIONS:
        if est_pas_sortie(tete_lgn, tete_col,lgn,col,direction):
            if est_pas_mur(l_arene, tete_lgn, tete_col, direction):
                res += direction
    res = dico_finale(res, tete_lgn, tete_col)
    return res

def dico_finale(direc_pos, lgn_tete, col_tete):
    dico = {}
    dico["direction"] = direc_pos
    dico["coordonnees"] = set()
    for direct in direc_pos:
        dico["coordonnees"].add((lgn_tete + arene.DIRECTIONS[direct][0], col_tete + arene.DIRECTIONS[direct][1]))
    return dico

def objets_voisinage(l_arene:dict,num_joueur:int,dist_max:int):
    """Retourne un ensemble de coordonées accessibles par rapport a dist_max
    Args:
        l_arene (dict): l'arène considérée
        num_joueur (int): le numéro du joueur considéré
        dist_max (int): le nombre de cases maximum qu'on s'autorise à partir du point de départ
    Returns:
        set: un ensemble avec les coordonées accessibles par le serpent
    """
    def create_dico_bonus(l_arene:dict,set_position_bonus:tuple):
        """Créer un dictionnaire a partir des position des bonus

        Args:
            l_arene (dict): dict de l'arène
            set_position_bonus (tuple): ensemble de position des bonus

        Returns:
            dict: dictionnaire des positions des bonus ex -> {-2:(x,y),1:(x,y),...}
        """        
        dico_bonus = {}
        for pos_bonus in set_position_bonus:
            val_bonus = arene.get_val_boite(l_arene,pos_bonus[0],pos_bonus[1])
            if val_bonus not in dico_bonus:
                dico_bonus[val_bonus] = pos_bonus
        return dico_bonus
    distance = 0
    position_serpent = arene.get_serpent(l_arene,num_joueur)
    tete_serpent = position_serpent[0]
    str_direction_voisin = directions_possibles(l_arene,tete_serpent)["direction"]
    set_position_voisin = directions_possibles(l_arene,tete_serpent)["coordonnees"]
    set_future_voisins = directions_possibles(l_arene,tete_serpent)["coordonnees"]
    set_position_bonus = set()
    check = False
    while not check:
        distance += 1
        set_voisin_temp = set()
        for position in set_future_voisins:
            voisin_pos = directions_possibles(l_arene,position)["coordonnees"]
            set_voisin_temp|=voisin_pos
        if distance >= dist_max:
            check = True
        set_future_voisins = set_voisin_temp
        set_position_voisin|=set_voisin_temp
    for bonus in set_position_voisin:
            if arene.est_bonus(l_arene,bonus[0],bonus[1]) or arene.get_val_boite(l_arene,bonus[0],bonus[1]) > 0 and arene.get_proprietaire(l_arene,bonus[0],bonus[1]) != num_joueur: 
                set_position_bonus.add(bonus)
    set_position_voisin = set()
    return create_dico_bonus(l_arene,set_position_bonus)


# verif serpent

# ---------------------------------------------------------------------------

#{keys: valeur_bonus valeur: coordonnees}:

def avancer_tour(la_partie:dict,dico_info:dict):
    """_summary_

    Args:
        la_partie (dict): _description_
        dico_info (dict): _description_

    Returns:
        _type_: _description_
    """   
    score_tete = arene.get_val_boite(dico_info["arene"],dico_info["positions"][0][0],dico_info["positions"][0][1]) 
    temps_restant = partie.get_temps_restant(la_partie)
    #if score_tete < 2:
    if temps_restant <= 150:
        return strategie_1(dico_info)
        
""" elif temps_restant >=50 and temps_restant < 100:
        return strategie_2(dico_info)
    else:  
        pass"""
    

def est_ateignable(pos_bonus:tuple,dico_info:dict,chemin_bonus:list):
    """Vérifie si la case est atteignable en fonction du temps restants du bonus dans l'arene,
        de si il y a un serpent avec une queue score plus grande que notre tête

    Args:
        pos_bonus (tuple): coordonées du bonus
        dico_info (dict): dico info
        chemin_bonus (list): liste de coordonées pour arriver au bonus

    Returns:
        bool: True si atteignable, False sinon
    """    
    #temps de vie restant 
    temps_restant_case_bonus = dico_info["arene"]["matrice"]["valeurs"][pos_bonus]["temps_restant"]
    if len(chemin_bonus) < temps_restant_case_bonus:
        return True
    return False
    #maybe serpent autour
    #objet qu'on veut pas prendre 
    

def prio_strategie_1(l_arene:dict, num_joueur:int,dico_info:dict ): #ordre de prise des bonus pour les 50 premier tours
    """permet de connaître l'odre des bonus à aller chercher dans l'odre d'inportance croissant

    Args:
        l_arene (dict): dico de l'arene
        num_joueur (int): numéro du joueur

    Returns:
        list: ordre des bonus à aller chercher dans l'ordre d'importance   
    """    
    ordre = []
    score_tete = arene.get_val_boite(l_arene,dico_info["positions"][0][0],dico_info["positions"][0][1])
    if score_tete < 2:
        ordre.append(1)
        return ordre
    else:
        ordre.append(2,1,-2,-1)
        return ordre


"""def prio_strategie_2(): #ordre de prise des bonus de 100 à 150 tours
        permet de connaître l'odre des bonus à aller chercher dans l'odre d'inportance croissant

    Args:
        l_arene (dict): dico de l'arene
        num_joueur (int): numéro du joueur

    Returns:
        list: ordre des bonus à aller chercher dans l'ordre d'importance   
      
    ordre = []
    ordre.append(2,-2,-1,1)
    return ordre"""    


def strategie_1(dico_info:dict):
    """Renvoie la direction a prendre en fonction de la stratégie durant les 50 premiers tours

    Args:
        dico_info (dict): dico info

    Returns:
        str: La direction a prendre pour le serpent
    """    
    prio_ordre = prio_strategie_1(dico_info["arene"],dico_info["num_joueur"],dico_info)
    #chemin_prio = dico_info["objets_voisins"][prio_ordre][0]
    object_choisie = 0
    for prio in prio_ordre:
        if prio in dico_info["objets_voisins"]:
            chemin_prio = fabrique_chemin(dico_info["arene"],dico_info["positions"][0],dico_info["objets_voisins"][prio])
            if est_ateignable(dico_info["objets_voisins"][prio],dico_info,chemin_prio) :
                if len(chemin_prio) == 1:
                    return find_direction(dico_info["objets_voisins"][prio],dico_info)
                else:
                    return find_direction(chemin_prio[0],dico_info)


"""def strategie_2(chemin_prio):
    pass"""


def find_direction(coordone_bonus:tuple,dico_info:dict):
    """Renvoie la direction a prendre par le serpent

    Args:
        coordone_bonus (tuple): coordone du bonus
        dico_info (dict): dico info

    Returns:
        str: direction a prendre
    """    
    lgn = coordone_bonus[0] - dico_info["positions"][0][0]
    col = coordone_bonus[1] - dico_info["positions"][0][1]
    for direct,coordone in arene.DIRECTIONS.items():
        if coordone[0] == lgn and coordone[1] == col:
            return direct


def fabrique_chemin(l_arene:dict, position_serpent:tuple, position_bonus:tuple):
    """Renvoie le plus court chemin entre position_serpent position_bonus

    Args:
        l_arene (plateau): un plateau de jeu
        position_serpent (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_bonus (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_bonus et position_serpent
        qui représente un plus court chemin entre les deux positions (sans position_serpent)
    """
    def voisins_possibles(l_arene, position):
        """Renvoie les directions possibles autour des coordonées sous la forme d'une liste de tuples

        Args:
            l_arene (_type_): dict de l'arène
            position (_type_): position actuelle de l'inondation

        Returns:
            list: liste de tuples de coordonées -> [(x,y),(x,z),...]
        """        
        res = directions_possibles(l_arene, position)
        voisins = res["coordonnees"]
        return voisins
    file_position = [(position_serpent,[position_serpent])] #methode de séquence file
    chemin = [] 
    deja_visite = set()
    deja_visite.add(position_serpent)
    while file_position:
        position,chemin = file_position.pop(0) #je retire le première élément de la file et le met dans position
        if position == position_bonus:
            chemin.append(position_bonus)
        for voisin in voisins_possibles(l_arene,position):
            if voisin not in deja_visite:
                deja_visite.add(voisin)
                file_position.append((voisin,chemin+[voisin])) 
    return chemin

"""
postion_bonus

"""

# ---------------------------------------------------------------------------

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
    def information(la_partie:dict,dist_max:int=5,num_joueur:int=0)->dict:
        """Créer un dictionnaire avec comme clé le nom de l'information et en attributs sa valeur

        Args:
            la_partie (dict): dict de la partie

        Returns:
            dict: {"num_joueur":int,"point":int,"objets_voisins":dict}
        """        
        information = {}
        l_arene = partie.get_arene(la_partie)
        dico_serpent = l_arene["serpents"][num_joueur-1] 
        information["num_joueur"] = num_joueur
        information["arene"] = l_arene
        information["point"] = dico_serpent["points"]
        information["objets_voisins"] = objets_voisinage(l_arene, information["num_joueur"], dist_max)
        information["positions"] = arene.get_serpent(l_arene,information["num_joueur"])
        return information
    dico_info = information(la_partie,30,num_joueur)
    direction=random.choice("NSEO")
    direction_prec=direction #La décision prise sera la direction précédente le prochain tour
    l_arene = partie.get_arene(la_partie)
    dir_pos=directions_possibles(l_arene,(arene.get_serpent(l_arene,num_joueur)[0][0],arene.get_serpent(l_arene,num_joueur)[0][1]))["direction"]
    print(directions_possibles(l_arene,(arene.get_serpent(l_arene,num_joueur)[0][0],arene.get_serpent(l_arene,num_joueur)[0][1]))["direction"])
    print("les bonus: ",num_joueur,objets_voisinage(partie.get_arene(la_partie),num_joueur,dist_max=5))
    if dir_pos=='':
        direction=random.choice('NOSE')
    else:
        direction=avancer_tour(la_partie,dico_info)
        if direction == None :
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
