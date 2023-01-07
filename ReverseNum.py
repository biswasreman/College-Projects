i = int(input("Enter the number:\n> "))
rev = 0
while (i > 0):
    rev = (rev * 10) + i % 10
    i = i//10
    
print("The reverse of your given number is: ", rev)
     


