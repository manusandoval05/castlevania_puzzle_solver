from itertools import combinations_with_replacement

positions = {
    "inner": 4, 
    "medium": 4,
    "outer": 4
}

def fix_cycle(positions): 
    for key in positions: 
        if positions[key] == 5: 
            positions[key] = 1
        elif positions[key] == 0: 
            positions[key] = 4

    return positions

def move_inner(positions, clockwise=True):
    positions["inner"] += 1 if clockwise else -1
    positions["medium"] += -1 if clockwise else 1
    
    positions = fix_cycle(positions)
    return positions

        

def move_medium(positions, clockwise=True): 
    positions["medium"] += 1 if clockwise else -1
    positions["outer"] += -1 if clockwise else 1
    positions["inner"] += -1 if clockwise else 1
    
    positions = fix_cycle(positions)    
    return positions

def move_outer(positions, clockwise=True):
    positions["outer"] += 1 if clockwise else -1
    positions["medium"] += -1 if clockwise else 1
    
    positions = fix_cycle(positions)
    return positions

MOVEMENT_PATTERNS = {
    "inner": move_inner, 
    "medium": move_medium, 
    "outer": move_outer
}

def valid_movement_patterns():
    movements = []
    # True or False means clockwise or counter clockwise
    combinations_list = [("inner", True), ("inner", False), ("medium", True), ("medium", False), ("outer", True), ("outer", False)]
    for i in range(6):
        movements += list(combinations_with_replacement(combinations_list, i))
    
    return movements

def most_effective_solution(start_position, movement_patterns):
    solutions = []
    for pattern in movement_patterns: 
        current_position = start_position.copy()
        for movement, clockwise in pattern:
            current_position = MOVEMENT_PATTERNS[movement](current_position, clockwise)
        if current_position["outer"] == 1 and current_position["inner"] == 1 and current_position["medium"] == 1: 
            solutions.append(pattern)
    
    return solutions
    

print(most_effective_solution(positions, valid_movement_patterns()))