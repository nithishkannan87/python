

# Pizza Category
print("\nPizza Categories")
print("1. Normal")
print("2. Delux")
cat = int(input("Enter your Choice [1 or 2]: "))

# Pizza Type
print("\nPizza Types")
print("1. Veg")
print("2. Non Veg")
ptype = int(input("Enter your Choice [1 or 2]: "))

# Base price calculation
if cat == 1 and ptype == 1:      # Normal Veg
    base_price = 200.0
elif cat == 1 and ptype == 2:    # Normal Non-Veg
    base_price = 400.0
elif cat == 2 and ptype == 1:    # Delux Veg
    base_price = 300.0
else:                            # Delux Non-Veg
    base_price = 500.0

total = base_price

# Extra Cheese
cheese = int(input("\nEnter Cheese? [1.Yes or 2.NO]: "))
extra_cheese = 0
if cheese == 1:
    extra_cheese = 100.0
    total += extra_cheese

# Extra Topping
topping = int(input("Enter Topping? [1.Yes or 2.NO]: "))
extra_topping = 0
if topping == 1:
    extra_topping = 100.0
    total += extra_topping

# Water Bottles
water = int(input("\nDo you want Water Bottles? [1.Yes or 2.NO]: "))
water_cost = 0
if water == 1:
    bottles = int(input("How many bottles?: "))
    water_cost = bottles * 20.0
    total += water_cost

# Ketchup
ketchup = int(input("\nDo you want Ketchup? [1.Yes or 2.NO]: "))
ketchup_cost = 0
if ketchup == 1:
    packets = int(input("How many Packets?: "))
    ketchup_cost = packets * 5.0
    total += ketchup_cost

# Soft Drinks
soft = int(input("\nDo you want Soft Drinks? [1.Yes or 2.NO]: "))
soft_cost = 0
if soft == 1:
    cans = int(input("How many Cans?: "))
    soft_cost = cans * 75.0
    total += soft_cost

# Take Away
takeaway = int(input("\nIs it a Take Away? [1.Yes or 2.NO]: "))
takeaway_charge = 0
if takeaway == 1:
    takeaway_charge = 20.0
    total += takeaway_charge

# GST (18%)
gst = total * 0.18
net_amount = total + gst

# Bill Display
print("\n----------------------------------")
print("** Pizza Bill Generator **")
print("----------------------------------")
print(f"Base Price         = {base_price}")
print(f"Extra Cheese       = {extra_cheese}")
print(f"Extra Toppings     = {extra_topping}")
print(f"Water Bottle       = {water_cost}")
print(f"Ketchup Packets    = {ketchup_cost}")
print(f"Soft Drinks        = {soft_cost}")
print(f"Take Away Charges  = {takeaway_charge}")
print("----------------------------------")
print(f"Total Cost         = {total}")
print(f"GST Charges (18%)  = {gst}")
print("----------------------------------")
print(f"Net Amount Payable = {net_amount}")