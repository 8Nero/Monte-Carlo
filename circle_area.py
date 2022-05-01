import random, math

def simulate(trials):
    in_circle = 0.0
    in_box = 1.0 * trials
    for _ in range(trials):
        x, y = random.random(), random.random()

        n_1 = math.pow((x-0.5), 2)
        n_2 = math.pow((y-0.5), 2)

        if (n_1+n_2 <= 0.25):
            in_circle += 1
    pi = in_circle/in_box
    return pi


for i in range(1):
    print(4*simulate(10000000))

