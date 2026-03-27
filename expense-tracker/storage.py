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

def get_summary():
    expenses = get_expenses()
    total = 0
    categories = {}

    for e in expenses:
        total += e["amount"]
        cat = e["category"]

        if cat not in categories:
            categories[cat] = 0

        categories[cat] += e["amount"]

    return total, categories
