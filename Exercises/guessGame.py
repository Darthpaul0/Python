print('''
From 1 to 10, guess the number I'm thinking of!
You only have 3 attempts''')


secret_number = 5
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    guess = int(input("Guess: "))
    attempts += 1
    if guess != secret_number:
        print(f'You failed!')
    else:
        print(f'Congrats, {secret_number} is the right number.')
        break
else:
    print("Sorry, you lose!")
