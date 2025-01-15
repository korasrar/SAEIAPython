import arene
import IA
def avancer_tour(temps_restant,l_arene,num_joueur):
    if temps_restant < 50:
        return priorite_phase_1(l_arene, num_joueur)
    elif temps_restant >=50 and temps_restant < 100:
        return priorite_phase_2(l_arene, num_joueur)
    else:  
        pass       

def priorite_phase_1(l_arene, num_joueur ): #ordre de prise des bonus pour les 50 premier tours
    ordre = []
    score_tete = arene.get_val_boite(l_arene, arene.get_serpent(l_arene, num_joueur)[0],arene.get_serpent(l_arene, num_joueur)[1])
    if score_tete < 2:
        ordre = [1]
    else:
        ordre = [2,1,-2,-1]





        
def priorite_phase_2(): #ordre de prise des bonus de 100 à 150 tours
    


  
def fabrique_chemin(l_arene, position_serpent, position_bonus):
    """Renvoie le plus court chemin entre position_serpent position_bonus

    Args:
        l_arene (plateau): un plateau de jeu
        position_serpent (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_bonus (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_bonus et position_serpent
        qui représente un plus court chemin entre les deux positions
    """
    calque=fabrique_le_calque(l_arene,position_serpent)
    chemin=[position_bonus]
    pas_fini=True
    while pas_fini:
        position_actu=chemin[-1]
        ens_voisins=voisins(l_arene,position_actu)
        mini=None
        voisin_min=None
        for voisin in ens_voisins:
            ligne,colonne=voisin
            val=matrice.get_val(calque,ligne,colonne)
            if mini is None or mini>val:
                mini=val
                voisin_min=voisin
        if voisin_min==position_serpent:
            pas_fini=False
        else:
            chemin.append(voisin_min)
    return chemin
    
def deplace_fantome(l_arene, fantome, personnage):
    """déplace le FANTOME sur le plateau vers le personnage en prenant le chemin le plus court

    Args:
        l_arene (plateau): un plateau de jeu
        fantome (tuple): la position du fantome sur le plateau
        personnage (tuple): la position du personnage sur le plateau

    Returns:
        [tuple]: la nouvelle position du FANTOME
    """
    if fantome==personnage:
        return fantome
    else:
        chemin=fabrique_chemin(l_arene,fantome,personnage)
        ligne,colonne=fantome
        matrice.set_val(l_arene,ligne,colonne,COULOIR)
        new_ligne,new_colonne=chemin[-1]
        matrice.set_val(l_arene,new_ligne,new_colonne,FANTOME)
        return (new_ligne,new_colonne)

def fabrique_chemin_v2(l_arene, position_serpent, position_bonus):
    for recherche in IA.objets_voisinage(l_arene, num_joueur, 15):
        if recherche.keys() == position_bonus:
            rech