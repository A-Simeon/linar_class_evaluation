print("welcome to simeon taxcalculator")
user_name=input("enter your name")
print(user_name)
print("simeon_calculator for calculating tax calculation")

#for private

monthly_salary =float(input("enter your montly salary"))
tax = (monthly_salary/100*10)
print(tax)
leftover = (monthly_salary - tax)
print("your leftover is ",leftover)
print("thanks for using my tax calculator")