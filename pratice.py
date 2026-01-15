def is_palindrome(text):
    return text == text[::-1]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python palindrome.py <text>")
        sys.exit(1)
    print("Palindrome" if is_palindrome(sys.argv[1]) else "Not Palindrome")
