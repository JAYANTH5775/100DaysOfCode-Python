age=input("enter the age")
age_as_int=int(age)

years_remaining = 90 - age_as_int
weeks_remaining = 52 * years_remaining
days_reamining = years_remaining * 365
months_remaining = years_remaining*12
print(f"days remainig is :  {days_reamining} \n weeks_remaining : {weeks_remaining} \n years reamaining: {years_remaining}  \n months remaining : {months_remaining}\n ")