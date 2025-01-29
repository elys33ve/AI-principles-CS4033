

"""
RomanianMapProblem Class

map: dictionary representing cities as keys and neighboring cities with travel costs as values.
sld_to_bucharest: dict storing the straight-line distance (SLD) to Bucharest for each city

actions(state): Returns a list of neighboring cities for a given state.
result(state, action): Returns the resulting city after taking an action.
goal_test(state): Checks if the current city is the goal.
step_cost(state, action): Returns the distance cost between cities.
heuristic(state, heuristic_type=1): Computes heuristics using:
    Type 1: Triangle inequality using Bucharest as an intermediary.
    Type 2: Minimum edge cost from the current state and goal state.
"""


class RomanianMapProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

        self.map = {
            'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
            'Zerind': {'Arad': 75, 'Oradea': 71},
            'Oradea': {'Zerind': 71, 'Sibiu': 151},
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
            'Timisoara': {'Arad': 118, 'Lugoj': 111},
            'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
            'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
            'Drobeta': {'Mehadia': 75, 'Craiova': 120},
            'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
            'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
            'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
            'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
            'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
            'Giurgiu': {'Bucharest': 90},
            'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
            'Hirsova': {'Urziceni': 98, 'Eforie': 86},
            'Eforie': {'Hirsova': 86},
            'Vaslui': {'Urziceni': 142, 'Iasi': 92},
            'Iasi': {'Vaslui': 92, 'Neamt': 87},
            'Neamt': {'Iasi': 87}
        }

        # straight-line distances (SLD) to Bucharest. h_SLD
        self.sld_to_bucharest = {
            'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
            'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
            'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
            'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
        }

    def actions(self, state):
        """ returns the neighboring cities from the given city """
        return list(self.map.get(state, {}).keys())

    def result(self, state, action):
        """ returns the destination city when traveling from the current city """
        return action

    def goal_test(self, state):
        """ checks if the given city is the goal city """
        return state == self.goal_state

    def step_cost(self, state, action, next_state):
        """ returns the distance between current city and next city """
        return self.map.get(state, {}).get(next_state, 0)

    def heuristic(self, state, goal=None):
        """ calculates the heuristic value for the given state (estimated distance to the goal) """
        if goal == None:
            goal = self.goal_state

        # if goal is Bucharest, use predefined SLD values
        if goal == "Bucharest":
            return self.sld_to_bucharest.get(state, float('inf'))

        # if goal is not Bucharest, estimate the SLD
        if state in self.sld_to_bucharest and goal in self.sld_to_bucharest:
            # approach 1: use Bucharest as an intermediate reference
            h1 = abs(self.sld_to_bucharest[state] - self.sld_to_bucharest[goal])

            # approach 2: use a reference city (e.g., Sibiu, Pitesti)
            reference_city = "Sibiu"  # (or another well-connected city)
            if reference_city in self.sld_to_bucharest:
                h2 = self.sld_to_bucharest[state] + self.sld_to_bucharest[goal] - 2 * self.sld_to_bucharest[reference_city]
            else:
                h2 = float('inf')

            # return best heuristic estimation
            return max(0, min(h1, h2))

        return float('inf')  # no valid heuristic found
        


