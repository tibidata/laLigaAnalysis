from src import data_loader

url = 'https://drive.google.com/drive/folders/1O_B3fHgjKmjrYxIoUyutJmd1fuovTLQv'

data_loader = data_loader.DataLoader(url=url, dest_folder='datasets')
df = data_loader.load_data()
print(df.shape)