from item import Item


class Phone(Item):
    # pass
    ###########################
    
    all = []
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        #################################################################################################
        # assert price >= 0, f'Price {price} in not greater than or equal to zero!'
        # assert quantity >= 0, f'Quantity {quantity} in not greater than or equal to zero!'
        assert broken_phones >= 0, f'Broken Phones {broken_phones} in not greater than or equal to zero!'
        #################################################################################################
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones
        #################################################################################################
        Phone.all.append(self)