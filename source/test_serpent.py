dico_test : dict = {"nom_joueur": "morad", "num_joueur":1, "points":3, "positions":positions, 
"tps_s":tps_s, "tps_p":tps_p, "tps_m":tps_m, "direction":direction}


def test_get_nom():
    assert get_nom(dico_serpent) == "test1"
    
def test_get_num_joueur():
    assert get_num_joueur(dico_serpent) == 1

def test_get_points():
    assert get_points(dico_serpent) == 0
    
def test_get_liste_pos():
    assert get_liste_pos(dico_serpent) == ...

def test_get_queue():
    assert get_queue(dico_serpent) == ...
    
    
def test_get_derniere_direction():
    assert get_derniere_direction(dico_serpent) == 'N'

def test_get_bonus():
    assert get_bonus(dico_serpent) == ...
    
def test_ajouter_points():
    assert ajouter_points(dico_serpent, 5) == 5