"""
Project 2: Budget App
Part of the freeCodeCamp "Python Certification" (Python v9)

Key Features:
- Object-Oriented Programming: Encapsulates financial logic within a Category class.
- Ledger Management: Tracks deposits, withdrawals, and inter-category transfers.
- Custom Formatting: Overrides __str__ for professional receipt-style output.
- Data Visualization: Calculates and renders an ASCII-based spending percentage chart.
"""

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""): # A deposit method that accepts an amount and an optional description. If no description is given, it should default to an empty string.
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        current_balance = 0
        for element in self.ledger:
            current_balance += element['amount']
        return current_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):

        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        printed_content = f"{self.name.center(30, '*')}\n"
        for element in self.ledger:

        # for amount, description in self.ledger:
            if len(element['description']) > 23:
                description = element['description'][:23]  # __str__() should only format and return output; it must not modify the original data.

            else:
                description = element['description']
            amount = f"{element['amount']:.2f}"
            if len(amount) > 7:
                amount = amount[:7]
            printed_content += f"{description.ljust(23)}{amount.rjust(7)}\n" # description.ljust(23): lefe-justify the string, pad the right sid with space until the total length is 23 chars. if the string is longer than 23, nothing is cut.

        printed_content = printed_content + f"Total: {self.get_balance()}"
        return printed_content  # __str__() should return a string, not print it

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)


auto = Category('Auto')
auto.deposit(2000, 'deposit')
auto.withdraw(12.5, 'gas')
auto.withdraw(20.19, 'repair')

clothing.deposit(1000, 'deposit')
clothing.withdraw(22.5, 'shirt')
clothing.withdraw(22.19, 'coat')

# print(food)
# print(auto)
# print(clothing)


def create_spend_chart(categories):
    total_spend = {}

    for category in categories:
        name = category.name
        spend = 0
        for element in category.ledger:
            if element['amount'] < 0:
                spend += abs(element['amount'])

        total_spend[f"spend_{name}"] = spend
    # print(total_spend)
    total_sum = sum(total_spend.values())

    percentage_spend = {}
    for category in categories:
        name = category.name
        spend = 0
        for element in category.ledger:
            if element['amount'] < 0:
                spend += abs(element['amount'])
        percentage_spend[f"percentage_spend_{name}"] = int((10 * spend // total_sum)*10) # rounded down to the nearest 10
    # print(percentage_spend)

    # print("Percentage spent by category")
    title = "Percentage spent by category"

    y_axis_content = ""
    for i in range(100, -10, -10):
        if i == 0:
            y_axis = f"  {i}| "

        elif i < 100:
            y_axis = f" {i}| "
        else:
            y_axis = f"{i}| "

        content = ""
        for category in percentage_spend.keys():
            if percentage_spend[category] >= i:
                content += "o  "
            else:
                content += "   "

        # print(f"{y_axis}{content}")
        y_axis_content += f"{y_axis}{content}\n"
    # print(f"    _"+"___"*len(categories))
    horizontal_line = f"    -"+"---"*len(categories)

    max_length = 0
    content_category_name = ""
    for category in categories:
        name = category.name
        if len(name)> max_length:
            max_length = len(name)

    for s in range(max_length):
        content_for_name = ""
        for category in categories:
            if len(category.name) > s:
                content_for_name += f"{category.name[s]}  "
            else:
                content_for_name += "   "

        # print(f"     {content_for_name}")
        content_category_name += f"\n     {content_for_name}"

    return f"{title}\n{y_axis_content}{horizontal_line}{content_category_name}"


categories = [food,auto,clothing]
result = create_spend_chart(categories)
print(result)



