import math, heapq
from Node import *
from Problem import *




# --- breadth-first
bfs_visited = 0
def breadth_first_search(problem):
    """
    BFS:
    - expand shallowest unexpanded node
    - first-in, first-out (FIFO) queue, successors at end
    """
    global bfs_visited
    node = Node(problem.initial_state)
    if problem.goal_test(node.state):
        return node  # return solution path

    queue = [node]  # FIFO queue
    explored = set()

    while queue:
        node = queue.pop(0)  # remove the first element
        explored.add(node.state)
        bfs_visited += 1    # incr counter for each visited city

        for child in node.expand(problem):
            if child.state not in explored and child not in queue:
                if problem.goal_test(child.state):
                    return child
                queue.append(child)

    return None  # no solution found



# --- depth-first
dfs_visited = 0
def depth_first_search(problem, limit):
    """
    DFS:
    - expand deepest unexpanded node
    - last-in, first-out (LIFO) queue, successors at front
    """
    global dfs_visited
    dfs_visited = 0  # reset the counter for each search
    node = Node(problem.initial_state)
    frontier = [(node, limit)]  # LIFO queue
    explored = set()

    while frontier:
        node, node_limit = frontier.pop()  # pop the last element (LIFO)
        dfs_visited += 1  # increment the counter for each visited city
        if problem.goal_test(node.state):
            return node  # solution found
        if node_limit > 0:
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored:
                    frontier.append((child, node_limit - 1))  # add child with decremented limit

    return None  # no solution found


# --- Best-First Search (Greedy Algorithm)
greedy_visited = 0
def best_first_search(problem):
    """
    Best-First / Greedy (non-recursive):
    - expands the node that appears closest to goal
    - evaluation function h(n) (heuristic) = estimate cost from n to closest goal
    """
    global greedy_visited
    greedy_visited = 0  # reset the counter for each search
    node = Node(problem.initial_state)
    node.f_value(problem)
    queue = [(node.f, node)]  # use a list as a priority queue
    explored = set()

    while queue:
        _, node = min(queue, key=lambda x: x)  # get node with lowest f-value
        queue.remove((_, node))  # remove the best node from the frontier
        greedy_visited += 1  # increment the counter for each visited city
        if problem.goal_test(node.state):
            return node  # solution found

        explored.add(node.state)
        for child in node.expand(problem):
            child.f_value(problem)
            if child.state not in explored and child not in [n for (_, n) in queue]:
                queue.append((child.f, child))  # add child to the frontier

    return None  # no solution found


### --- A* Search
a_star_visited = 0
def a_star_search(problem):
    """
    A* Search:
    - avoid expanding paths that are already expensive
    - Evaluation function f (n) = g(n) + h(n)
        - g(n) = cost so far to reach n
        - h(n) = estimated cost to goal from n
        - f(n) = estimated total cost of path through n to goal
    - uses an admissible heuristic
    """
    global a_star_visited
    node = Node(problem.initial_state)
    node.f_value(problem)  # initialize first node f-cost

    queue = [(node.f, node)]  # priority queue using heapq
    heapq.heapify(queue)
    explored = set()

    while queue:
        _, node = heapq.heappop(queue)  # get node with lowest f-cost
        a_star_visited += 1     # incr counter for visited city
        if problem.goal_test(node.state):
            return node     # return solution
        
        explored.add(node.state)
        for child in node.expand(problem):
            # set the child node's heuristic
            child.f_value(problem)
            if child.state not in explored:
                if child not in queue:
                    heapq.heappush(queue, (child.f, child))
                else:
                    # child is in queue, check if this path is better
                    for i, (_, n) in enumerate(queue):
                        if n.state == child.state and child.path_cost < n.path_cost:
                            queue[i] = (child.f, child)
                            heapq.heapify(queue)  # re-heapify after updating
                            break
    
    return None     # no solution found


if __name__=="__main__":
    initial_state = 'Neamt'
    goal_state = 'Drobeta'#'Giurgiu'  #'Craiova'
    problem = RomanianMapProblem(initial_state, goal_state)
    heuristic_value = problem.heuristic(initial_state)

    # BFS
    print("===== Breadth-First Search")
    bfs = breadth_first_search(problem)
    if bfs:
        print(f"{bfs.solution()} \ncost: {bfs.solution_distance()} \nvisited: {bfs_visited}")

    # DFS
    print("===== Depth-First Search")
    limit = 20
    dfs = depth_first_search(problem, limit)
    if dfs == 'cutoff':
        print(f"cutoff {limit}")
    elif dfs:
        print(f"{dfs.solution()} \ncost: {dfs.solution_distance()} \nvisited: {dfs_visited}")

    # Best-First (Greedy Algorithm)
    print("===== Best-First (Greedy Algorithm)")
    greedy = best_first_search(problem)
    if type(greedy) == str:
        print(greedy)
    else:
        print(f"{greedy.solution()} \ncost: {greedy.solution_distance()} \nvisited: {greedy_visited}")

    # A* Search
    print("===== A* Search")
    a_star = a_star_search(problem)
    if a_star:
        print(f"{a_star.solution()} \ncost: {a_star.solution_distance()} \nvisited: {a_star_visited}")

    # --
    print(f"Heuristic value ({initial_state}, {goal_state}): {heuristic_value}")

