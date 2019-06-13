import unittest
from employee import Employee
from menuitem import MenuItem
from orderdetail import OrderDetail
from orders import Orders
from payment import Payment
import datetime

class OrderItemTest(unittest.TestCase):
    def setUp(self):
        self.item=MenuItem(15, 'Cheeseburger', 'Large', 3.79)

    def test_GetItemName(self):
        self.assertEqual(self.item.getItemName(), 'Cheeseburger')

    def test_GetItemID(self):
        self.assertEqual(self.item.getItemID(), 15)

    def test_GetItemSize(self):
        self.assertEqual(self.item.getItemSize(), 'Large')

    def test_GetItemPrice(self):
        self.assertEqual(self.item.getItemPrice(), 3.79)

class OrderTest(unittest.TestCase):
    def setUp(self):
        self.orderdetails=OrderDetail(23, 2, '2019-06-13', 'Complete')

    def test_getOrderStatus(self):
        self.assertEqual(self.orderdetails.getOrderStatus(), 'Complete')

    def test_getQuantity(self):
        self.assertEqual(self.orderdetails.getQuantity(), 2)

    def test_getDate(self):
        self.assertEqual(self.orderdetails.getOrderDate(), '2019-06-13')



