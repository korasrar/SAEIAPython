import serpent as s

dico_test : dict = {"nom_joueur": "morad", "num_joueur":1, "points":3, "positions":[[0,0],[1,0],[1,1]]
,"tps_s":3, "tps_p":3, "tps_m":3, "direction":'N'}

def test_get_nom():
    assert s.get_nom(dico_test) == "test1"
    
def test_get_num_joueur():
    assert s.get_num_joueur(dico_test) == 1

def test_get_points():
    assert s.get_points(dico_test) == 0
    
def test_get_liste_pos():
    assert s.get_liste_pos(dico_test) == ...

def test_get_queue():
    assert s.get_queue(dico_test) == ...
    
def test_get_derniere_direction():
    assert s.get_derniere_direction(dico_test) == 'N'

def test_get_bonus():
    assert s.get_bonus(dico_test) == ...
    
def test_ajouter_points():
    assert s.ajouter_points(dico_test, 5) == 8