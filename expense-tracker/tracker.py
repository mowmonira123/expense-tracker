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