import random

BATCHES = 10
ITERATIONS = 100

def monty_hall(switch=False, rand=False):
    remove = 0 
    prize = random.randint(0, 2)
    choice = random.randint(0, 2)

    while remove != choice and remove != prize:
        remove = random.randint(0, 2)

    if rand:
        switch = bool(random.randint(0, 1))

    if switch:
        if prize != choice:
            choice = prize
        else:
            return False

    return choice == prize 

def perform_batch(switch=False, rand=False):
    wins = 0

    for _ in range(ITERATIONS):
        if monty_hall(switch, rand):
            wins += 1

    return wins/ITERATIONS

if __name__ == "__main__":
    print("-- SWITCH --")
    for _ in range(BATCHES):
        print(perform_batch(switch=True))

    print("-- RANDOM --")
    for _ in range(BATCHES):
        print(perform_batch(rand=True))
    
    print("-- NO SWITCH --")
    for _ in range(BATCHES):
        print(perform_batch())
