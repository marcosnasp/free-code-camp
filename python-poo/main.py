class Item:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        pass

    def calculate_total_price(self, x, y):
        total_price = x * y
        print(f"Total price is: {total_price}")
        return total_price
        pass

    pass


item1 = Item("Phone", 11000, 4)
print(item1.calculate_total_price(item1.price, item1.quantity))


item2 = Item("Laptop", 6000, 4)
print(item2.calculate_total_price(item2.price, item2.quantity))

print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

random_str = "aaa"
print(random_str.upper())
