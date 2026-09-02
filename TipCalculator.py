print("Welcome to the tip calculator!")
bill = int(input("what was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
persons = int(input("How many people to split the bill?"))
total_bill= (tip/100)*bill + bill
each_person = round(total_bill/persons,2)
print(f"Each person should pay: ${each_person}")
