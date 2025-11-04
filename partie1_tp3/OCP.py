class Discount:
    def __init__(self, price):
        self.price = price

    def apply_discount(self):
        return self.price
    
class VIPDiscount(Discount):
    def apply_discount(self):
        return self.price * 0.8 # 20% discount

class NewCustDis(Discount):
    def apply_discount(self):
        return self.price * 0.7 #30% discount
    
if __name__ == '__main__':
    price=1000
    mydiscount0=NewCustDis(price)
    newprice0=mydiscount0.apply_discount()
    print(f"Old price:{price} for the first time customar, New price {newprice0}")
    price = 1000
    mydiscount = VIPDiscount(price)
    newprice = mydiscount.apply_discount()
    print(f"Old Price:{price} for VIP, New price {newprice}")
    price = 1000
    mydiscount2 = Discount(price)
    newprice2 = mydiscount2.apply_discount()
    print(f"Old Price:{price} for regular, New price {newprice2}")
