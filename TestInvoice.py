import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'pen':{'qnt': 10, 'unit_price': 3.75, 'discount': 5},'notebook':{'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice
def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_addProduct(invoice, products):
    temp = invoice.addProduct(10, 5.0, 10)
    products["apple"] = temp
    assert products == {'pen':{'qnt': 10, 'unit_price': 3.75, 'discount': 5},'notebook':{'qnt': 5, 'unit_price': 7.5, 'discount': 10},'apple': {'qnt': 10, 'unit_price': 5.0, 'discount': 10}}

def test_itemCount(invoice, products):
    invoice.itemCount(products)
    assert invoice.itemCount(products) == 15
