def get_side_length(prompt):
    while True:
        try:
            length = int(input(prompt))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            return length
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

def determine_triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "EQUILATERAL"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "ISOSCELES"
    else:
        return "SCALENE"

def main():
    side1 = get_side_length("Enter length of side one: ")
    side2 = get_side_length("Enter length of side two: ")
    side3 = get_side_length("Enter length of side three: ")

    triangle_type = determine_triangle_type(side1, side2, side3)
    print(triangle_type)

if __name__ == "__main__":
    main()
