import random
import sys


def randomize_input(n):
    # Validate if the input is within the range
    if not (2 <= n <= 2*(10**5)):
        print("n should be between 2 and 2*10^5")
    
    # Generate n random integers between 0 and 2*10^5
    numbers = [random.randint(0, 2*10**5) for _ in range(n)]
    
    # Print n
    print(n)
    # Print the n numbers
    print(" ".join(map(str, numbers)))

if __name__ == "__main__":
    # Ensure there's at least one argument provided (n value)
    if len(sys.argv) < 2:
        print("Please provide n as a command line argument.")
        sys.exit(1)
    
    # Convert the first command line argument to integer (after script name)
    n = int(sys.argv[1])
    randomize_input(n)