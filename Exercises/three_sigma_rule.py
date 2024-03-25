import numpy as np

sample = np.random.normal(loc=0, scale=1, size=100000)


mu = np.mean(sample)
sigma = np.std(sample)


within_1_sigma = np.mean((sample >= mu - sigma) & (sample <= mu + sigma))
within_2_sigma = np.mean((sample >= mu - 2 * sigma) & (sample <= mu + 2 * sigma))
within_3_sigma = np.mean((sample >= mu - 3 * sigma) & (sample <= mu + 3 * sigma))

within_1_sigma_percent = within_1_sigma * 100
within_2_sigma_percent = within_2_sigma * 100
within_3_sigma_percent = within_3_sigma * 100

print(within_1_sigma_percent, within_2_sigma_percent, within_3_sigma_percent)
