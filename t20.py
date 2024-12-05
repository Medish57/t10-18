import matplotlib.pyplot as plt
import random


n_points = 100000


x, y = [0], [0]


coefficients = [
    (0, 0, 0, 0.16, 0, 0),     
    (0.85, 0.04, -0.04, 0.85, 0, 1.6),  
    (0.2, -0.26, 0.23, 0.22, 0, 1.6),   
    (-0.15, 0.28, 0.26, 0.24, 0, 0.44)  
]


probabilities = [0.01, 0.85, 0.07, 0.07]


def choose_function():
    r = random.random()
    cumulative_probability = 0
    for i, p in enumerate(probabilities):
        cumulative_probability += p
        if r <= cumulative_probability:
            return coefficients[i]


for _ in range(n_points):
    a, b, c, d, e, f = choose_function()
    x_new = a * x[-1] + b * y[-1] + e
    y_new = c * x[-1] + d * y[-1] + f
    x.append(x_new)
    y.append(y_new)


plt.figure(figsize=(6, 10))
plt.scatter(x, y, s=0.1, color='green')
plt.title("Barnsley Fern")
plt.axis("off")
plt.show()