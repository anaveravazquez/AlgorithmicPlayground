# THIS IS THE OLD CODE - NAIVE ALGORITHM
# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])

#     return max_product


def max_pairwise_product(numbers):
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


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
