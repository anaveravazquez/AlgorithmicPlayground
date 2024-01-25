from sys import stdin

def bestItem(weights, values, n):
    maxValuePerWeight = 0 
    bestItemIndex = 0
    for i in range(n):
        if weights[i] > 0:
            if values[i]/weights[i] > maxValuePerWeight:
                maxValuePerWeight = values[i]/weights[i]
                bestItemIndex = i
    return bestItemIndex


def optimal_value(capacity, weights, values, n):

    """
    Input: The capacity of a backpack W as well as the weights (w1,...,wn) and costs (c1,...,cn) of n different compounds.
    Output: The maximum total value of fractions of items that fit into the backpack of the given capacity
    """
    total_value = 0 

    for _ in range(n):
        if capacity == 0: 
            return total_value
        i = bestItem(weights, values, n)
        a = min(weights[i], capacity)
        total_value = total_value + a*(values[i]/weights[i])
        weights[i] = weights[i] - a
        capacity = capacity - a


    return total_value
        
        
    
   


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values, n)
    print("{:.10f}".format(opt_value))
