from src.category import Category
from src.product import Product


def main() -> None:
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

    category = Category(
        name="Техника",
        description="Электроника и гаджеты",
        products=[product1, product2],
    )

    print(category.name)
    print(category.description)
    print(category.products)
    print(Category.category_count)
    print(Category.product_count)


if __name__ == "__main__":
    main()
    