import matplotlib.pyplot as plt
from .storage import get_summary


def plot_expenses():
    total, categories = get_summary()

    if not categories:
        print("No data to display.")
        return
    labels = list(categories.keys())
    values = list(categories.values())
    
    plt.figure()