
import matplotlib.pyplot as plt
import numpy as np


class Distribution:

    def __init__(self, mean=0, standard_deviation=0.1, size=1000):
        '''
        For Distribution Graph
        parameters: mean(optional), standard_deviation(optional), size(optional) 
        '''
        self.mean = mean
        self.standard_deviation = standard_deviation
        self.size = size
        self.arr = np.random.normal(
            self.mean, self.standard_deviation, self.size)

    def normal(self, probablity_density=False):
        '''
        Input: probablity_density function(deafult: False)
        Output: Normally Distributed Histogram
        '''
        if probablity_density:

            n, bins, patches = plt.hist(self.arr, 30, density=True)
            plt.plot(bins, 1/(self.standard_deviation * np.sqrt(2 * np.pi)) *
                     np.exp(- (bins - self.mean)**2 / (2 * self.standard_deviation**2)))
            plt.show()
        else:
            plt.hist(self.arr, 30, density=True)
            plt.show()

    def estimated_population(self):
        '''
        ========
        In Beta
        ========
        To see the difference between Population Mean and varience
        and Estimated Mean and varience from smaller dataset 
        '''

        # Population Mean
        sum_of_arr = 0
        for i in self.arr:
            sum_of_arr += i
        population_mean = sum_of_arr/len(self.arr)

        # Population Varience
        sum_of_diff_population = 0
        for a in self.arr:
            sum_of_diff_population += (a-population_mean)**2
        population_varience = sum_of_diff_population/len(self.arr)

        # Estimated Mean
        estimated_arr = np.random.normal(size=10)
        sum_of_estimated_arr = 0
        for j in estimated_arr:
            sum_of_estimated_arr += j
        estimated_mean = sum_of_estimated_arr/len(estimated_arr)

        # Population Varience
        sum_of_diff_estimated = 0
        for b in estimated_arr:
            sum_of_diff_estimated += (b-estimated_mean)**2
        estimated_varience = sum_of_diff_estimated/len(estimated_arr)

        print("Population Mean is: {}, Estimated Mean is {}".format(
            population_mean, estimated_mean))
        print("Population varience is {}, Estimated Varience is {}".format(
            population_varience, estimated_varience))
