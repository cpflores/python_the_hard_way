def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# calls function, passing two arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# gives values to variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# calls function, passing two variables for arguements
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calls function, passes value math for arguements 
print("We can even do math innside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# calls function, passes variables for values and math for arguements
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)