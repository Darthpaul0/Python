name = input("What's your name? ")

if len(name) < 3:
    print("Your name must be at least 3 characters long")
elif len(name) > 50:
    print("Maximum 50 characters")
else:
    print(f"{name} is a good name.")
