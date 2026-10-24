from src.product import Product


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