#Problem2.py
#Project Euler problem 2

from NumberTests import isEven, fibonacciSequence

def main():
    # 4,000,000 limit
    nums = fibonacciSequence(4000000)
    total = 0
    
    for fib in nums:
        if isEven(fib):
            total = total + fib
            
    print(f"The total sum of even Fibonacci terms: {total}")

if __name__ == '__main__':
    main()
