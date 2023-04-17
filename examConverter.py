#Exam Score Converter
grade = int(input("Enter your grade number__ "))

if grade >= 70 and grade <= 100:
    print("Your grade is equivalent to an A")
elif grade >= 60 and grade <= 69:
    print("Your grade is equivalent to a B")
elif grade >= 50 and grade <= 59:
    print("Your grade is equivalent to a C")
elif grade >= 40 and grade <= 49:
    print("Your grade is equivalent to an D")    
else:
    print("Oops! Your grade point is an F")