command = ""
is_started = False
print("> You're in the car, what do you want to do?")
while 1+1:
    command = input("> ").lower()
    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == "start":
        if is_started:
            print("Car is already started!")
        else:
            is_started = True
            print("The car is now started...")
    elif command == "stop":
        if not is_started:
            print("Car is already stopped!")
        else:
            is_started = False
            print("The car is now stopped...")
    elif command == "quit":
        print('You left the car.')
        break
    else:
        print("Don't understand that. Try help.")

