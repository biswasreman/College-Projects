age = int(input("Enter the age: "))

if (age >= 18):
    print("You're eligible to vote.")

else:
    print("You're not eligible to vote.")
    print(18 - age, "Years remaining to eligible for voting.")

