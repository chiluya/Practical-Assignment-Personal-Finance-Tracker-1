# ================================
# Personal Finamce Tracker - Student A
# ================================

# Define variables
monthly_income = float(input("Enter your monthly income: "))
total_expenses = 0.0
savings_goal = float(input("Enter your savings goal: "))

# Create a function to add income
def add_income(amount):
    global monthly_income
    if amount > 0:
        monthly_income += amount
        print(f"Income of {amount} added. Total income: {monthly_income}")
    else:
        print("Income amount must be positive.")
        
# Create a list to store expenses
expenses = []

# Create a function to add expense
def add_expense(category, amount, date):
    global total_expenses
    if amount > 0:
        expense = {"Category": category, "Amount": amount, "Date": date}
        expenses.append(expense)
        total_expenses += amount
        print(f"Expense of {amount} added. Total expense: {total_expenses}")
    else:
        print("Expense amount must be positive.")

# Prompt the user to enter an expense
def input_expense():
    category = input("Enter the category of your expense: ")
    amount = float(input("Enter the expense: "))
    date = input("Enter the date(YYYY-MM-DD): ")
    try:
        add_expense(category, amount, date)
        print("")
    except ValueError:
        print("Invalid input. Please enter numbers for amount.")

# Show expenses to prompt the choose an index of an expense
def show_expenses(expenses):
    print("\n Your Expenses")
    for i, expense in enumerate(expenses):
        print(f"{i}. {expense["Date"]} - {expense["Category"]} - K{expense["Amount"]}")

# Prompt the user to update existing expense
def update_expense(index, amount, date):
    if 0 <= index < len(expenses):
        old_category = expenses[index]["Category"]
        expenses[index] = {"Category": old_category, "Amount": amount, "Date": date}

        global total_expenses
        total_expenses = sum(expense["Amount"] for expense in expenses)
        print("Expense updated successfuly!")
    else:
        print("Invalid expense index!")

# Enable user to search expenses by category
def search_expenses_by_category():
    search_category = input("Enter category to search: ")
    found = False
    print("\nExpenses in category: ",search_category)
    for expense in expenses:
        if expense["Category"].lower() == search_category.lower():
            print("Amount for", search_category, "is: ", expense["Amount"], "on", expense["Date"])
            found = True
    if not found:
        print("Expenses not found in this category.")

# integrate everything
input_expense()
# Loop 
while True:
    add = input("Would you like to enter an expense? (yes/no)")
    if add.lower() == "yes":
         category = input("Enter the category of your expense: ")
         amount = float(input("Enter the expense: "))
         date = input("Enter the date(YYYY-MM-DD): ")
         try:
            add_expense(category, amount, date)
            print("")
         except ValueError:
            print("Invalid input. Please enter numbers for amount.")

    elif add.lower() == "no":
        break
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
                amount = float(input("Enter new amount: "))
                date = input("Enter new date (YYYY-MM-DD): ")
                update_expense(index, amount, date)  # pass list + index
            except ValueError:
                print("Invalid input. Please enter valid data.")
        
        elif response.lower() == "no":
             print("\nCurrent Data:")
             print("Income:", monthly_income)
             print("Total Expenses:", total_expenses)
             print("Expenses List:", expenses)
             break


