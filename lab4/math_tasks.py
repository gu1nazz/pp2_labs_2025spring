#1
import math

# Get the value of degrees from the user
degree = float(input(" Enter the degree value:"))

# Convert to radians
radian = math.radians(degree)

print("Градус:",degree)
print("Радиан:" ,radian)

#2
# Enter the trapezoid parameters
height = float(input("Enter the height value:"))
base1 = float(input("Enter the first base value:"))
base2 = float(input("Enter the second base value:"))

# Calculation of the area
area = (base1 + base2) * height / 2

print("Area of the trapezoid:", area)

#3
import math

# Enter parameters
num_sides = int(input("Number of ribs: "))
side_length = float(input("Length of one wall: "))

# Calculation of the area
area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

print("Area of a right Polygon:" ,area)

#4

# Enter parameters
base = float(input("Base length:"))
height = float(input("Height: "))

# Calculation of the area
area = base * height

print("Area of the parallelogram:",area)



