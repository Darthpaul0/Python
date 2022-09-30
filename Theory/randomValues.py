import random

for i in range(3):
    print(random.randint(10, 25))

members = ['Paco', 'Antonio', 'Pepe', 'Marcos']
leader = random.choice(members)
print(leader)
