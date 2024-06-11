import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import TruncatedSVD
car_prices_df = pd.read_csv('https://gist.githubusercontent.com/palles77/38bd063939c1ac08b8d1e4f7c2c26abc/raw/b01ca987613684082b3897dd24e2f00909da6bd9/car_prices.csv')
car_prices_df = car_prices_df.drop(['ID', 'Price', 'Doors'], axis=1)
car_prices_df['Levy'] = car_prices_df['Levy'].replace('-', '0').astype(int)
car_prices_df['Mileage'] = car_prices_df['Mileage'].str.replace(' km', '').astype(int)
categorical_columns = ['Leather interior', 'Manufacturer', 'Model', 'Category', 'Fuel type', 'Gear box type', 'Drive wheels', 'Wheel', 'Color']
label_encoder = LabelEncoder()
for column in categorical_columns:
    car_prices_df[column] = car_prices_df[column].fillna('Missing')
    car_prices_df[column] = label_encoder.fit_transform(car_prices_df[column])
car_prices_df.fillna(0, inplace=True)
for col in car_prices_df.columns:
    if car_prices_df[col].dtype == 'object':
        car_prices_df[col] = pd.to_numeric(car_prices_df[col], errors='coerce')
car_prices_df.fillna(0, inplace=True)  
data_array = car_prices_df.to_numpy()
svd = TruncatedSVD(n_components=5)
reduced_data = svd.fit_transform(data_array)
reduced_df = pd.DataFrame(reduced_data, columns=['CUR_1', 'CUR_2', 'CUR_3', 'CUR_4', 'CUR_5'])
print(reduced_df.head())
reduced_df_with_labels = pd.concat([car_prices_df.reset_index(drop=True), reduced_df], axis=1)
print(reduced_df_with_labels.head())
