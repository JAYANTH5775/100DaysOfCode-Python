height = float(input("enter your height"))
weight = float(input("enter your weight"))

bmi = round(weight / height **2 )
if bmi < 18:
    print(f"your bmi is : {bmi } :your underweight")
elif  bmi < 25:
    print(f"your bmi is : {bmi } :your totally fine :) normal weight")
elif bmi < 30:
    print("your over weight ")
elif bmi < 35:
    print(f"your bmi is : {bmi } :your obese\n")
else:
    print(f"your bmi is : {bmi } :clincally obese\n")