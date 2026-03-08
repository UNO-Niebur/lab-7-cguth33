# NumberTests.py

def isThreeOrFive(n):
    
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False

def isPrime(p):
    
    if p < 2:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True

def isEven(n):
    
    if n % 2 == 0:
        return True
    else:
        return False

def addNum(numList, num):
    """Adds the given number to the given list. Does not add duplicate values."""
    if num not in numList:
        numList.append(num)

def fibonacciSequence(value):
    """Returns a list of numbers in the fibonacci sequence up to the given value"""
    nums = [1, 2]
    size = 2
    n = nums[size - 1] + nums[size - 2]

    while n < value:
        addNum(nums, n)
        size = len(nums)
        n = nums[size - 1] + nums[size - 2]
    
    return nums

def main():
    # Test your new functions in this main
    num = int(input("Enter a number: "))

    if isPrime(num):
        print("%d is a prime number" % (num))
    
    if isEven(num):
        print("%d is an even number" % (num))

if __name__ == '__main__':
    main()