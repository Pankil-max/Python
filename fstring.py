letter="My name is {1} and I am from {0}"
name="Pankil"
country="Jhapa"
print(letter.format(country,name))
# Fstrings
print(f"My name is {name} and I am from{country}")

price=39.0999
print(f"Price of new Hoodie ={price:.2f} dollars!!")