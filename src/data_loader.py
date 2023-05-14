from os import listdir
from os.path import isdir

import gdown
import pandas as pd
class DataLoader:
    #  Data loader class, downloads data from the Google Drive and transforms it into a pandas dataframe
    def __init__(self, url: str, dest_folder: str):
        self.url = url
        self.dest_folder = dest_folder
        self.dataframe = None

    def download_data(self):
        """
        Downloads data from the Google Drive to the datasets folder
        :return: None
        """
        if isdir(self.dest_folder):
            pass
        else:
            url = self.url
            gdown.download_folder(url=url, output=self.dest_folder)

    def read_data(self):
        """
        Transforms CSV files into pandas DataFrame
        :return: pd.DataFrame : Dataframe of the input data
        """
        files = [f for f in listdir(self.dest_folder)]
        df_list = []

        for file in files:
            df = pd.read_csv(self.dest_folder + '/' + file)
            df_list.append(df)
        return pd.concat(df_list)

    def load_data(self):
        """
        Calls the download_data and read_data methods
        :return: pd.DataFrame: DataFrame of the input data
        """
        self.download_data()
        self.dataframe = self.read_data()

        return self.dataframe




