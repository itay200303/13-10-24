# .1
num: float = float(input("enter a number: "))
if num > 10:
    num = num - 10
elif num < 10:
    num = num * 10
else:
    print("put a number in the right condition")
print(int(num))

# .2
num1: float = float(input("enter a number: "))
num2: float = float(input("enter a number: "))
num3: float = float(input("enter a number: "))
score = num1 + num2 + num3
print(f"{score}" if score  > 100 else "score is lower than 100")

# .3
num1: float = float(input("enter a number: "))
num2: float = float(input("enter a number: "))
frac1 = num1 - int(num1)
frac2 = num2 - int(num2)
if frac1 > frac2:
    print(f"the bigger fraction is: {frac1}")
elif frac2 > frac1:
    print(f"the bigger fraction is: {frac2}")
else:
    print("equals")
print()

# .4
age: int = int(input("enter age: "))
print(f"{age}" if 0 <= age <= 120 else "age is not in the right condition")

# .5
num: int = int(input("enter a 3 digit number: "))
middle_digit = num / 10 % 10
print(int(middle_digit))
