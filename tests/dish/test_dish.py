from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest

ingredients_dish = {Ingredient('bacon'), Ingredient('queijo mussarela')}
value_error = "Dish price must be greater then zero."


# Req 2
def test_dish():
    lasanha = Dish('lasanha', 10)
    queijo = Ingredient('queijo mussarela')
    bacon = Ingredient('bacon')
    salmao = Ingredient('salmão')
    assert lasanha.name == 'lasanha'
    assert lasanha.price == 10
    assert lasanha.__repr__() == "Dish('lasanha', R$10.00)"
    pizza = Dish('pizza', 20)
    assert lasanha.__hash__() != pizza.__hash__()
    other_lasanha = Dish('lasanha', 10)
    assert other_lasanha.__hash__() == lasanha.__hash__()
    assert other_lasanha.__eq__(lasanha) is True
    assert other_lasanha.__eq__(pizza) is False
    lasanha.add_ingredient_dependency(queijo, 1)
    lasanha.add_ingredient_dependency(bacon, 1)
    other_lasanha.add_ingredient_dependency(queijo, 1)
    other_lasanha.add_ingredient_dependency(bacon, 1)
    pizza.add_ingredient_dependency(salmao, 1)
    assert lasanha.get_ingredients() == ingredients_dish
    assert lasanha.get_restrictions() == other_lasanha.get_restrictions()
    assert lasanha.get_restrictions() != pizza.get_restrictions()
    with pytest.raises(ValueError, match=value_error):
        Dish('Miojo', -10)
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('Miojo', "a")
