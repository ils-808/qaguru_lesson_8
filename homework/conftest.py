from homework.models import Product, Cart
import pytest


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def iphone():
    return Product("iphone", 999, "This is a smartphone", 1000)



@pytest.fixture
def cart():
    return Cart()