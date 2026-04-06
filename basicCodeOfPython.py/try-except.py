def area(width, length):
    return width*length

width = int(input("Enter the width of the rectangle:"))
length = int(input("Enter the length of the rectangle:"))
try:
    result = area(width,length)
    print(f"The area of the rectangle is: {result}")

except ValueError:
    print("Please enter valid numbers for width and length.")


# example for try-except block to handle file not found error
file_name = "sample.txt"
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found -", file_name)