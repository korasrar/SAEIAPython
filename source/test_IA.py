import arene
import IA
import partie
import serpent

def information(la_partie):
    information = {}
    l_arene = partie.get_arene()
    information["num_joueur"] = dico_serpent["num_joueur"]
    dico_serpent = l_arene["serpent"][information["num_joueur"]-1] 
    information["point"] = dico_serpent["point"]
    information["object_voisins"] = IA.objets_voisinage(l_arene, information["num_joueur"], 15)
    return information

info = information(la_partie)

#{keys: valeur_bonus valeur: coordonnees}

def avancer_tour(temps_restant,l_arene,num_joueur):
    if temps_restant < 50:
        return strategie_1()
    elif temps_restant >=50 and temps_restant < 100:
        return strategie_2()
    else:  
        pass
def get_info_bonus(bonus):
    """

    """
    for 

def est_ateignable(bonus, dico_ref):
    pass
    
def est_sur_chemin(chemmin_prio, t ):
    pass    

def priorite_phase_1(l_arene, num_joueur ): #ordre de prise des bonus pour les 50 premier tours
    ordre = []
    score_tete = arene.get_val_boite(l_arene, arene.get_serpent(l_arene, num_joueur)[0],arene.get_serpent(l_arene, num_joueur)[1])
    if score_tete < 2:
        return ordre.append(1)
    else:
        return ordre.append(2,1,-2,-1)
    
def priorite_phase_2(): #ordre de prise des bonus de 100 à 150 tours
    pass    

def strategie_1(chemin_prio, ):
    object_choisie = 0
    if len(chemin_prio) == 1:
        return object_choisie + 1
    elif chemin_prio:
        return 
#si il y a un 2

def strategie_2(chemin_prio):
    pass
  
def fabrique_chemin(l_arene:dict, position_serpent:tuple, position_bonus:tuple):
    """Renvoie le plus court chemin entre position_serpent position_bonus

    Args:
        l_arene (plateau): un plateau de jeu
        position_serpent (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_bonus (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_bonus et position_serpent
        qui représente un plus court chemin entre les deux positions
    """
    def voisins_possibles(l_arene, position):
        voisins=IA.directions_possibles(l_arene,position_serpent)["coordonnees"]
        return voisins
    file_position = [] #methode de séquence file
    chemin = [] 
    deja_visite = set()
    check = False
    while not check:
        position = file_position.pop(0) #je retire le première élément de la file et le met dans position
        if position == position_bonus:
            chemin.append(position_bonus)
        for voisin in voisins_possibles(l_arene,position):
            if voisin not in deja_visite:
                deja_visite.add(voisin)
                file_position.append(voisin)
                chemin.append(voisin)
    return chemin
    
def fabrique_chemin_v2(l_arene, position_serpent, position_bonus):
    for recherche in IA.objets_voisinage(l_arene, num_joueur, 15):
        if recherche.keys() == position_bonus:
            rech

"""
postion_bonus

"""