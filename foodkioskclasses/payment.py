class Payment():
    def __init__(self, paymentID, paymentType, paymentAmt):
        self.paymentID = paymentID
        self.paymentType = paymentType
        self.paymentAmt = paymentAmt
    
    def getPaymentID(self):
        return self.paymentID

    def getPaymentType(self):
        return self.paymentType

    def getPaymentAmt(self):
        return self.paymentAmt

    def __str__(self):
        