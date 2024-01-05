"""
Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""

name=str(input("Hello, What's your name?: "))
length=float(input(f"{name}, What's the length of the room?: "))
width=float(input("and, What's the width of the room?: "))
units=str(input("Are the units in meter or feet?: "))

area=length*width

print(f"The area of the room is {area} square {units}")