import random

def max_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num<minimum:
            # print(f"Current Min: {minimum}")
            minimum = num
    return minimum


def getValues():
    list = random.sample(range(50,100), 10)
    list_a = list[2:]
    print(list_a)
    # print(list)
    # max_min(list)

def main():
    getValues()

main()


