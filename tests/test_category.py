from src.category import Category
from src.product import Product


def test_category_initialization() -> None:
    product = Product(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
    )

    category = Category(
        name="Смартфоны",
        description="Мобильные телефоны",
        products=[product],
    )

    assert category.name == "Смартфоны"
    assert category.description == "Мобильные телефоны"
    assert category.products == [product]
