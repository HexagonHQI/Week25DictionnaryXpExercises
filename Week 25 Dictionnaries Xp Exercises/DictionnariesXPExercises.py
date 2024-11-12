#Exercise 1 : Convert Lists into Dictionaries
#Convert the lists keys and values into a dictionary.


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Using zip() to combine keys and values into a dictionary
result = dict(zip(keys, values))
print(result)
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

 #Exercise 2 : Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for member, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    total_cost += price
    print(f"{member.capitalize()} has to pay: ${price}")

print("Total cost for the family:", total_cost)

#bonus

family = {}
while True:
    name = input("Enter a family member's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

# Reuse the calculation logic above
total_cost = 0
for member, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    total_cost += price
    print(f"{member.capitalize()} has to pay: ${price}")

print("Total cost for the family:", total_cost)

# Exercise 3 : Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

#Change the number of stores to 2.
brand["number_stores"] = 2

#Print a sentence about Zara's clients.
print("Zara offers clothing for men, women, children, and home decor.")

#Add country_creation with value "Spain"
brand["country_creation"] = "Spain"

#Add Desigual to international_competitors if the key exists.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#Delete the creation_date.
del brand["creation_date"]

#Print the last international_competitor.
print("Last international competitor:", brand["international_competitors"][-1])

#Print the US major colors.
print("Major colors in the US:", brand["major_color"]["US"])

#Print the dictionary length.
print("Number of key-value pairs:", len(brand))

#Print all dictionary keys.
print("Keys in the dictionary:", list(brand.keys()))

#Create and merge more_on_zara with brand.
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)

#Print number_stores and explain what happened.
print("Number of stores:", brand["number_stores"])  # The value updated to 10000 due to the merge with more_on_zara.

#Exercise 4 : Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. disney_users_A: Create a dictionary with characters as keys and indexes as values
disney_users_A = {user: index for index, user in enumerate(users)}
print(disney_users_A)

# 2. disney_users_B: Create a dictionary with indexes as keys and characters as values
disney_users_B = {index: user for index, user in enumerate(users)}
print(disney_users_B)

# 3. disney_users_C: Create a dictionary with characters sorted alphabetically as keys
disney_users_C = {user: index for index, user in enumerate(sorted(users))}
print(disney_users_C)

# Additional requirements:
# Only recreate disney_users_A for characters with the letter "i"
disney_users_A_i = {user: index for index, user in enumerate(users) if 'i' in user}
print(disney_users_A_i)

# Only recreate disney_users_A for characters whose names start with "m" or "p"
disney_users_A_mp = {user: index for index, user in enumerate(users) if user[0].lower() in ['m', 'p']}
print(disney_users_A_mp)

