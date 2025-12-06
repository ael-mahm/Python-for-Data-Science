import sys

if len(sys.argv) == 1:
    exit()
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    exit()

num = sys.argv[1].lstrip("-")
if not num.isdigit():
    print("AssertionError: argument is not an integer")
    exit()

num = int(sys.argv[1])
if num % 2 == 0 :
    print("I'm Even.")
else:
    print("I'm Odd.")