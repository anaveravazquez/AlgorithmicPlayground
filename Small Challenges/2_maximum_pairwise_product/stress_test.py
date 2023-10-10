import random 
import sys

def MaxPairwiseProductNaive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n): 
            max_product = max(max_product, numbers[first] * numbers[second]) 
    return max_product


def MaxPairwiseProductFast(numbers):
    n=len(numbers)
    #first scan to fing the largest number 
    
    idx = 0
    for i in range(1,n):
        if numbers[i]>numbers[idx]:
            idx=i
    
    #scan a second time for the largest among the remaining
    if idx == 0:
        idx2 = 1
        for i in range(0,n):
            if numbers[i]>=numbers[idx2] and i!= idx:
                idx2 = i
    else:
        idx2 = 0
        for i in range(1,n):
            if numbers[i]>=numbers[idx2] and i!= idx:
                idx2 = i
    
    return numbers[idx]*numbers[idx2]


def stressTest(N,M):
    while True:
        n = random.randint(2,N)
        A = [random.randint(0, M) for _ in range(n)]
        print(A)
        result1 = MaxPairwiseProductNaive(A)
        result2 = MaxPairwiseProductFast(A)

        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer:", result1, result2)
            return


if __name__ == "__main__":
    # Ensure there's at least one argument provided (n value)
    if len(sys.argv) < 3:
        print("Please provide N and M as a command line argument.")
        sys.exit(1)
    
    # Convert the first command line argument to integer (after script name)
    N = int(sys.argv[1])
    M =int(sys.argv[2])
    stressTest(N,M)