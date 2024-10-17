import statistics

# .11
sum_negative = 0
while True:
    num: int = int(input("enter a number: "))
    if num == 0:
        break
    if num < 0:
        sum_negative += num
print(sum_negative)

# .12
num_list: list[int] = []
for i in range(1,10 + 1):
    num: int = int(input("enter a number :"))
    num_list.append(i)
print(num_list[::-1])

# .13
sum_rishoni = 0
divider = 2
while True:
    num: int = int(input("enter a number: "))
    if num == 0:
        break
    elif num == 1:
        pass
    while divider < num:
        if num % divider == 0:
            break
        divider += 1
        sum_rishoni += 1
print(sum_rishoni)

# .14
above_avg = 0
numbers: list[int] = []
for i in range(5):
    num: int = int(input("enter number: "))
    numbers.append(num)
avg = statistics.mean(numbers)
for i in range(len(numbers)):
    if numbers[i] > avg:
        above_avg += 1
print(f"avg = {statistics.mean(numbers)}")
print(f"above avg = {above_avg}")

# .15
f_n: int = int(input("enter a number: "))
s_n: int = int(input("enter a number: "))
num = (f_n // s_n)
print(f"({f_n} / {s_n})" ,"=", num)
