import random

def main(): 
    #linear search
    def linear_search(values, target):
        for item in range(len(values)):
            if values[item] == target:
                return item # returns the index
            
        return -1
    
    def get_values():
        values = random.sample(range(10,20), 5)
        print(f"The list is: {values}")
        target = int(input("Enter values to search: "))
        result = linear_search(values, target)
        if result != 0:
            print(f"The values at index {result} is {values[result]}")
        else:
            print("None found")
    
    #binary search
    # 1. Recursive
    def binary_recursion(values, target, low, high):
        if low > high:
            return -1
        mid = (low+high) // 2
        print(f"{low} {mid} {high}")
        if values[mid] == target:
            return mid
        elif values[mid] > target:
            return binary_recursion(values, target, low, mid-1)
        else:
            return binary_recursion(values, target, high, mid+1)
    
    def get_values1():
        values = sorted(random.sample(range(10,20), 5))
        print(f"The list is: {values}")
        target = int(input("Enter values to search: "))
        result = binary_recursion(values, target, 0, len(values))
        if result != -1:
            print(f"The values at index {result} is {values[result]}")
        else:
            print("None found")
    
    get_values1()
    


main()