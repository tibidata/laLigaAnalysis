import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis, chisquare, kstest


class DataAnalyser:
    def __init__(self, data: pd.DataFrame):
        self.kurtosis = None
        self.skewness = None
        self.column_medians = None
        self.column_means = None
        self.data_array = None
        self.data = data
        self.is_nulls = None

    def check_nulls(self):
        self.is_nulls = self.data.isnull().values.any()
        return self.is_nulls

    def create_np_array(self):
        if self.is_nulls:
            raise Exception('There are NaN numbers in the dataframe, please remove them before continuing')
        else:
            self.data_array = self.data.to_numpy()

        return self.data_array

    def calculate_mean(self):
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            self.column_means = np.mean(self.data_array, axis=0)

        return self.column_means

    def calculate_median(self):
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            self.column_medians = np.median(self.data_array, axis=0)

        return self.column_medians

    def plot_boxplot(self):
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            data_list = []
            for i in range(self.data_array.shape[1]):
                data_list.append(self.data_array[:, i])
            fig, ax = plt.subplots()
            ax.set_xticklabels(['home goals', 'away goals', 'expected home', 'expected away'])
            plt.boxplot(x=data_list)
            plt.title('Box plots of the goals')
            plt.ylabel('Number of goals')

            plt.savefig('plots/boxplot.png')

            plt.show()

    def plot_hist(self):
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            x_labels = ['home goals', 'away goals', 'expected home', 'expected away']

            f, a = plt.subplots(2, 2)
            a = a.ravel()
            for idx, ax in enumerate(a):
                ax.hist(self.data_array[:, idx])
                ax.set_xlabel(x_labels[idx])
                ax.set_ylabel('number of goals')
            plt.tight_layout()
            plt.savefig('plots/histograms.png')
            plt.show()

    def calculate_skewness(self):
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            self.skewness = skew(self.data_array)

            return self.skewness

    def calculate_kurtosis(self):
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            self.kurtosis = kurtosis(self.data_array)

            return self.kurtosis

    def chi_square_test(self):

        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            stat, p = chisquare(self.data_array)
            return p

    def kolmogorov_test(self):

        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            stat, p = kstest(self.data_array[:, 2], 'norm')

        return p