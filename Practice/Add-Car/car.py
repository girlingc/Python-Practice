class Car:
    def __init__(self, make='', model='', year=0000, cost=0.00, price=0.00):
        self.make = make
        self.model = model
        self.year = year
        self.cost = cost
        self.price = price
    
    def calc_profit(self):
        print(self.price - self.cost)
        return self.price - self.cost

    def get_details(self):
        print("{} {} {} for sale for ${}".format(self.make, self.model, self.year, self.price))
        return "{} {} {} for sale for ${}".format(self.make, self.model, self.year, self.price)

    def reduce_price(self, reduction):
        print(self.price - reduction)
        return self.price - reduction

    def __del__(self):
        print("Car deleted")

a = Car("Honda", "Civic", 2010, 20000, 35000)
print(a.get_details())
print(f"The profit is ${a.price}")
print(f"The price of {a.year} {a.make} {a.model} has been reduced from ${a.price} to ${a.reduce_price(5000)}")