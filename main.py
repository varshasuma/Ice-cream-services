print("Thank you for choosing our ice cream Deliveries!")
size = input("Enter your choice: {S, M, L}") 
extra_cocoa = input("Choice of extra cocoa's : {Y or N}") 
extra_popins = input("Choice of extra popins : {Y or N}")
Birthday_wishes = input("If its's a birthday gift, Hurray! you got 20% off : {Y or N}")
bill = 0
if size == 'S':
  bill += 90
elif size == 'M':
  bill += 150
else:
  bill += 200

if extra_cocoa == "Y":
  if size == 's':
    bill += 5
  else: 
    bill += 10

if extra_popins == "Y":
  bill += 5

if Birthday_wishes == "Y":
  discount =(bill * 20) / 100
  bill -= discount
print(f"Your final bill is: {bill}.Thanks for choosing us....Have a nice day.")
