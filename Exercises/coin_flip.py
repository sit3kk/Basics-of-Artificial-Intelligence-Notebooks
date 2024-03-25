import numpy as np

random_ints = np.random.randint(0, 2, size=(100000, 3))


sums = np.sum(random_ints, axis=1)

count = np.sum(sums >= 2)


print(count)
