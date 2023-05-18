import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab
from scipy.stats import skew, kurtosis, chisquare, kstest, pearsonr, ttest_ind, spearmanr
import statsmodels.api as sm


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
        """
        Checks if the input data has null values.
        :return: bool:
        """
        self.is_nulls = self.data.isnull().values.any()
        return self.is_nulls

    def create_np_array(self):
        """
        Creates a ndarray from the input data
        :return: ndarray:
        """
        if self.is_nulls:
            raise Exception('There are NaN numbers in the dataframe, please remove them before continuing')
        else:
            self.data_array = self.data.to_numpy()

        return self.data_array

    def calculate_mean(self):
        """
        Calculates the mean colum-wise
        :return: ndarray : means of the columns
        """
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            self.column_means = np.mean(self.data_array, axis=0)

        return self.column_means

    def calculate_median(self):
        """
        Calculates the median colum-wise
        :return: ndarray : medians of the columns
        """
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            self.column_medians = np.median(self.data_array, axis=0)

        return self.column_medians

    def plot_boxplot(self):
        """
        Plots the boxplot of the columns
        :return: None
        """
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
        """
        Plots the histograms of the columns
        :return: None
        """
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
        """
        Calculates the skewness of the variables
        :return: ndarray: array of the skewnesses
        """
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            self.skewness = skew(self.data_array)

            return self.skewness

    def calculate_kurtosis(self):
        """
        Calculates the kurtosis of the variables
        :return: ndarray: array of the kurtosis
        """
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            self.kurtosis = kurtosis(self.data_array)

            return self.kurtosis

    def qq_plot(self):
        """
        Plots the Q-Q plot of the variables
        :return:
        """
        x_labels = ['FTHG', 'FTAG', 'HxG', 'AxG']
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            for i in range(self.data_array.shape[1]):
                sm.qqplot(self.data_array[:, i], line='45')
                plt.title('Normal Q-Q plot - ' + x_labels[i])
                plt.savefig('plots/qq_plot_' + str(i))
                plt.show()

    def pearson_corr(self):
        """
        Calculates the pearson-correlation of the variables
        :return: list: pvalue and statistic of the test
        """
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            res1 = pearsonr(self.data_array[:, 0], self.data_array[:, 2])
            res2 = pearsonr(self.data_array[:, 1], self.data_array[:, 3])
            return [res1, res2]

    def t_test(self):
        """
        Does the t-test
        :return: list: pvalue and statistic of the test
        """
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            res1 = ttest_ind(self.data_array[:, 0], self.data_array[:, 2])
            res2 = ttest_ind(self.data_array[:, 1], self.data_array[:, 3])

            return [res1, res2]

    def spearman(self):
        """
        Calculates the spearman-correlation of the variables
        :return: list: pvalue and statistic of the test
        """
        if self.data_array is None:
            raise Exception('Use the create_np_array() method first')
        else:
            res1 = spearmanr(self.data_array[:, 0], self.data_array[:, 2])
            res2 = spearmanr(self.data_array[:, 1], self.data_array[:, 3])

            return [res1, res2]
