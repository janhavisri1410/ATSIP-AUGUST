import tkinter as tk
from tkinter import messagebox

unit_price = {}
description = {}
stock = {}

try:
    with open("stock.txt", "r") as details:
        no_items = int(details.readline().rstrip("\n"))

        for i in range(no_items):
            line = details.readline().rstrip("\n")
            x1, x2 = line.split("#")
            x1 = int(x1)
            x2 = float(x2)
            unit_price[x1] = x2

        for i in range(no_items):
            line = details.readline().rstrip("\n")
            x1, x2 = line.split("#")
            x1 = int(x1)
            description[x1] = x2

        for i in range(no_items):
            line = details.readline().rstrip("\n")
            x1, x2 = line.split("#")
            x1 = int(x1)
            x2 = int(x2)
            stock[x1] = x2

except FileNotFoundError:
    print("Stock empty")

finally:
    try:
        details.close()
    except NameError:
        pass


cart = []
total_cost = [0]  # Use a list to store the total cost
flag = 0


def add_item():
    p_no = int(item_number_entry.get())
    p_pr = float(item_price_entry.get())
    p_desc = item_description_entry.get()
    p_stock = int(item_stock_entry.get())

    m = 0
    while p_no in unit_price:
        p_no += 1
        m = 1
    if m == 1:
        messagebox.showinfo(
            "Item Number Exists", f"That item number already exists :( Changing value to {p_no}"
        )

    unit_price[p_no] = p_pr
    description[p_no] = p_desc
    stock[p_no] = max(0, p_stock)

    messagebox.showinfo(
        "Item Added",
        f"Item number: {p_no}\nDescription: {description[p_no]}\nPrice: {unit_price[p_no]}\nStock: {stock[p_no]}\nItem was added successfully!",
    )

    item_number_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)
    item_description_entry.delete(0, tk.END)
    item_stock_entry.delete(0, tk.END)


def remove_item():
    def confirm_remove():
        p_no = int(remove_item_entry.get())

        if p_no in unit_price:
            unit_price.pop(p_no)
            description.pop(p_no)
            stock.pop(p_no)
            messagebox.showinfo("Item Removed", "Item successfully removed!")
        else:
            messagebox.showinfo("Item Not Found", "Sorry, we don't have such an item!")

        remove_window.destroy()
        item_number_entry.delete(0, tk.END)

    remove_window = tk.Toplevel(window)
    remove_window.title("Remove Item")

    remove_label = tk.Label(remove_window, text="Enter Item Number to Remove:")
    remove_label.pack()

    remove_item_entry = tk.Entry(remove_window)
    remove_item_entry.pack()

    confirm_button = tk.Button(remove_window, text="Confirm", command=confirm_remove)
    confirm_button.pack()


def list_items():
    items = ""
    for item_no in unit_price:
        items += f"Item number: {item_no} | Description: {description[item_no]} | Price: {unit_price[item_no]} | Stock: {stock[item_no]}\n"

    messagebox.showinfo("Items List", items)


def purchase_item():
    def confirm_purchase():
        p_no = int(purchase_item_entry.get())

        if p_no in unit_price:
            if stock[p_no] > 0:
                stock_current = stock[p_no]
                stock[p_no] = stock_current

                item_price = unit_price[p_no]
                total_cost[0] += item_price  # Update the total_cost variable using the list
                messagebox.showinfo("Item Added to Cart", f"{description[p_no]} added to cart: ${item_price}")
                cart.append(p_no)
            else:
                messagebox.showinfo("Out of Stock", "Sorry! We don't have that item in stock!")
        else:
            messagebox.showinfo("Item Not Found", "Sorry! We don't have such an item!")

        purchase_window.destroy()
        item_number_entry.delete(0, tk.END)

    purchase_window = tk.Toplevel(window)
    purchase_window.title("Purchase Item")

    purchase_label = tk.Label(purchase_window, text="Enter Item Number to Purchase:")
    purchase_label.pack()

    purchase_item_entry = tk.Entry(purchase_window)
    purchase_item_entry.pack()

    confirm_button = tk.Button(purchase_window, text="Confirm", command=confirm_purchase)
    confirm_button.pack()


def checkout():
    def show_checkout():
        items_purchased = "You bought the following items:\n"
        for item_no in cart:
            items_purchased += f"Item number: {item_no} | Description: {description[item_no]} | Price: {unit_price[item_no]}\n"

        messagebox.showinfo("Checkout", items_purchased)

        tax = round(0.12 * total_cost[0], 2)
        total = round(total_cost[0] + tax, 2)

        messagebox.showinfo(
            "Total Cost", f"Total: ${round(total_cost[0], 2)}\nTax is 12%: ${tax}\nAfter Tax: ${total}"
        )

        total_cost[0] = 0  # Reset the total_cost to zero
        flag = 1

        cart.clear()

        checkout_window.destroy()

    checkout_window = tk.Toplevel(window)
    checkout_window.title("Checkout")

    confirm_button = tk.Button(checkout_window, text="Confirm Checkout", command=show_checkout)
    confirm_button.pack()


# Create a Tkinter GUI window
window = tk.Tk()
window.title("Inventory Management System")

# Create and configure GUI widgets
welcome_label = tk.Label(window, text="Welcome to Inventory Management System")
welcome_label.pack()

item_number_label = tk.Label(window, text="Item Number:")
item_number_label.pack()

item_number_entry = tk.Entry(window)
item_number_entry.pack()

item_price_label = tk.Label(window, text="Item Price:")
item_price_label.pack()

item_price_entry = tk.Entry(window)
item_price_entry.pack()

item_description_label = tk.Label(window, text="Item Description:")
item_description_label.pack()

item_description_entry = tk.Entry(window)
item_description_entry.pack()

item_stock_label = tk.Label(window, text="Item Stock:")
item_stock_label.pack()

item_stock_entry = tk.Entry(window)
item_stock_entry.pack()

add_button = tk.Button(window, text="Add", command=add_item)
add_button.pack()

remove_button = tk.Button(window, text="Remove", command=remove_item)
remove_button.pack()

list_button = tk.Button(window, text="List", command=list_items)
list_button.pack()

purchase_button = tk.Button(window, text="Purchase", command=purchase_item)
purchase_button.pack()

checkout_button = tk.Button(window, text="Checkout", command=checkout)
checkout_button.pack()

# Run the GUI event loop
window.mainloop()
