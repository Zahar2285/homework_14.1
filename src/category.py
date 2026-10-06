from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1


    @property
    def products(self) -> str:
        return "".join(
            f"{product.name}, {product.price} руб. Остаток: "
            f"{product.quantity} шт.\n"
            for product in self.__products
        )
