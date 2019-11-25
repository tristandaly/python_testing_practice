def add(a, b):
    a = input()
    b = input()
    if a.isalpha() or b.isalpha():
        print("Must provide number")
    else:
        return a + b