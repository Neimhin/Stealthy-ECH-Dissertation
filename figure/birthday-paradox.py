#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Setting up parameters
digest_length = 8  # 8-bit digest
total_possibilities = 2**digest_length  # 256 possibilities

# Function to calculate 1 - P(n)
def no_collision_probability(n, total_possibilities):
    prob = 1.0
    for i in range(n):
        prob *= (total_possibilities - i) / total_possibilities
    return prob

def no_preimage_probability(n, total_possibilities):
    prob = 1.0
    return ((total_possibilities-1)/total_possibilities)**n


# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Generate data for plotting
n_values = np.arange(1, total_possibilities + 1)
P_values = [1 - no_collision_probability(n, total_possibilities) for n in n_values]
plt.plot(n_values, P_values, marker='.',  linestyle='-', label='collision')

# Generate data for plotting
n_values = np.arange(1, total_possibilities + 1)
P_values = [1-no_preimage_probability(n, total_possibilities) for n in n_values]

plt.plot(n_values, P_values, marker='.', linestyle='-', label='preimage')
plt.title('Probability of Collision/Premige $P(n)$ vs. Number of Samples $n$ for 8-bit Digest')
plt.xlabel('Number of Samples $n$')
plt.ylabel('Probability of Collision/Preimage $P(n)$')
plt.legend()
plt.axhline(1-no_collision_probability(20, 256), color='orange')
plt.axvline(1.253*(2**4), color='orange')
print(1-no_collision_probability(20, 256))
plt.grid(True)
plt.savefig(sys.argv[1])
