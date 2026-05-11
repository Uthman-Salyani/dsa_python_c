def main():
    #indirect recursion
    def a(n):
        if n > 0:
            print(f"Inside a: {n}")
            return b(n-1)
        
    def b(n):
        if n>0:
            print(f"Inside b: {n}")
            return a(n-1)

    #head recursion 
    def head_recursion(n):
        if n<1:
            return n
        head_recursion(n-1) # no return otherwise the function will exit
        print(n)

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(fibonacci(5))

main()