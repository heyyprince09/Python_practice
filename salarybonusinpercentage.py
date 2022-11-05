salary = int(input("enter 1st number"))
year = int(input("enter 2nd number"))
if year>10:
    print("you are eligible for 10% bonus",(10/100)*salary + salary )
elif year>6:
    print("you are eligible for 6% bonus",(6/100)*salary + salary)
elif year<6:
    print("you are eligible for 5% bonus",(5/100)*salary + salary)
