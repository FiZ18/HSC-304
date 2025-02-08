def calculate_rectangle_area(length, width):
    return length * width

def main():
    print("Enter the dimensions of the rectangle:")
    length = float(input("Length: "))
    width = float(input("Width: "))
    
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()