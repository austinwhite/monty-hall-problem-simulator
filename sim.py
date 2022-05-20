import random
import numpy as np
import matplotlib.pyplot as plt

BATCHES = 1000
ITERATIONS = 2500 
POINT_SIZE = 3

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


def simulate(switch=False, rand=False):
    win_loss_ratio = []

    for _ in range(BATCHES):
        win_loss_ratio.append(perform_batch(switch, rand))

    return win_loss_ratio


def generate_np_array(forced_value=None):
    arr = []
    
    if forced_value:
        arr = [forced_value for _ in range(BATCHES)]
    else:
        arr = [i for i in range(BATCHES)]
    
    return np.array(arr)


def construct_visualization(switch, rand, no_switch):
    x_values = generate_np_array()

    plt.title("The Monty Hall Problem")
    plt.ylim([0.2, 0.8])
    plt.xlabel("Iteration")
    plt.ylabel("Win Rate")

    x = np.array(x_values)
    y = np.array(switch)
    plt.scatter(x, y, POINT_SIZE, label="Switch")
    plt.plot(x, generate_np_array(0.33), color="black")

    x = np.array(x_values)
    y = np.array(rand)
    plt.scatter(x, y, POINT_SIZE, label="Random")
    plt.plot(x, generate_np_array(0.5), color="black")

    x = np.array(x_values)
    y = np.array(no_switch)
    plt.scatter(x, y, POINT_SIZE, label="No swtich")
    plt.plot(x, generate_np_array(0.66), color="black", label="Theoretical")

    plt.legend(loc="upper right")

    plt.show()


if __name__ == "__main__":
    print("Performing Simulation: Switch Choice")
    switch = simulate(switch=True)
    print("Performing Simulation: Random Choice")
    rand = simulate(rand=True)
    print("Performing Simulation: Keep Choice")
    no_switch = simulate()

    print("Constructing Visualiztion.")
    construct_visualization(switch, rand, no_switch)
