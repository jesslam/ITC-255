from menuitem import MenuItem
from order import Order

class OrderDetail():
    def __init__(self, orderID, quantity, orderDateTime, orderStatus):
        self.menuitems = []
        self.orderID = orderID
        self.orderDateTime = datetime.datetime.now()
        self.orderStatus = orderStatus

    def getMenuItems(self):
        return self.menuitems

    def getOrderDateTime(self):
        return self.orderDateTime

    def getOrderStatus(self):
        return self.orderStatus

        

