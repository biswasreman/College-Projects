fir = int(input("Enter first number:\n> "))
sec = int(input("Enter second number:\n> "))
thi = int(input("Enter third number:\n> "))

if (fir > sec) and (fir > thi):
    print(f"{fir} is the largest number.")
elif (sec > fir) and (sec > thi):
    print(f"{sec} is the largest number.")
else:
    print(f"{thi} is the largest number.")



