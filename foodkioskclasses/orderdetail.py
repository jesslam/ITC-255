from menuitem import MenuItem
from orders import Orders

class OrderDetail():
    def __init__(self, orderID, quantity, orderDate, orderStatus):
        self.menuitems = []
        self.orderID = orderID
        self.quantity = quantity
        self.orderDate = orderDate
        self.orderStatus = orderStatus

    def getMenuItems(self):
        return self.menuitems

    def getQuantity(self):
        return self.quantity

    def getOrderDate(self):
        return self.orderDate

    def getOrderStatus(self):
        return self.orderStatus

        

