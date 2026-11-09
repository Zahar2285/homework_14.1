from abc import ABC, abstractmethod


class PrintMixin:
    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__}{args}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    @abstractmethod
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            *args,
    ) -> None:
        self.name = name
        self.description = description
        self._Product__price = price
        self.quantity = quantity


class Product(PrintMixin, BaseProduct):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            *args,
    ) -> None:
        if quantity == 0:
            raise ValueError(
                "Товар с нулевым количеством не может быть добавлен"
            )

        super().__init__(name, description, price, quantity, *args)

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")

        return (
            self.price * self.quantity
            + other.price * other.quantity
        )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(
            name,
            description,
            price,
            quantity,
            efficiency,
            model,
            memory,
            color,
        )
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(
            name,
            description,
            price,
            quantity,
            country,
            germination_period,
            color,
        )
        self.country = country
        self.germination_period = germination_period
        self.color = color
