def add(P,Q):
    return P + Q
def sub(P,Q):
    return P - Q
def mul(P,Q):
    return P * Q
def div(P,Q):
    return P / Q

print("Please select an operation?\nA) Addition\nB) Subtraction\nC) Multiplication\nD) Division\n")

choice = input(str("Your choice, a, b, c or d: "))

num1 = int(input("\nfirst number being operated: "))
num2 = int(input("second number being operated: "))

if choice == "a":
    print(add(num1, num2))
elif choice == "b":
    print(sub(num1, num2))
elif choice == "c":
    print(mul(num1, num2))
elif choice == "d":
    print(div(num1, num2))
else:
    print("invalid input")