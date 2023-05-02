# class Physics:
#     gravity = 9.8 #Attribute of classes
#     def potentialEnergy(Self, m, h): #Behaviors/Method
#         return m * Self.gravity * h

# physics = Physics()
# print(physics.potentialEnergy(12, 10))

class ThemePark:
    age = int(input("Enter your age "))
    height = float(input("Enter your height "))
    def checkEligigibility(self):
        if (self.age >= 17 or self.height >= 179):
            return "Welcome to wonderland"
        else:
            return "You are ineligible"
print(ThemePark().checkEligigibility())