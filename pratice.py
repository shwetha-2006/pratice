import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    celsius = float(sys.argv[1])
    result = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", result)
