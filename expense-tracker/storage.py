import os

FILE_NAME = "expenses.txt"
LIMIT_FILE = "limit.txt"

def add_expense(amount, category):
    with open(FILE_NAME, "a") as f:
        f.write(f"{amount},{category}\n")