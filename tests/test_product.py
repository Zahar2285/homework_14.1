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
