import random
import numpy as np

from vacuum import *

"""Reflex Agent"""

def reflex_agent(percept):
    """Clean and Go as Far North as You Possibly Can"""
    if percept:
        return "clean"
    else:
        return "north"


"""Random Agent"""

def random_agent(percept):
    """Clean, and go in a random direction. Then clear there as well"""
    if percept:
        return 'clean'
    else:
        directions = ['north', 'east', 'south', 'west']
    return random.choice(directions)



"""State Agent"""

clean_count = 0
direction = 0
run_length = 0


def state_agent_reset():
    global clean_count
    global direction
    global run_length
    clean_count = 0
    direction = 0
    run_length = 0


def state_agent(in_dirty_square):
    '''
    Similar to the random agent, but if it hasn't seen any dirt in a while
    it picks a random direction and sprints.
    '''
    global clean_count
    global direction
    global run_length
    directions = list(OFFSETS.keys())
    if in_dirty_square:  # Happily cleaning
        clean_count = 0
        return 'clean'
    elif run_length > 0:  # In the process of sprinting
        run_length -= 1
        return directions[direction]
    else:
        clean_count += 1
        if clean_count >= 10:  # In a desert of cleanliness
            run_length = random.randrange(10)
        direction = random.choice([(direction + 1) % 4, (direction + 3) % 4])
        return directions[direction]


# run(20, 50000, random_agent)
# run(20, 50000, state_agent, state_agent_reset)

# print(many_runs(20, 50000, 10, reflex_agent))
# print(many_runs(20, 50000, 10, random_agent))
# print(many_runs(20, 50000, 10, state_agent, state_agent_reset))


# def static_agent(percept):
#     directions = ['north', 'east', 'south', 'west']
#     current_dir = random.choice(directions) # Choose a random direction to start
#
#     count_times = 0  # Counts how many times you checked the same block for cleanliness
#     if percept: # if dirty --> clean
#         count_times += 1 # been there once
#         return 'clean' # cleaning action
#     else:
#         count_times += 1
#         if count_times > 1:
#             directions.remove(current_dir)  # Remove Direction from the list
#             return random.choice(directions)
#
#         count = 0
#         directions.append(current_dir)
#         return current_dir

#
# def state_agent(percept):
#     directions = ['north', 'east', 'south', 'west']
#     current_dir = random.choice(directions)  # Picking the starting direction

    # counts = {} # for counting the number of visits to a direction.
    # for direction in directions:
    #     """Initialize the directions counts to 0"""
    #     counts[direction] = 0 # populating our counts hashmap, with the directions as keys, and 0 as the value
    #                           # values represent the number of visits to each direction, for now 0, because nothing was visited
    #
    # if percept:  # if percept is true then block is dirty. Therefore --> clean
    #     counts[current_dir] += 1   # Now that the cleaner has been here, we increment the number of visits to the destination
    #     return 'clean'
    # else:
    #     counts[current_dir] += 1
    #     total_visits = sum(counts.values())
    #     probs = [counts[d]/total_visits for d in directions] # list comprehension to find probabilities of going in a certain direction
    #     probs = [p/sum(probs) for p in probs] # normalize the probabilities so they add up to 1
    #     current_dir = np.random.choice(directions, p=probs) # choose a direction based on the probabilities
    #     return current_dir


# run(20,50000,state_agent)
print(many_runs(20, 50000, 10, random_agent),"RA")
# # # print(many_runs(20, 50000, 10, reflex_agent)) # 18610028.2
print(many_runs(20, 50000, 10, state_agent,state_agent_reset),"SA")


# Tested them

#Loss 2 , Win 2
#Loss 2 , Win 1