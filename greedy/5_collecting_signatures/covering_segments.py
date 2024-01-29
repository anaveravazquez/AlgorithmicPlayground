from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #1. sort segments by end position
    segments.sort(key = lambda s: s.end)
    #2. iterate though segments
    current_point = None
    for segment in segments: 
        # Step 3: Add the end point if the segment is not covered
        if current_point is None or segment.start > current_point:
            current_point = segment.end
            points.append(current_point)
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
