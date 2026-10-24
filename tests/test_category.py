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
    assert category.products == "iPhone 15, 100000.0 руб. Остаток: 5 шт.\n"


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


def test_add_product() -> None:
    product = Product(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
    )

    category = Category(
        name="Смартфоны",
        description="Мобильные телефоны",
        products=[],
    )

    category.add_product(product)

    assert category.products == "iPhone 15, 100000.0 руб. Остаток: 5 шт.\n"
    assert Category.product_count == 1

def test_category_str() -> None:
    product1 = Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )
    product2 = Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )
    product3 = Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )

    category = Category(
        name="Смартфоны",
        description="Смартфоны и гаджеты",
        products=[product1, product2, product3],
    )

    assert str(category) == (
        "Смартфоны, количество продуктов: 27 шт."
    )
