import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore") # insert programmer laziness joke here

size_ten = 10
size_hundred = 100
size_thousand = 1000
size_million = 1000000

# Case 1 on the task said to retrieve n=10 random numbers from the uniform distribution [1,10]

# Remembering the set notation of [low, high), where low is included and high is excluded. 
# We could check the validity of our computation with the functions that we would show below (via console logging)

case_1_histogram = plt.figure(1, figsize=(7,7))

case_1_sample_ten = np.random.uniform(1,10,10)
print("For we are supposed to retrieve random numbers from [1,10], it begs the question as to whether the intervals are actually included in our computation.\n")
print("Does the random distribution of (low=1,high=10,size=10) includes samples from numbers that is less or equal to 10?", np.all(case_1_sample_ten <= 10))
print("Does the random distribution of (low=1,high=10,size=10) includes samples from numbers that is greater or equal to 1?", np.all(case_1_sample_ten >= 1))
print("\nAs the questions above has been answered, we will proceed to show the graph of other uniform distributions with differing number of sample size.")

case_1_sample_hundred = np.random.uniform(1,10,100)
case_1_sample_thousand = np.random.uniform(1,10,1000)
case_1_sample_million = np.random.uniform(1,10,1000000)

plt.hist(case_1_sample_ten, 15, density=True)
plt.hist(case_1_sample_hundred, 15, density=True)
plt.hist(case_1_sample_thousand, 15, density=True)
plt.hist(case_1_sample_million, 15, density=True)

case_1_histogram.suptitle('Uniform Distribution Case 1 Combined Histogram', fontsize=14, fontweight='bold')
case_1_axes_title = case_1_histogram.add_subplot(111)
case_1_histogram.subplots_adjust(top=0.85)
case_1_axes_title.set_title('retrieve n=10 random numbers from the uniform distribution [1,10] \nwith n iterating from 10,100,1000,1000000')
case_1_histogram.show()

print("\n---\nNow on to the second case.\n")

case_2_histogram = plt.figure(2, figsize=(7,7))

case_2_sample_ten = np.random.uniform(25,100,10)
print("For we are supposed to retrieve random numbers from [25,100], it begs the question as to whether the intervals are actually included in our computation.\n")
print("Does the random distribution of (low=25,high=100,size=10) includes samples from numbers that is less or equal to 25?", np.all(case_2_sample_ten <= 25))
print("Does the random distribution of (low=25,high=100,size=10) includes samples from numbers that is greater or equal to 10?", np.all(case_2_sample_ten >= 10))
print("\nAs the questions above has been answered, we will proceed to show the graph of other uniform distributions with differing number of sample size.")

case_2_sample_hundred = np.random.uniform(25,100,100)
case_2_sample_thousand = np.random.uniform(25,100,1000)
case_2_sample_million = np.random.uniform(25,100,1000000)

plt.hist(case_2_sample_ten, 15, density=True)
plt.hist(case_2_sample_hundred, 15, density=True)
plt.hist(case_2_sample_thousand, 15, density=True)
plt.hist(case_2_sample_million, 15, density=True)

case_2_histogram.suptitle('Uniform Distribution Case 2 Combined Histogram', fontsize=14, fontweight='bold')
case_2_axes_title = case_2_histogram.add_subplot(111)
case_2_histogram.subplots_adjust(top=0.85)
case_2_axes_title.set_title('retrieve n=10 random numbers from the uniform distribution [25,100] \nwith n iterating from 10,100,1000,1000000')
case_2_histogram.show()

print("\n---\nNow that the combined histograms of both cases has been shown, we will show the individual graphs.\n")

case_1_each, case_1_each_axes = plt.subplots(2, 2, figsize=(10,10))
case_1_each.suptitle('Uniform Distribution Case 1 Histogram of Every Sample Size', fontsize=14, fontweight='bold')

case_1_each_axes[0, 0].hist(case_1_sample_ten, 15, density=True)
case_1_each_axes[0, 0].set_title('low=1,high=10,size=10')
case_1_each_axes[1, 0].hist(case_1_sample_hundred, 15, density=True)
case_1_each_axes[1, 0].set_title('low=1,high=10,size=100')
case_1_each_axes[0, 1].hist(case_1_sample_thousand, 15, density=True)
case_1_each_axes[0, 1].set_title('low=1,high=10,size=1000')
case_1_each_axes[1, 1].hist(case_1_sample_million, 15, density=True)
case_1_each_axes[1, 1].set_title('low=1,high=10,size=1000000')

case_2_each, case_2_each_axes = plt.subplots(2, 2, figsize=(10,10))
case_2_each.suptitle('Uniform Distribution Case 2 Histogram of Every Sample Size', fontsize=14, fontweight='bold')

case_2_each_axes[0, 0].hist(case_2_sample_ten, 15, density=True)
case_2_each_axes[0, 0].set_title('low=25,high=100,size=10')
case_2_each_axes[1, 0].hist(case_2_sample_hundred, 15, density=True)
case_2_each_axes[1, 0].set_title('low=25,high=100,size=100')
case_2_each_axes[0, 1].hist(case_2_sample_thousand, 15, density=True)
case_2_each_axes[0, 1].set_title('low=25,high=100,size=1000')
case_2_each_axes[1, 1].hist(case_2_sample_million, 15, density=True)
case_2_each_axes[1, 1].set_title('low=25,high=100,size=1000000')

plt.show()