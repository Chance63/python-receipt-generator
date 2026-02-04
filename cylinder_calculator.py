import math

#Grabs user input to obtain radius and height
radius = float(input("Please enter the radius of the cylinder: "))
height = float(input("Please enter the height of the cylinder: "))

#Calculates surface area and volume from user input
surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
volume = math.pi * radius ** 2 * height

#Calculates the rounding of the answers
surface_area = round(surface_area, 2)
volume = round(volume, 2)

#Prints our calcualted input
print(f"Surface area of the cylinder is {surface_area} square units.")
print(f"Volume of the cylinder is {volume} cubic units.")
