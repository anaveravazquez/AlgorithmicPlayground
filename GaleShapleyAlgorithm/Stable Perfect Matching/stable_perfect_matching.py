
from collections import deque
import sys 


# Subtask 1: m<= 45 
# Subtask 2: G is the complete bipartite graph K_n/2, n/2 STABLE MARRIAGE PROBLEM
# Subtask 3: G is bipartite
# Subtask 4: G is the complete graph K_n (Stables Roommates Problem)
# Subtask 5: No restrictions

def is_integer(s):
    """Check if a string represents an integer."""
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def assign_numeric_identifiers(lines):
    # Create a mapping from each unique item to a unique number
    item_to_num = {}
    current_id = 1

    # First pass to assign IDs to the main entities (left side of the preferences)
    for line in lines[1:]:
        main_entity = line.split()[0]
        if main_entity not in item_to_num:
            item_to_num[main_entity] = current_id
            current_id += 1

    # Second pass for preferences (excluding main entities)
    for line in lines[1:]:
        parts = line.split()[1:]
        for item in parts:
            if item not in item_to_num:
                item_to_num[item] = current_id
                current_id += 1

    # Debug prints:
    print("Item to Number Mapping:")
    for k, v in item_to_num.items():
        print(f"{k} -> {v}")

    # Convert input lines to use these numeric identifiers
    converted_lines = [lines[0]]  # First line remains unchanged
    for line in lines[1:]:
        parts = line.split()
        converted_line = str(item_to_num[parts[0]]) + " " + " ".join(map(str, [item_to_num[item] for item in parts[1:]]))
        converted_lines.append(converted_line)

    return converted_lines, item_to_num




def is_valid_match(a, b, preferences):
    # Check if b is in a's preferences and a is in b's preferences
    return b in preferences[a-1] and a in preferences[b-1]

def generate_permutations(nodes, preferences, current_matching=[]):
    if not nodes:
        # Base case: if no more nodes to match, return the current matching
        return [current_matching]

    current_node = nodes[0]
    possible_matches = [node for node in nodes if node != current_node]

    matchings = []

    for match in possible_matches:
        # If the match is not already in current matching and is valid
        if ((current_node, match) not in current_matching and
           (match, current_node) not in current_matching and
           is_valid_match(current_node, match, preferences)):
            next_nodes = [node for node in nodes if node != current_node and node != match]
            matchings.extend(generate_permutations(next_nodes, preferences, current_matching + [(current_node, match)]))

    return matchings




def ranking(preferences):
    #create a nxn matrx filled with -1
    ranking = [[-1 for _ in range(n)] for _ in range(n)]
    for i, pref in enumerate(preferences):
        for rank, node in enumerate(pref):
            ranking[i][node-1] = rank +1
    return ranking 

def is_matching_stable(matching, ranking, preferences):
    n = len(ranking)
    if len(matching) != n // 2:  # Incomplete matching
        return False

    for (a, b) in matching:
        for c in preferences[a - 1]:
            if c == b:  # No one else preferred
                break
            partner_c = get_current_partner(c, matching)
            if ranking[c - 1][a - 1] < ranking[c - 1][partner_c - 1]:
                return False
        for d in preferences[b - 1]:
            if d == a:  # No one else preferred
                break
            partner_d = get_current_partner(d, matching)
            if ranking[d - 1][b - 1] < ranking[d - 1][partner_d - 1]:
                return False

    return True



def get_current_partner(node, matching):
    for (a,b) in matching:
        if a == node:
            return b
        if b == node:
            return a
    return None

def is_barpartite(preferences):
    color = [0] * n # give evertything color white
    for i in range(n):
        # If the node is uncolored and couldn't be colored, the graph isn't bipartite
        if color[i] == 0 and not bfs(i, preferences, color):
            return False
    return True
    

def bfs(node, preferences, color):
    queue = deque([node])
    color[node] = 1
    
    while queue: 
        curr_node = queue.popleft()
        for neighbor in preferences[curr_node]:
            # Neighbor has the same color, graph is not bipartite
            if color[neighbor-1] == color[curr_node]:
                return False
            # If the neighbor hasn't been colored, color it with opposite color
            if color[neighbor-1] == 0:
                color[neighbor-1] = 3 - color[curr_node]
                queue.append(neighbor - 1)
    return True




def stable_perfect_matching(n, m, preferences):

    print('Original Input')
    print(n, m)
    for preference in preferences:
        print(str(preferences.index(preference) + 1) + ' ' + str(preference))

    
    # We will do a exhausive search if m<=45
    if m <= 45:
        nodes = list(range(1, n + 1))
        all_matchings = generate_permutations(nodes, preferences)
        print('All possible matchings are:', all_matchings)
        ranking_matrix = ranking(preferences)
        for matching in all_matchings:
            if is_matching_stable(matching, ranking_matrix, preferences):
                for (a, b) in matching:
                    print(a, b)
                break
        else: 
            print('-')
    
    #stable marriage problem
    elif is_barpartite(preferences) == True:
    
        














    else:
        print('NOT bipartite')
        



            
def stable_perfect_matching_with_names(n, m, preferences, num_to_item):

    print('Original Input')
    print(n, m)
    for preference in preferences:
        print(str(preferences.index(preference) + 1) + ' ' + str(preference))

    # We will do a exhausive search if m<=45
    if m <= 45:
        nodes = list(range(1, n + 1))
        all_matchings = generate_permutations(nodes, preferences)
        print('All possible matchings are:', all_matchings)
        ranking_matrix = ranking(preferences)
        for matching in all_matchings:
            if is_matching_stable(matching, ranking_matrix, preferences):
                for (a, b) in matching:
                    print(f"{num_to_item[a]} {num_to_item[b]}")

                break
        else: 
            print('-')  

        



    
    





    

        










if __name__ == '__main__':
    lines = [line.strip() for line in sys.stdin if line.strip()]
    
    # Check if the first preference item is an integer or a string
    first_item = lines[1].split()[1]
    
    # If it's a string, use assign_numeric_identifiers to convert
    if not is_integer(first_item):
        lines, item_to_num = assign_numeric_identifiers(lines)
        num_to_item = {v: k for k, v in item_to_num.items()}  # Inverse mapping
        
    n, m = map(int, lines[0].split())
    preferences = [list(map(int, line.split()[1:])) for line in lines[1:]]
    
    # If using name identifiers, use the num_to_item mapping for printing
    if 'num_to_item' in locals():
        stable_perfect_matching_with_names(n, m, preferences, num_to_item)  # Create this function
    else:
        stable_perfect_matching(n, m, preferences)

    
