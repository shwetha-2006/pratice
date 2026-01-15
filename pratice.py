import sys

def calculate_cube(num):
    """Function to calculate cube of a number"""
    return num ** 3


if __name__ == "__main__":
    print("\n---- Cube of a Number ----\n")
    try:
        # Case 1: Argument passed (for Jenkins or CLI)
        if len(sys.argv) == 2:
            num = float(sys.argv[1])

        # Case 2: No argument passed (for console use)
        else:
            num = float(input("Enter a number: "))

        cube = calculate_cube(num)

        print(f"\nNumber: {num}")
        print(f"Cube = {cube}\n")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
