# .6
n: int = int(input("enter a num: "))
for n in range(n , 0, -1):
    print(n , end=" ")

# .7
num1: int = int(input("enter a number: "))
num2: int = int(input("enter a number: "))
for number in range(num1, num2 + 1):
    if number % 2 == 0:
        print(number, end=' ')

# .8
n: int = int(input("enter a num: "))
for i in range(1, n + 1):
         if i % 3 == 0 or i % 5 == 0:
            print(i, end=" ")
print()

# .9
n: int = int(input("enter a num: "))
for i in range(1, n + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()


