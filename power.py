base = int(input("Enter the base:\n> "))
exponent = int(input("Enter the exponent:\n> "))


ans = 1

for i in range (1, exponent + 1):
    ans = ans * base


print(base, "to the power of", exponent, "is", ans)




