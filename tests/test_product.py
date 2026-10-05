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
