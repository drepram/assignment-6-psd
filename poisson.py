# This program and its computation instruction was written by Andre Christoga Pramaditya (drepram.com) with the student ID (2006570006).
# Program dan instruksi komputasi ini ditulis oleh Andre Christoga Pramaditya (drepram.com) dengan Nomor Pokok Mahasiswa (2006570006).

import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore") # insert programmer laziness joke here

sample_size = 10000

lambda_two = np.random.poisson(2, sample_size)
lambda_twenty = np.random.poisson(20, sample_size)
lambda_two_hundred = np.random.poisson(200, sample_size)

combined_histogram = plt.figure(1, figsize=(7,7))

plt.hist(lambda_two, 15, density=True)
plt.hist(lambda_twenty, 15, density=True)
plt.hist(lambda_two_hundred, 15, density=True)

combined_histogram.suptitle('Poisson Distribution Combined Histogram', fontsize=14, fontweight='bold')
combined_axes_title = combined_histogram.add_subplot(111)
combined_histogram.subplots_adjust(top=0.85)
combined_axes_title.set_title('Blue bars (λ = 2), Orange bars (λ = 20), Green bars (λ = 20)')
combined_histogram.show()

histogram_each, (case1, case2, case3) = plt.subplots(1,3, figsize=(15,9))
histogram_each.suptitle('Poisson Distribution for Each Case \n(with more specific range for the x axis)', fontweight='bold')
case1.hist(lambda_two, 15, density=True, color="blue")
case1.set_title('λ = 2, sample size = 10.000')
case2.hist(lambda_twenty, 15, density=True, color="orange")
case2.set_title('λ = 20, sample size = 10.000')
case3.hist(lambda_two_hundred, 15, density=True, color="green")
case3.set_title('λ = 200, sample size = 10.000')
histogram_each.show()

plt.show()