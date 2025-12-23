# ============================================================
# SWIGGY FOOD ORDERING SYSTEM – DEMONSTRATION OF ALL DATA TYPES
# This program collects food order details from a Swiggy user
# and stores them using different Python data types.
# ============================================================

# Task - 1
# ---------------- STRING DATA TYPE ----------------
# Used to store customer name
customer_name = input("Enter Customer Name: ")


# ---------------- INTEGER DATA TYPE ----------------
# Used to store order ID
order_id = int(input("Enter Order ID: "))


# ---------------- FLOAT DATA TYPE ----------------
# Used to store total bill amount
total_bill = float(input("Enter Total Bill Amount: "))


# ---------------- LIST DATA TYPE ----------------
# Used to store multiple food items ordered
# split() converts input into a list
food_items = input("Enter Food Items (Pizza Burger Fries): ").split()


# ---------------- TUPLE DATA TYPE ----------------
# Used to store fixed delivery time (HH MM)
# tuple is immutable (cannot be changed)
delivery_time = tuple(
    map(int, input("Enter Delivery Time (HH MM): ").split())
)


# ---------------- SET DATA TYPE ----------------
# Used to store unique add-ons
# Duplicate add-ons are removed automatically
addons = set(
    input("Enter Add-ons (ExtraCheese Mayo Coke): ").split()
)


# ---------------- DICTIONARY DATA TYPE ----------------
# Used to store all order details together
order_details = {
    "Customer Name": customer_name,
    "Order ID": order_id,
    "Total Bill": total_bill,
    "Food Items": food_items,
    "Delivery Time": delivery_time,
    "Add-ons": addons
}

# Task - 2
# ---------------- OUTPUT SECTION ----------------
print("\n--- SWIGGY ORDER DETAILS ---\n")


# ---------------- COMMA SEPARATION PRINTING ----------------
# sep=", " separates values using comma
print("Customer Name, Order ID, Total Bill",
      order_details["Customer Name"],
      order_details["Order ID"],
      order_details["Total Bill"],
      sep=", ")


# ---------------- PERCENTAGE / NUMERIC FORMATTING ----------------
# Display bill with 2 decimal places
print("Total Bill Amount: ₹%.2f" % order_details["Total Bill"])


# ---------------- F-STRING FORMATTING ----------------
# Display delivery time in readable format
print(f"Delivery Time: {delivery_time[0]}:{delivery_time[1]}")

# Display ordered food items
print(f"Food Items Ordered: {food_items}")

# Display selected add-ons
print(f"Add-ons Selected: {addons}")


# ---------------- FORMAT() METHOD ----------------
# Formatting using format() method
print("Customer: {}, Order ID: {}".format(
    order_details["Customer Name"],
    order_details["Order ID"]
))
