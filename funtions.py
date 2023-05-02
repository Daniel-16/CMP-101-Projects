# def nameoffunction():
#     print("hello")
#     print("world")
# nameoffunction()

def calculateVelocity():
    distance = float(input("Enter distance "))
    time = int(input("Enter time "))
    print(f'The velocity is {distance/time}')

calculateVelocity()

def calculateVelocity(u, a, t):
    print(u + (a * t))
calculateVelocity(12, 10, 60)

#Static Polymorphism/Overlaoding - Multiple methods with the same name but different functions
#Overloading can be dynamic