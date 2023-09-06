from src.models.ingredient import Ingredient  # noqa: F401, E261, E501

# Req 1


def test_ingredient():
    queijo = Ingredient('queijo mussarela')
    other_mussarela = Ingredient('queijo mussarela')
    assert queijo.name == 'queijo mussarela'
    assert queijo.__repr__() == "Ingredient('queijo mussarela')"
    assert queijo.__eq__('queijo provolone') is False
    assert queijo.__eq__(other_mussarela) is True
    bacon = Ingredient('bacon')
    assert bacon.__hash__() != queijo.__hash__()
    assert queijo.__hash__() == other_mussarela.__hash__()
    assert queijo.restrictions == other_mussarela.restrictions
    assert queijo.restrictions != bacon.restrictions
