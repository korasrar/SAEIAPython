import serpent as s

dico_morad = {"nom_joueur": "morad", "num_joueur":1, "points":3, "positions":[[0,0],[1,0],[1,1]]
,"tps_s":3, "tps_p":8, "tps_m":0, "direction":'N'}
dico_celestin = {"nom_joueur": "celestin", "num_joueur":2, "points":6, "positions":[[0,0],[1,0],[1,1],[1,2]]
,"tps_s":6, "tps_p":0, "tps_m":2, "direction":'S'}
dico_clement = {"nom_joueur": "clement", "num_joueur":3, "points":5, "positions":[[0,0],[1,0],[1,1]]
,"tps_s":0, "tps_p":1, "tps_m":9, "direction":'O'}

def test_get_nom():
    assert s.get_nom(dico_morad) == "morad"
    assert s.get_nom(dico_celestin) == "celestin"
    assert s.get_nom(dico_clement) == "clement"

def test_get_num_joueur():
    assert s.get_num_joueur(dico_morad) == 1
    assert s.get_num_joueur(dico_celestin) == 2
    assert s.get_num_joueur(dico_clement) == 3

def test_get_points():
    assert s.get_points(dico_morad) == 3
    assert s.get_points(dico_celestin) == 6
    assert s.get_points(dico_clement) == 5
    
def test_get_liste_pos():
    assert s.get_liste_pos(dico_morad) == [[0,0],[1,0],[1,1]]
    assert s.get_liste_pos(dico_celestin) == [[0,0],[1,0],[1,1],[1,2]]
    assert s.get_liste_pos(dico_clement) == [[0,0],[1,0],[1,1]]

def test_get_queue():
    assert s.get_queue(dico_morad) == [1,1]
    assert s.get_queue(dico_celestin) == [1,2]
    assert s.get_queue(dico_clement) == [1,1]

def test_get_derniere_direction():
    assert s.get_derniere_direction(dico_morad) == 'N'
    assert s.get_derniere_direction(dico_celestin) == 'S'
    assert s.get_derniere_direction(dico_clement) == 'O'

def test_get_bonus():
    assert s.get_bonus(dico_morad) == ['tps_s','tps_p']
    assert s.get_bonus(dico_celestin) == ['tps_s','tps_m']
    assert s.get_bonus(dico_clement) == ['tps_p','tps_m']

def test_to_str():
    assert s.to_str(dico_morad) == "morad -> 3 s:3 m:0 p:8"
    assert s.to_str(dico_celestin) == "celestin -> 6 s:6 m:2 p:0"
    assert s.to_str(dico_clement) == "clement -> 5 s:0 m:9 p:1"
    
def test_get_temps_mange_mur():
    assert s.get_temps_mange_mur(dico_morad) == 0
    assert s.get_temps_mange_mur(dico_celestin) == 2
    assert s.get_temps_mange_mur(dico_clement) == 9

def test_get_temps_protection():
    assert s.get_temps_protection(dico_morad) == 8
    assert s.get_temps_protection(dico_celestin) == 0
    assert s.get_temps_protection(dico_clement) == 1

def test_ajouter_temps_protection():
    assert s.ajouter_temps_protection(dico_morad, 2) == s.get_temps_protection(dico_morad)
    assert s.ajouter_temps_protection(dico_celestin, 3) == s.get_temps_protection(dico_celestin)
    assert s.ajouter_temps_protection(dico_clement, 1) == s.get_temps_protection(dico_clement)

def test_ajouter_temps_mange_mur():
    assert s.ajouter_temps_mange_mur(dico_morad,2) == s.get_temps_mange_mur(dico_morad)
    assert s.ajouter_temps_mange_mur(dico_celestin,2) == s.get_temps_mange_mur(dico_celestin)
    assert s.ajouter_temps_mange_mur(dico_clement,2) == s.get_temps_mange_mur(dico_clement)

def test_ajouter_temps_surpuissance():
    assert s.ajouter_temps_surpuissance(dico_morad, 2) == s.get_temps_surpuissance(dico_morad)

def test_serpent_2_str():
    assert s.serpent_2_str(dico_morad) == f"morad;{s.get_num_joueur(dico_morad)};{s.get_points(dico_morad)};{s.get_temps_surpuissance(dico_morad)};{s.get_temps_protection(dico_morad)};{s.get_temps_mange_mur(dico_morad)};N\n0;0;1;0;1;1"
    assert s.serpent_2_str(dico_celestin) == f"celestin;{s.get_num_joueur(dico_celestin)};{s.get_points(dico_celestin)};{s.get_temps_surpuissance(dico_celestin)};{s.get_temps_protection(dico_celestin)};{s.get_temps_mange_mur(dico_celestin)};S\n0;0;1;0;1;1;1;2"
    assert s.serpent_2_str(dico_clement) == f"clement;{s.get_num_joueur(dico_clement)};{s.get_points(dico_clement)};{s.get_temps_surpuissance(dico_clement)};{s.get_temps_protection(dico_clement)};{s.get_temps_mange_mur(dico_clement)};O\n0;0;1;0;1;1"

def test_serpent_from_str():
    assert s.serpent_from_str(f"morad;{s.get_num_joueur(dico_morad)};{s.get_points(dico_morad)};{s.get_temps_surpuissance(dico_morad)};{s.get_temps_protection(dico_morad)};{s.get_temps_mange_mur(dico_morad)};N\n0;0;1;0;1;1") == dico_morad
    assert s.serpent_from_str(f"celestin;{s.get_num_joueur(dico_celestin)};{s.get_points(dico_celestin)};{s.get_temps_surpuissance(dico_celestin)};{s.get_temps_protection(dico_celestin)};{s.get_temps_mange_mur(dico_celestin)};S\n0;0;1;0;1;1;1;2") == dico_celestin
    assert s.serpent_from_str(f"clement;{s.get_num_joueur(dico_clement)};{s.get_points(dico_clement)};{s.get_temps_surpuissance(dico_clement)};{s.get_temps_protection(dico_clement)};{s.get_temps_mange_mur(dico_clement)};O\n0;0;1;0;1;1") == dico_clement

def test_copie_serpent():
    assert s.copy_serpent(dico_morad) == dico_morad
    assert s.copy_serpent(dico_celestin) == dico_celestin
    assert s.copy_serpent(dico_clement) == dico_clement
    
