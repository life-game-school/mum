from grille_cellule import Grille, apply_life_rules


def test_apply_life_rules():
    grille = Grille(10)
    grille.generer()
    vivantes = apply_life_rules(grille, [])
    assert(vivantes == [])
