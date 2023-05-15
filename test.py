from src import data_loader
from src import data_analyser
url = 'https://drive.google.com/drive/folders/1O_B3fHgjKmjrYxIoUyutJmd1fuovTLQv'

data_loader = data_loader.DataLoader(url=url, dest_folder='datasets')
df = data_loader.load_data(columns_to_keep=['FTHG', 'FTAG', 'HxG', 'AxG'])

analyser = data_analyser.DataAnalyser(data=df)

arr = analyser.create_np_array()

kurt = analyser.calculate_kurtosis()
skew = analyser.calculate_skewness()
print(kurt)
print(skew)
