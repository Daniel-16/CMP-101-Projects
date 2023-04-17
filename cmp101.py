num1 = int(input('Enter a number '))
num2 = int(input('Enter another number '))
sum = num1 + num2
if num1 and num2 % 2 == 0:
    print(sum + 1)
elif num1 % 2 and num2 % 2 > 0:
    print(sum + 2)
else:
    print(sum + 3)