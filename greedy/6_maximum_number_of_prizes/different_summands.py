def optimal_summands(n):
    summands = []
    summand = 1
    current_sum = 0
    while True:
        if current_sum + summand > n: 
           break
        summands.append(summand)
        current_sum+= summand
        summand += 1
    
    if current_sum != n:
        difference = n-current_sum
        if difference not in summands:
            summands.append(difference)
        else: 
            summands[-1] = summands[-1] + difference
    
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
