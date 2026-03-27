from .storage import (
    add_expense,
    get_expenses,
    get_summary,
    remove_expense,
    set_limit,
    get_limit,
    reset_expenses,
)
from .visualize import plot_expenses
import os


# Detect if terminal supports colors
USE_COLORS = os.name != "nt" or "ANSICON" in os.environ


class Colors:
    HEADER = "\033[95m" if USE_COLORS else ""
    BLUE = "\033[94m" if USE_COLORS else ""
    CYAN = "\033[96m" if USE_COLORS else ""
    GREEN = "\033[92m" if USE_COLORS else ""
    WARNING = "\033[93m" if USE_COLORS else ""
    RED = "\033[91m" if USE_COLORS else ""
    END = "\033[0m" if USE_COLORS else ""
    
def print_menu():
    print("\n=== $$$ Expense Tracker $$$===")
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Show summary")
    print("4. Show graph")
    print("5. Show remaining budget")
    print("6. Set/Update monthly limit")
    print("7. Remove expense")
    print("8. Reset all expenses")
    print("9. Exit")

def main():
    while True:
        print_menu()
        choice = input(Colors.BLUE + "Choose an option: " + Colors.END)

        if choice == "1":
            try:
                amount = float(input("Amount (€): "))
                category = input("Category: ")
                add_expense(amount, category)
                print(Colors.GREEN + "Expense added!" + Colors.END)
            except ValueError:
                print(Colors.RED + "Invalid amount!" + Colors.END)

        elif choice == "2":
            expenses = get_expenses()
            if not expenses:
                print(Colors.WARNING + "No expenses found." + Colors.END)
            else:
                print("\nAll Expenses:")
                for e in expenses:
                    print(f"{e['amount']}€ - {e['category']}")

        elif choice == "3":
            total, categories = get_summary()
            print(Colors.GREEN + f"\nTotal spent: {total}€" + Colors.END)
            print("By category:")
            for cat, amt in categories.items():
                print(f"{cat}: {amt}€")

        elif choice == "4":
            plot_expenses()

        elif choice == "5":
            limit = get_limit()
            total, _ = get_summary()

            if limit is None:
                print(Colors.WARNING + "No limit set yet." + Colors.END)
            else:
                remaining = limit - total
                print(Colors.GREEN + f"Limit: {limit}€" + Colors.END)
                print(Colors.GREEN + f"Spent: {total}€" + Colors.END)
                print(Colors.GREEN + f"Remaining: {remaining}€" + Colors.END)
                if remaining < 0:
                    print(Colors.RED + "Warning: You exceeded your budget!" + Colors.END)


        elif choice == "6":
           try:
              limit = float(input("Enter monthly limit (€): "))
              set_limit(limit)
              print("Limit saved!")
           except ValueError:
              print(Colors.RED + "Invalid amount!" + Colors.END)

                       
        
        elif choice == "8":
            confirm = input("Are you sure you want to delete all expenses? (y/n): ")
            if confirm.lower() == "y":
                reset_expenses()
                print("All expenses reset!")
            else:
                print(Colors.WARNING + "Cancelled." + Colors.END)
                
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print(Colors.RED + "Invalid choice!" + Colors.END)