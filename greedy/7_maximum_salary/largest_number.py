from functools import cmp_to_key

def compare(a,b):
    order1 = a + b
    order2 = b + a
    if order1 < order2:
        return 1
    if order1 > order2:
        return -1
    else: 
        return 0
    
def largest_number_naive(numbers):  
   #covert all numbers to strings
    str_numbers = [str(number) for number in numbers]
    str_numbers.sort(key = cmp_to_key(compare))
    
    largest_number = ''.join(str_numbers)

    # Edge case: remove leading zeros (in case all numbers are zeros)
    largest_number = largest_number.lstrip('0')
    
    # Return '0' if the result is empty, meaning all inputs were zeros; otherwise, return the result
    return largest_number if largest_number != '' else '0'

        
if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
