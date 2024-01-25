from sys import stdin


def min_refills(distance, tank, stops):
    """
    input: distance from city to city d, miles you can do in a full tank m, and stop_1<...<stop_n gas stations
    output: minimum number of refills to get from one city to another if a car can travel
            at most m miles on a full talk. Distance btw cities is d miles and there are 
            gas stations at distances stop_1, ..., stop_n. The car starts with a full tank. 
    """

    refills = 0
    current_stop = 0
    stops = [0] + stops + [distance]  # Append start point and destination to stops list

    while current_stop < len(stops) - 1:
        last_stop = current_stop
        # Move to the furthest reachable stop within the tank's capacity
        while current_stop < len(stops) - 1 and stops[current_stop + 1] - stops[last_stop] <= tank:
            current_stop += 1

        # If we haven't moved, it means we can't reach the next stop
        if current_stop == last_stop:
            return -1

        # If we haven't reached the destination yet, we need a refill
        if current_stop < len(stops) - 1:
            refills += 1

    return refills


    
if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
