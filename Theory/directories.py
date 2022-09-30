from pathlib import Path

# Absolute path
path = Path("new")
# path.mkdir()  # creates a new directory
# path.rmdir()  # removes a directory
# path.glob('*.py')  # locates a directory
for file in path.glob('*.py'):
    print(file)
# print(path.exists())

# Relative path
