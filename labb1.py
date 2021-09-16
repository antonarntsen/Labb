import math

choice = input("Cube or Tetrahedron (C/T)? ")
if choice == "T" or choice == "t":
    sides = input("Length of tetrahedon (cm): ")
    result = ((float(sides) ** 3)/6) * math.sqrt(2)
    print("The volume of the tetrahedon is ", result, " cm^3")
elif choice == "C" or choice == "c":
    sides = input("Length of cube (cm): ")
    result = float(sides) ** 3
    print("The volume of the cube is ", result, " cm^3")



