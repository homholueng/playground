import model_v5 as model

class LineItem:
    descrption = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()
    
    def __init__(self, descrption, weight, price):
        self.descrption = descrption
        self.weight = weight
        self.price = price
    
    def subtotal(self):
        return self.weight * self.price