import abc


class GameShop(object):
    """Parent class which stores four data values
       """
    def __init__(self, name, category, memory, price):

        self.name = name
        self.category = category
        self.memory = memory
        self.price = price
    """Getters and setters for each data value"""
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCategory(self, category):
        self.category = category

    def getCategory(self):
        return self.category

    def setMemory(self, memory):
        self.memory = memory

    def getMemory(self):
        return self.memory

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    """Abstract method to be overridden later by classes that inherit from GameShop """
    @abc.abstractmethod
    def getNewPrice(self):
        return


class Buy(GameShop):
    """Child class Buy inherits from GameShop"""
    def __init__(self, name, category, memory, price, discount):
        super(Buy, self).__init__(name, category, memory, price)
        self.discount = discount

    def getNewPrice(self):
        """Overrides abstract method"""
        return float(self.price*0.2)


class RentIt(GameShop):
    """Child class RentIt inherits from GameShop"""
    def __init__(self, name, category, memory, price, discount):
        super(RentIt, self).__init__(name, category, memory, price)
        self.discount = discount

    def getDiscount(self):
        return self.discount

    def getNewPrice(self):
        """Overrides abstract method"""
        return (float(self.price))-(float(self.price*self.discount*0.01))

