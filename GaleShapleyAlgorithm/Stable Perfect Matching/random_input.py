import random
import sys

def randomize_input(max_m_45 = False, complete_graph_forced = False, bipartite_graph_forced = False, complete_graph_with_full_preferences=False):

    n = random.randrange(2, 200, 2)

    if complete_graph_forced == True and bipartite_graph_forced == False: 
        m=int((n*(n-1)//2))
        if max_m_45 and m>45: 
            n = random.randrange(2, 10, 2)
            m=int((n*(n-1)//2))

    elif complete_graph_forced == True and bipartite_graph_forced == True:
        m = int((n/2)**2)
        if max_m_45 and m>45:
            n = random.randrange(2,13,2)
            m = int((n/2)**2)
    elif complete_graph_forced == False and bipartite_graph_forced == True:
        m = random.randint(n/2, (n/2)**2)
        if max_m_45 and m>45:
            n = random.randrange(2, 13, 2)
            m = random.randint(n/2 , (n/2)**2)
    else:
        m = random.randint(n/2 , n*(n-1)//2)
        if max_m_45 and m>45:
            n = random.randrange(2, 10, 2)
            m = random.randint(n/2 , n*(n-1)//2)

    preferences = {i: [] for i in range(1, n + 1)}
    added_edges = set()

    if complete_graph_with_full_preferences:
        added_edges = set()
        if n == 2:
            preferences = {1: [2], 2: [1]}
        else:
            preferences = {i: [j for j in range(1, n + 1) if j != i] for i in range(1, n + 1)}
    
    else:
        if bipartite_graph_forced:
            if complete_graph_forced:
                for i in range(1, n//2 + 1):
                    possible_neighbors = [j for j in range(n//2 + 1, n+1)]
                    random.shuffle(possible_neighbors)
                    preferences[i] = possible_neighbors
                
                for j in range(n//2+1, n+1):
                    possible_neighbors = [i for i in range(1, n//2 + 1)]
                    random.shuffle(possible_neighbors)
                    preferences[j].extend(possible_neighbors)
                

            else:
                # Split nodes into two sets
                A = [i for i in range(1, n//2 + 1)]
                B = [i for i in range(n//2 + 1, n + 1)]

                for node in A:
                    neighbor = random.choice(B)
                    added_edges.add((node, neighbor))
                    B.remove(neighbor)
                B = [i for i in range(n//2 + 1, n + 1)]  # Reset B
                # Add edges until we have m edges
                while len(added_edges) < m:
                    u = random.choice(A)
                    v = random.choice(B)
                    if (u, v) not in added_edges:
                        added_edges.add((u, v))
                    
                for u, v in added_edges:
                    preferences[u].append(v)
                    preferences[v].append(u)

        else:
            #first, let's make sure there are no isolated edges (assumption from problem statement)
            for i in range(1, n+1):
                possible_neighbors = [j for j in range(1,n+1) if j!= i and (i,j) not in added_edges and (j,i) not in added_edges]
                if len(possible_neighbors) == 0: 
                    break
                neighbor = random.choice(possible_neighbors)
                preferences[i].append(neighbor)
                added_edges.add((i, neighbor))

            #now that we have all the keys with at least one link in preference list
            while len(added_edges) < m:
                i = random.randint(1, n)
                possible_neighbors = [j for j in range(1,n+1) if j!=i and (i,j) not in added_edges and (j,i) not in added_edges]
                if len(possible_neighbors) == 0: 
                    continue
                neighbor = random.choice(possible_neighbors)
                preferences[i].append(neighbor)
                added_edges.add((i, neighbor))

    print(n, m)
    for key, value in preferences.items():
        print(key, ' '.join(map(str, value)))

if __name__ == "__main__":
    randomize_input(max_m_45=False, complete_graph_forced=True, bipartite_graph_forced=True, complete_graph_with_full_preferences=False)
