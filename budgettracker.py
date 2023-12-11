import json
import os


data_file = 'budget_data.json'


if os.path.exists(data_file):
    with open(data_file, 'r') as file:
        budget_data = json.load(file)
else:
    budget_data = {'budget': 0, 'expenses': []}


def update_data():
    with open(data_file, 'w') as file:
        json.dump(budget_data, file, indent=4)


def set_budget():
    budget = float(input("Enter your monthly budget: "))
    budget_data['budget'] = budget
    update_data()
    print("Monthly budget set to ${:.2f}".format(budget))


def add_expense():
    amount = float(input("Enter the expense amount: $"))
    category = input("Enter the expense category: ")
    budget_data['expenses'].append({'amount': amount, 'category': category})
    update_data()
    print("Expense recorded.")


def display_report():
    total_expenses = sum(expense['amount'] for expense in budget_data['expenses'])
    print("\nBudget Report:")
    print("Total Budget: ${:.2f}".format(budget_data['budget']))
    print("Total Expenses: ${:.2f}".format(total_expenses))
    print("Remaining Budget: ${:.2f}".format(budget_data['budget'] - total_expenses))
    print("\nExpenses by Category:")
    for category in set(expense['category'] for expense in budget_data['expenses']):
        total = sum(expense['amount'] for expense in budget_data['expenses'] if expense['category'] == category)
        print(f"{category}: ${total:.2f}")


while True:
    print("\nPersonal Budget Planner")
    print("1. Set Monthly Budget")
    print("2. Add an Expense")
    print("3. Display Budget Report")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        set_budget()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        display_report()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
