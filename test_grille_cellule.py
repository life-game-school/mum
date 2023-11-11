from grille_cellule import Grille, apply_life_rules


def test_apply_life_rules():
    # Seed with no live cells
    grille = Grille(10)
    grille.generer()
    vivantes = apply_life_rules(grille, [])
    assert(vivantes == [])


def test_still_lifes():
    # Block
    # 0 0 0 0
    # 0 1 1 0
    # 0 1 1 0
    # 0 0 0 0
    grille = Grille(10)
    grille.generer()
    vivantes = [(1, 1), (1, 2), (2, 1), (2, 2)]
    grille.modifier(vivantes)
    nouvelles_vivantes = apply_life_rules(grille, vivantes)
    assert(set(nouvelles_vivantes) == set(vivantes))
