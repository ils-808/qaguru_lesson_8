class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if quantity > self.quantity:
            return False
        else:
            return True

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity += quantity
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)

    """
    переопределяем функцию __repr__ для отображения содержимого в pprint()
    """
    def __repr__(self):
        return f"Product(name: {self.name}, price: {self.price}, description: {self.description}, quantity: {self.quantity}"


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if buy_count <= product.quantity:
            if (product in self.products):
                self.products[product] += buy_count
            else:
                self.products[product] = buy_count
        else:
            raise ValueError

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if (remove_count >= self.products[product]) or remove_count == 0:
            self.products.pop(product)
        else:
            self.products[product] -= remove_count

    def clear(self):
        if len(self.products):
            self.products.clear()
        else:
            raise ValueError

    def get_total_price(self) -> float:
        total = 0.00
        for product in self.products:
            total += self.products[product] * product.price
        return total

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        # Не применимо в моем кейсе, т.к. для метода add_product выполняется проверка со стоками.
        # Что, на мой взгляд более логично
        for product in self.products:
            if product.quantity < self.products[product]:
                #невозможно купить
                raise ValueError
            else:
                self.remove_product(product)
                #возможно купить
