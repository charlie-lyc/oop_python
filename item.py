import csv


class Item:
    # pass
    ########################################
    
    pay_rate = 0.8
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        # print('Item object was created!')
        ##################################################################################
        ## Validations to the received arguments
        assert price >= 0, f'Price {price} in not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} in not greater than or equal to zero!'
        ##################################################################################
        # self.name = name
        ##################################################################################
        ## READ ONLY Attribute
        # self._name = name
        self.__name = name
        self.__price = price
        self.quantity = quantity
        ##################################################################################
        Item.all.append(self)
        
    #########################################################################################################
    
    @property ## READ ONLY Attribute
    def name(self):
        ## Necessary Logic...
        # print('You are trying to get name!')
        return self.__name
    
    @name.setter
    def name(self, value):
        ## Necessary Logic...
        # print('You are trying to set name!')
        if len(value) > 10:
            raise Exception('Too Long Name!')
        self.__name = value
    
    #########################################################################################################
    
    @property
    def price(self):
        return self.__price
    
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    
    def apply_discount(self):
        # self.price = self.price * pay_rate      # NameError
        #########################################
        # self.price = self.price * Item.pay_rate # Class Level
        #########################################
        # self.price = self.price * self.pay_rate # Instance Level
        #########################################
        self.__price = self.__price * self.pay_rate
    
    #########################################################################################################
    
    # def calculate_total_price(self, x, y):
    #     return x * y 
    ########################################
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            ###########################################
            # for row in reader:
            #     print(row)
            ###########################################
            for item in list(reader):
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )
            ###########################################
    
    @staticmethod
    def is_integer(num):
        return isinstance(num, int)
    
    def __repr__(self):
        # return 'Item'
        ##################################################################################
        # return f"Item('{self.name}', {self.price}, {self.quantity})"
        ##################################################################################
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    #########################################################################################################
    
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f'''
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, CharlieCodeFactory
        '''
        
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect('google_smtp')
        self.__prepare_body()
        self.__send()
    
    