#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class store_inventory:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def double_cost(self):
        self.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
clothes = store_inventory(30, 300, 1)
soup = store_inventory(200, 3, 2)
greg = store_inventory(1, 500, 50)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"Clothes Stock: {clothes.stock}, Soup Stock: {soup.stock}, GREG Stock: {greg.stock}")
print(f"Soup Cost: {soup.cost}")
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
soup.double_cost()
print(f"New Soup Cost: {soup.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
greg.stock /= 4
greg.stock = round(greg.stock)
print("GREG Stock:", greg.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del clothes

try:
    print(clothes.weight)
except:
    print("Out of Stock!")
