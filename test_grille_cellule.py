from grille_cellule import Grille, apply_life_rules


def test_apply_life_rules_no_lives():
    # Seed with no live cells
    grille = Grille(10)
    grille.generer()
    vivantes = apply_life_rules(grille, [])
    assert(vivantes == [])


def test_still_lifes_block():
    # Block
    # 0 0 0 0
    # 0 1 1 0
    # 0 1 1 0
    # 0 0 0 0
    grille = Grille(4)
    grille.generer()
    vivantes = [(1, 1), (1, 2), (2, 1), (2, 2)]
    grille.modifier(vivantes)
    nouvelles_vivantes = apply_life_rules(grille, vivantes)
    assert(sorted(nouvelles_vivantes) == sorted(vivantes))


def test_still_lifes_beehive():
    # Beehive
    # 0 0 0 0 0 0
    # 0 0 1 1 0 0
    # 0 1 0 0 1 0
    # 0 0 1 1 0 0
    # 0 0 0 0 0 0
    # 0 0 0 0 0 0
    grille = Grille(6)
    grille.generer()
    vivantes = [(1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 3)]
    grille.modifier(vivantes)
    nouvelles_vivantes = apply_life_rules(grille, vivantes)
    assert(sorted(nouvelles_vivantes) == sorted(vivantes))


def test_still_lifes_loaf():
    # Loaf
    # 0 0 0 0 0 0
    # 0 0 1 1 0 0
    # 0 1 0 0 1 0
    # 0 0 1 0 1 0
    # 0 0 0 1 0 0
    # 0 0 0 0 0 0
    grille = Grille(6)
    grille.generer()
    vivantes = [(1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 4), (4, 3)]
    grille.modifier(vivantes)
    nouvelles_vivantes = apply_life_rules(grille, vivantes)
    assert(sorted(nouvelles_vivantes) == sorted(vivantes))


def test_still_lifes_boat():
    # Boat
    # 0 0 0 0 0
    # 0 1 1 0 0
    # 0 1 0 1 0
    # 0 0 1 0 0
    # 0 0 0 0 0
    grille = Grille(5)
    grille.generer()
    vivantes = [(1, 1), (1, 2), (2, 1), (2, 3), (3, 2)]
    grille.modifier(vivantes)
    nouvelles_vivantes = apply_life_rules(grille, vivantes)
    assert(sorted(nouvelles_vivantes) == sorted(vivantes))


def test_still_lifes_tub():
    # Tub
    # 0 0 0 0 0
    # 0 0 1 0 0
    # 0 1 0 1 0
    # 0 0 1 0 0
    # 0 0 0 0 0
    grille = Grille(5)
    grille.generer()
    vivantes = [(1, 2), (2, 1), (2, 3), (3, 2)]
    grille.modifier(vivantes)
    nouvelles_vivantes = apply_life_rules(grille, vivantes)
    assert(sorted(nouvelles_vivantes) == sorted(vivantes))

