#Project Euler Problem 1

import NumberTests

def main():
    total = 0
    # Use 1000 to get multiples *below* 1000
    for i in range(1000):
        if NumberTests.isThreeOrFive(i):
            total += i
    
    print(f"The sum of multiples of 3 or 5 below 1000 is: {total}")

if __name__ == '__main__':
    main()
