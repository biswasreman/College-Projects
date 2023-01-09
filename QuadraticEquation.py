import cmath

print("General Form :- ax^2 + bx + c = 0")

a = int(input("Enter a (not equal to 0): "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b**2) - (4 * a * c)

sol1 = (-b-cmath.sqrt(d)) / (2 * a * c)
sol2 = (-b+cmath.sqrt(d)) / (2 * a * c)

print("\n")
print(f"Results for equation, {a}x^2 + {b}x + {c} = 0, are:- ")

print(f"The solutions are:- {sol1} and {sol2}")
