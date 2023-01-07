a = int(input("Enter number: "))
num = 0
x = a
while (a > 0):
    num = (num * 10) + a % 10
    a = a // 10

if (x == num):
    print("its a palindrome number")
else:
    print("Its not a palindrome number")

