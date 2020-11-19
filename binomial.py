# This program and its computation instruction was written by Andre Christoga Pramaditya (drepram.com) with the student ID (2006570006).
# Program dan instruksi komputasi ini ditulis oleh Andre Christoga Pramaditya (drepram.com) dengan Nomor Pokok Mahasiswa (2006570006).

import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore") # insert programmer laziness joke here

# number of trials, probability of each trial
number_of_trials = 100
probability_5 = 0.5
probability_1 = 0.1
probability_9 = 0.9

sample_5 = np.random.binomial(number_of_trials, probability_5, 10000)
sample_1 = np.random.binomial(number_of_trials, probability_1, 10000)
sample_9 = np.random.binomial(number_of_trials, probability_9, 10000)

# disclaimer_text = "Orange bars (n=0.1), Blue bars (n=0.5), Green bars (n=0.9)."

combined_histogram = plt.figure(1, figsize=(7,7))

plt.hist(sample_5, 15, density=True)
plt.hist(sample_1, 15, density=True)
plt.hist(sample_9, 15, density=True)

combined_histogram.suptitle('Binomial Distribution Combined Histogram', fontsize=14, fontweight='bold')
combined_axes_title = combined_histogram.add_subplot(111)
combined_histogram.subplots_adjust(top=0.85)
combined_axes_title.set_title('Orange bars (n=0.1), Blue bars (n=0.5), Green bars (n=0.9)')
combined_histogram.show()

histogram_each, (case1, case2, case3) = plt.subplots(1,3, figsize=(15,9))
histogram_each.suptitle('Binomial Distribution for Each Case \n(with more specific range for the x axis)', fontweight='bold')
case1.hist(sample_1, 15, density=True, color="orange")
case1.set_title('retrieved 10.000 random number\nfrom n=100,p=0.1')
case2.hist(sample_5, 15, density=True, color="blue")
case2.set_title('retrieved 10.000 random number\nfrom n=100,p=0.5')
case3.hist(sample_9, 15, density=True, color="green")
case3.set_title('retrieved 10.000 random number\nfrom n=100,p=0.9')

# Standardization of the y axis if of any need, it is unnecessary for now
# case1.set_ylim([0, 0.2])
# case2.set_ylim([0, 0.2])
# case3.set_ylim([0, 0.2])

histogram_each.show()

### OLD METHOD OF SHOWING EACH FIGURES
# histogram_5 = plt.figure(2)
# plt.hist(sample_5, 15, density=True, color="blue")
# histogram_5.show()

# histogram_1 = plt.figure(3)
# plt.hist(sample_1, 15, density=True, color="orange")
# histogram_1.show()

# histogram_9 = plt.figure(4)
# plt.hist(sample_9, 15, density=True, color="green")
# histogram_9.show()

plt.show()