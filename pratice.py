import sys

if len(sys.argv) != 2:
    print("Usage: python pratice.py <celsius>")
    sys.exit(1)

celsius = float(sys.argv[1])
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
