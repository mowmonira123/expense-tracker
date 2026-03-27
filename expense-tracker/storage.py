import os

FILE_NAME = "expenses.txt"
LIMIT_FILE = "limit.txt"

def add_expense(amount, category):
    with open(FILE_NAME, "a") as f:
        f.write(f"{amount},{category}\n")
        
        
def get_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    expenses = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            amount, category = line.strip().split(",")
            expenses.append({
                "amount": float(amount),
                "category": category
            })
    return expenses