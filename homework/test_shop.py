"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert 1000 == product.quantity

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(10)
        assert 990 == product.quantity

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_empty_new_cart(self, cart):
        assert 0 == len(cart.products.items())

    def test_add_one_item_to_cart(self, cart, product):
        cart.add_product(product, 1)
        assert 1 == cart.products[product]

    def test_add_fifty_item_to_cart(self, cart, product):
        cart.add_product(product, 1)
        cart.add_product(product, 49)
        assert 50 == cart.products[product]

    def test_huest(self,cart,product):
        with pytest.raises(ValueError):
            cart.add_product(product, 1500)

    def test_add_two_different_items_to_cart(self, cart, product, iphone):
        cart.add_product(product, 1)
        cart.add_product(iphone, 40)

        assert 2 == len(cart.products.keys())

    def test_add_more_than_available_items_to_cart(self, cart, iphone):
        with pytest.raises(ValueError):
            cart.add_product(iphone, 1001)

    def test_del_totally_item_from_cart(self, cart, iphone):
        cart.add_product(iphone)
        cart.remove_product(iphone, iphone.quantity)
        assert len(cart.products) == 0

    def test_del_same_amount_from_cart(self, cart, iphone):
        cart.add_product(iphone, 2)
        cart.remove_product(iphone, 2)
        assert len(cart.products) == 0

    def test_del_less_amount_from_cart(self, cart, iphone):
        cart.add_product(iphone, 2)
        cart.remove_product(iphone, 1)
        assert len(cart.products) == 1
        assert cart.products[iphone] == 1

    def test_decrease_amount_of_item_in_cart(self, cart, iphone):
        cart.add_product(iphone, 2)
        cart.remove_product(iphone, 1)
        assert cart.products[iphone] == 1

    def test_correct_total_amount(self, cart, iphone, product):
        cart.add_product(iphone)
        cart.add_product(product)
        assert 1099 == cart.get_total_price()
        pass

    def test_flush_empty_cart_impossible(self, cart, product):
        with pytest.raises(ValueError):
            cart.clear()

    def test_clear_item_form_cart(self, cart, product):
        cart.add_product(product, 100)
        cart.clear()
        assert 0 == len(cart.products.items())
