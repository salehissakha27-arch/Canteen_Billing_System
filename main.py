from canteen import *
from canteen_pkg.ActualTask import display_menu, generate_bill

items = {
    "Burger": 2,
    "Coffee": 1
}

display_menu()
generate_bill(items, 10)
