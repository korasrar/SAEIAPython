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
    lgn = arene.get_dim(l_arene)[0]
    col = arene.get_dim(l_arene)[1]
    res = ''
    tete_lgn = arene.get_serpent(l_arene, num_joueur)[0][0]
    tete_col = arene.get_serpent(l_arene, num_joueur)[0][1]
    for direction in arene.DIRECTIONS:
        if est_pas_mur(l_arene, tete_lgn, tete_col, direction):
            if est_pas_sortie(tete_lgn, tete_col,direction):
                res += direction
    return res

def est_pas_mur(l_arene, lgn, col, direction):
    if not arene.est_mur(l_arene, lgn + arene.DIRECTIONS[direction][0], col + arene.DIRECTIONS[direction][1]):
        return True
    return False

def est_pas_sortie(lgn, col, direction):
    if lgn + arene.DIRECTIONS[direction][0] > 0 and lgn + arene.DIRECTIONS[direction][0] < lgn:
        if col + arene.DIRECTIONS[direction][1] > 0 and col + arene.DIRECTIONS[direction][1] < col:
            return True
    return False

def objets_voisinage(l_arene:dict,num_joueur:int,dist_max:int):
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
    val_obj = 0
    prop = 0 
    print(arene.get_serpent(l_arene,num_joueur)[0])
    set_future_voisins = set()
    coordo_serpent = arene.get_serpent(l_arene,num_joueur)[0]
    set_future_voisins.update(coordo_serpent) # coordone serpent
    str_direction_possible = directions_possibles(l_arene,num_joueur,arene.get_serpent(l_arene,num_joueur)[0])
    str_ancienne_direction = ''
    dict_voisinages = {}
    check = False
    while not check:
        print(set_future_voisins)
        for coordone in set_future_voisins:
            str_direction_possible = directions_possibles(l_arene,num_joueur,coordone)
            print(str_direction_possible)
            for direction in str_direction_possible:
                set_future_voisins.add((coordone[0]+arene.DIRECTIONS[direction][0],coordone[1]+arene.DIRECTIONS[direction][1]))
                print(set_future_voisins)
                str_ancienne_direction += direction
                print(str_ancienne_direction)
            if arene.est_bonus(l_arene,coordone[0],coordone[1]):
                dict_voisinages[str_ancienne_direction] = [
                    len(str_ancienne_direction),
                    arene.get_val_boite(coordone_direction),
                    arene.get_proprietaire(l_arene,coordone[0],coordone[1])]
            if len(str_ancienne_direction) < dist_max :
                    check = True
    return dict_voisinages

    def getcoordonee(position,direction) :
        position[0]+arene.DIRECTIONS[direction][0],position[1]+arene.DIRECTIONS[direction][1]
    distance = 0
    position_serpent = arene.get_serpent(l_arene,num_joueur)
    tete_serpent = position_serpent[0]
    str_direction_voisin = directions_possibles(l_arene,tete_serpent)
    set_coordone_voisin
    set_future_voisins = set()  
    check = False
    while not check:
        distance += 1
        for direction in set_direction_voisins:
            if est_pas_mur() :
                set_future_voisins = set_future_voisins.union(map(getcoordonee(directions_possibles(l_arene,direction))))
            if distance >= dist_max:
                    check = True
        set_position_voisins = set_future_voisins
        set_future_voisins = set()
    return set_position_voisins

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
    dir_pos=directions_possibles(partie.get_arene(la_partie),num_joueur)
    #print(objets_voisinage(partie.get_arene(la_partie),num_joueur,dist_max=4))
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

def avancer_tour(temps_restant):
    if temps_restant < 50:
        pass
    elif temps_restant >=50 and temps_restant < 100:
        pass
    else:  
        pass
def comparateur(restant_evo, tresor, radar):    
    
def strategie():
    pass 
def priorite_phase_1(l_arene, num_joueur ): #ordre de prise des bonus pour les 50 premier tours
    ordre = []
    score_tete = arene.get_val_boite(l_arene, arene.get_serpent(l_arene, num_joueur)[0],arene.get_serpent(l_arene, num_joueur)[1])
    if score_tete < 2:
        ordre = [1]
    else:
        ordre = [2,1,-2,-1]
    
        
def priorite_phase_2(): #ordre de prise des bonus de 100 à 150 tours
    pass
def radar_serpent():
    pass

def choix_direction():
    pass