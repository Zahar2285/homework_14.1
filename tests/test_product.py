import pytest

from src.product import LawnGrass, Product, Smartphone


def test_product_initialization() -> None:
    product = Product(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
    )

    assert product.name == "iPhone 15"
    assert product.description == "Смартфон Apple"
    assert product.price == 100000.0
    assert product.quantity == 5


def test_new_product() -> None:
    product_data = {
        "name": "iPhone 15",
        "description": "Смартфон Apple",
        "price": 100000.0,
        "quantity": 5,
    }

    product = Product.new_product(product_data)

    assert isinstance(product, Product)
    assert product.name == "iPhone 15"
    assert product.description == "Смартфон Apple"
    assert product.price == 100000.0
    assert product.quantity == 5


def test_product_price_setter() -> None:
    product = Product(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
    )

    product.price = 90000.0

    assert product.price == 90000.0


def test_product_price_setter_invalid() -> None:
    product = Product(
        name="iPhone 15",
        description="Смартфон Apple",
        price=100000.0,
        quantity=5,
    )

    product.price = 0

    assert product.price == 100000.0

    product.price = -5000

    assert product.price == 100000.0


def test_product_str() -> None:
    product = Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )

    assert str(product) == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )


def test_product_add() -> None:
    product1 = Product(
        name="Товар A",
        description="Первый товар",
        price=100.0,
        quantity=10,
    )
    product2 = Product(
        name="Товар B",
        description="Второй товар",
        price=200.0,
        quantity=2,
    )

    assert product1 + product2 == 1400.0


def test_smartphone_inherits_product() -> None:
    smartphone = Smartphone(
        "Samsung Galaxy",
        "Смартфон",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    assert isinstance(smartphone, Product)
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_inherits_product() -> None:
    grass = LawnGrass(
        "Газонная трава",
        "Трава для газона",
        1000.0,
        10,
        "Россия",
        "14 дней",
        "Зелёный",
    )

    assert isinstance(grass, Product)
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "Зелёный"


def test_add_different_product_types() -> None:
    smartphone = Smartphone(
        "Samsung Galaxy",
        "Смартфон",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    grass = LawnGrass(
        "Газонная трава",
        "Трава для газона",
        1000.0,
        10,
        "Россия",
        "14 дней",
        "Зелёный",
    )

    with pytest.raises(TypeError):
        smartphone + grass
