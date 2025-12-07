import sys
import string

def main(): 
    """ Main of the Program """

    text = ""
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return 1
    if len(sys.argv) == 1:
        print("What is the text to count?")
        text = sys.stdin.readline()
    else:
        text = sys.argv[1]
    lower_case = 0
    upper_case = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper_case += 1
        elif char.isdigit():
            digits += 1
        elif char.islower():
            lower_case += 1
        elif char.isspace():
            spaces += 1
        elif char in string.punctuation:
            punctuation += 1
    
    print(f"The text contains {len(text)} characters:")
    print(f"{upper_case} upper letters")
    print(f"{lower_case} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")
    return 0

if __name__ == "__main__":
    main()