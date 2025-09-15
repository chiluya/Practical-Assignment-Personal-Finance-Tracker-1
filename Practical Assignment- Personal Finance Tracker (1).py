# ================================
# Personal Finance Tracker - Student A
# ================================

# Step 1: Variable Definitions
monthly_income = 0.0       # total income
total_expenses = 0.0       # total expenses (for quick tracking)
savings_goal = 0.0         # user-defined savings goal

# Step 2: Function to add income
def add_income(amount):
    """Add income to the monthly total."""
    global monthly_income
    if amount > 0:
        monthly_income += amount
        print(f"Income of {amount} added. Total income: {monthly_income}")
    else:
        print("Income amount must be positive.")
# create list to store expenses
expenses = []   # each expense will be a dictionary with category, amount, date

# Step 3: Function to add an expense
def add_expense(category, amount, date):
    """Add a new expense record."""
    global total_expenses
    if amount > 0:
        expense = {"category": category, "amount": amount, "date": date}
        expenses.append(expense)
        total_expenses += amount
        print(f"Expense of {amount} for {category} on {date} added.")
    else:
        print("Expense amount must be positive.")


# Step 4: Simple input features (so the user can add data)
def input_income():
    """Prompt user to enter income amount."""
    try:
        amount = float(input("Enter income amount: "))
        add_income(amount)
    except ValueError:
        print("Invalid input. Please enter a number.")


def input_expense():
    """Prompt user to enter an expense (category, amount, date)."""
    category = input("Enter expense category (e.g., Food, Transport): ")
    try:
        amount = float(input("Enter expense amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        add_expense(category, amount, date)
    except ValueError:
        print("Invalid input. Please enter numbers for amount.")

# enable user to search expenses by category
def search_expenses_by_category():
    """Search and display expenses by category."""
    search_category = input("Enter category to search: ")
    found = False
    print("\nExpenses in category: ", search_category)
    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            print("Amount for", search_category, "is: ", expense["amount"], "on", expense["date"])
            found = True
    if not found:
        print("No expenses found in this category.")

# enable user to update expenses
def show_expenses(expenses):
    print("\nYour Expenses:")
    for i, expense in enumerate(expenses):
        print(f"{i}. {expense['date']} - {expense['category']} - K{expense['amount']}")


def update_expense(index, category, amount, date):
    """Update an existing expense record."""
    if 0 <= index < len(expenses):
        expenses[index] = {"category": category, "amount": amount, "date": date}

        # recalc total_expenses after update 
        global total_expenses
        total_expenses = sum(expense["amount"] for expense in expenses)
        print("Expense updated successfully.")
    else:
        print("Invalid expense index.")

# Quick test (comment this out when integrating with the full system)
if __name__ == "__main__":
    input_income()
    input_expense()
    print("\nCurrent Data:")
    print("Income:", monthly_income)
    print("Total Expenses:", total_expenses)
    print("Expenses List:", expenses)
while True:
        response = input("Would you like to update an expense? (yes/no) ")
        
        if response.lower() == "yes":
            show_expenses(expenses)
            try:
                index = int(input("Enter the expense index to update e.g.: 0: "))
                category = input("Enter new category: ")
                amount = float(input("Enter new amount: "))
                date = input("Enter new date (YYYY-MM-DD): ")
                update_expense(index, category, amount, date)  # pass list + index
            except ValueError:
                print("Invalid input. Please enter valid data.")
        
        elif response.lower() == "no":
             print("\nCurrent Data:")
             print("Income:", monthly_income)
             print("Total Expenses:", total_expenses)
             print("Expenses List:", expenses)
             break

   