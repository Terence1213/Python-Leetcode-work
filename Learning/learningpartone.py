import time
my_number = 10

print(f"Hello, my number is {my_number}")

# Note: The pow() doesn't require importing of the math class

fullname = "Terence Portelli"

name = fullname.split(" ")

first_name = name[0]
second_name = name[1] 

print(first_name)
print(second_name)

firstName = fullname[0:7]
secondName = fullname[8:]

print(firstName)
print(secondName)

price1 = 3.14159

print(f"Price 1 is ${price1:.2f}") # Displaying by 2 decimal places

entered_time = int(input("Please enter the timer: "))

for x in range(entered_time, 0, -1):
    seconds = int(x % 60)
    minutes = int((x / 60) % 60)
    hours = int(((x / 60) / 60))

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Timer's up!");

fruits = ["Apple", "Orangee"]
fruits.append("Banana")
fruits.remove("Apple")
fruits.insert(0, "Pineapple")
fruits.sort()

vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[1][1])

# Tuples -> Cannot be changed after initialisation
names = ("Terence", "Adam", "Ylenia", "Neil")

# practical use for sets: Eliminating duplicate values.
emails = ["a@example.com", "b@example.com", "a@example.com"]
unique_emails = set(emails)

tutorial_teachers = {"Terence", "Adam", "Ylenia"}
lecturer_teachers = {"Neil", "Terence", "Dale"}

flexible_teachers = tutorial_teachers & lecturer_teachers # Gets common elements between the 2 sets
print(flexible_teachers)

just_tutorial_teachers = tutorial_teachers - flexible_teachers 
# This gets the teachers which are only contained in tutorial teachers, and ignores the teachers which exist in both tutorial_teachers and flexible_teachers
print (just_tutorial_teachers)

single_purpose_teachers = tutorial_teachers ^ lecturer_teachers # Displays which teachers have only one purpose, either tutorial or lecturer
print (single_purpose_teachers)

# Dictionaries: 

menu_prices = {
    "pizza" : 13.50,
    "carbonara pasta" : 14.00,
    "nigger" : 12,
    "apple" : 3,
    "pineapple": 4
}

print(menu_prices["pizza"])

if menu_prices.get("Banana"):
    print("Banana exists in the meun!")
else:
    print("Banana doesn't exist in the menu!")

print("Pizza price: ", menu_prices.get("pizza"))

menu_prices.pop("carbonara pasta")

for key in menu_prices.keys():
    print(key)

for value in menu_prices.values():
    print(value)

for key, value in menu_prices.items():
    print(f"{key}: {value}")

cart = []
total_price = 0

while True:
    food = input("Enter the food which you want to add to the cart ('q' to confirm order): ").lower()

    if food == "q":
        print("Order complete.")
        break
    elif menu_prices.get(food):
        cart.append(f"{food}: ${menu_prices.get(food)}")
        total_price += menu_prices.get(food)
    else:
        print("The food you entered doesn't exist in the menu!")

if len(cart) == 0:
    print("No food has been purchased!")
else:
    # We now have to display all of the food which the customer has in their cart, and ask them to confirm or cancel their purchace.
    print("Cart: ")
    for item in cart:
        print(item)

    print(f"Total price: ${total_price}")

    while True:
        choice = input("Enter 'y' to confirm purchase, or 'n' to cancel purchase").lower()
        
        if choice == "y":
            print(f"Food succesfully purchased! Your balance went down by {total_price}")
            break
        elif choice == 'n':
            print("Food purchase cancelled")
            break
        else:
            print("Invalid input! Please enter either 'y' or 'n'")
