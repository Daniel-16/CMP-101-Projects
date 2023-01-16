name = input("What is your name? ")
birthyear = int(input("What year were you born? "))
department = input("What department are you in? ")
level = int(input("What level are you in? "))
age = 2023 - birthyear
print(f'Welcome {name}. You are {age} years old in {level} level, {department} department.')
