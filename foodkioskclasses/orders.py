from payment import Payment
from menuitem import MenuItem

class Orders():
    def __init__(self, orderID):
        self.menuitems = []
        self.orderID = orderID

    def getOrderID(self):
        return self.orderID

    def addMenuItems(self, menuitem):
        self.menuitems.append(menuitem)

    def calcOrderTotal(self):
        total = 0.00
        for m in self.menuitems:
            total += m.getMenuItems().itemPrice * m.quantity
            payment = Payment(total)
            return payment

    def __str__(self):
        return self.orderID + "Your total is: " + self.orderStatus
