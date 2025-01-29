

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

    def heuristic(self, state):
        """ calculates the heuristic value for the given state (estimated distance to the goal) """
        if self.goal_state == 'Bucharest':
            return self.sld_to_bucharest[state]
        else:
            # SLD(A, C) <= SLD(A, B) + SLD(B, C)
            # Heuristic 1: triangle inequality with Bucharest as the third point
            return self.sld_to_bucharest[state] + self.sld_to_bucharest[self.goal_state]
        


