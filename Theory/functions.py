# Create a function using reserved word def
# It's a good practice leave 2 lines after a function
def greeting(name, age):
    print(f'Greetings, {name} {age}!')


print("*****")
# Keyword arguments help to clarify the code when needed
greeting(name="Python", age=22)
print("*****")


def square(number):
    print(number*number)


print(square(3))
