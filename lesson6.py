#A program that determines whether the square root of a given number is an integer.

import math
mynumber=int(input("enter a number: "))
square_root=math.sqrt(mynumber)

print(f"{mynumber}:{square_root:.0f}")


if(square_root==int(square_root)):
    print(f"the square root of {mynumber} is an integer: {int(square_root)}")
else: 
    print(f"the square root of {mynumber} is not integer: {square_root:.3f}")