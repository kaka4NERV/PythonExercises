numbers = []

def createList(a, b):
    i = 0
    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + b
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

createList(8, 2)

print("The numbers: ")

for num in numbers:
    print(num)
