import random
user=input("Snake or Gun or Water:").lower()
choices=["snake","water","gun"]
computer_choice=random.choice(choices)
print(f"Computer chooses:{computer_choice}")

rules={
    "snake":"water",
    "gun":"snake",
    "water":"gun"

}
if(user==computer_choice):
    print("Its a TIE!!!")

elif(rules[user]==computer_choice):
    print("USER WON!!!!")
else:
    print("COMPUTER WON!!!")