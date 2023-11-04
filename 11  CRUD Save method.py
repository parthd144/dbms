from collections import defaultdict

class Item:
    def __init__(self, id, quantity, price, brand, discount):
        self.id = id
        self.quantity = quantity
        self.price = price
        self.brand = brand
        self.discount = discount

    def __str__(self):
        return f"Item ID: {self.id}, Quantity: {self.quantity}, Price: {self.price}, Brand: {self.brand}, Discount: {self.discount}"


class ItemManager:
    def __init__(self):
        self.items = defaultdict(list)
        self.item_prices = defaultdict(list)
        self.item_discounts = defaultdict(list)

    def save(self, item):
        self.items[item.brand].append(item)
        self.item_prices[item.brand].append(item.price)
        self.item_discounts[item.brand].append(item.discount)

    def count_brand(self):
        brand_count = defaultdict(int)
        for brand, items in self.items.items():
            brand_count[brand] = len(items)
        return brand_count

    def get_min_price_item(self):
        min_price = float('inf')
        min_item = None
        for brand, prices in self.item_prices.items():
            for price in prices:
                if price < min_price:
                    min_price = price
                    min_item = self.items[brand][prices.index(price)]
        return min_item

    def get_max_discount_item(self):
        max_discount = float('-inf')
        max_item = None
        for brand, discounts in self.item_discounts.items():
            for discount in discounts:
                if discount > max_discount:
                    max_discount = discount
                    max_item = self.items[brand][discounts.index(discount)]
        return max_item


item_manager = ItemManager()

# Saving items
item_manager.save(Item(1, 10, 100, 'Brand A', 5))
item_manager.save(Item( ItemManager()

# Creating and saving items
item1 =2, 5, 150, ' Item(1, 10, 1Brand B', 10))
item_manager.00, 'Brand1', 5)
save(Item(3, 7, 12item2 = Item(2, 5, 0, 'Brand A', 7))
item_150, 'Brand1', 10manager.save(Item(4, 1)
item3 = Item(3, 15, 80, 'Brand5, 200, 'B C', 2))

# Displayingrand2', 15)
item4 item count brand wise
print(item_manager = Item(4, 20.count_brand())

# Displaying, 25 item with minimum price
print(item_manager.get0, 'Brand2', 2_min_price_item())

#0)

item_manager.save( Displaying item with maximum discount
print(itemitem1)
item_manager.save(_manager.get_max_discountitem2)
item_manager.save(_item())