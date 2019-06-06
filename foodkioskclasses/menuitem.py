class MenuItem():
    def __init__(self, itemID, itemName, itemSize, itemPrice):
        self.itemID = itemID
        self.itemName = itemName
        self.itemSize = itemSize
        self.itemPrice = itemPrice

    def getItemID(self):
        return self.itemID

    def getItemName(self):
        return self.itemName
    
    def getItemSize(self):
        return self.itemSize

    def getItemPrice(self):
        return self.itemPrice


        