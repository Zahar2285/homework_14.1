import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counts() -> None:
    Category.category_count = 0
    Category.product_count = 0


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


def test_category_count() -> None:
    product = Product(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
    )

    Category(
        name="Смартфоны",
        description="Мобильные телефоны",
        products=[product],
    )

    Category(
        name="Ноутбуки",
        description="Ноутбуки для работы",
        products=[product],
    )

    assert Category.category_count == 2


def test_product_count() -> None:
    product1 = Product(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
    )
    product2 = Product(
        name="MacBook Air",
        description="Ноутбук Apple",
        price=150000.0,
        quantity=3,
    )

    Category(
        name="Техника",
        description="Электроника",
        products=[product1, product2],
    )

    assert Category.product_count == 2
