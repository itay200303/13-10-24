
# .16
three_digit_num: int = int(input("enter a 3 digit number: "))
ahadot = three_digit_num  % 10
asarot = three_digit_num // 10 % 10
maot = three_digit_num // 100
sum_num = ahadot + asarot + maot
if 100 <= three_digit_num <= 999:
    if three_digit_num % 3 == 0:
        print("divided by 3")
    else:
        print("not divided by 3")
print(f"the result is: {maot} + {asarot} + {ahadot} = {sum_num} ")

# .17
word: str = str(input("enter a word: "))
reverse = word.replace(" ", "").lower()
if reverse == word[::-1]:
    print(f"the str: {word} is reversed")
else:
    print(f"the str: {word} isn't reversed")




