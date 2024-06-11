import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
car_prices_df = pd.read_csv('https://gist.githubusercontent.com/palles77/38bd063939c1ac08b8d1e4f7c2c26abc/raw/b01ca987613684082b3897dd24e2f00909da6bd9/car_prices.csv')
car_prices_df = car_prices_df.drop(['ID', 'Price', 'Doors'], axis=1)
car_prices_df['Levy'] = car_prices_df['Levy'].replace('-', '0').astype(int)
car_prices_df['Mileage'] = car_prices_df['Mileage'].str.replace(' km', '').astype(int)
categorical_columns = ['Leather interior', 'Manufacturer', 'Model', 'Category', 'Fuel type', 'Gear box type', 'Drive wheels', 'Wheel', 'Color']
label_encoder = LabelEncoder()
for column in categorical_columns:
    car_prices_df[column] = car_prices_df[column].fillna('Missing')  # Uzupełnienie brakujących wartości
    car_prices_df[column] = label_encoder.fit_transform(car_prices_df[column])
car_prices_df.fillna(0, inplace=True)
for col in car_prices_df.columns:
    if car_prices_df[col].dtype == 'object':
        car_prices_df[col] = pd.to_numeric(car_prices_df[col], errors='coerce')
car_prices_df.fillna(0, inplace=True)  # Zamiana ewentualnych wartości NaN
data_array = car_prices_df.to_numpy()
svd = TruncatedSVD(n_components=5)
reduced_data = svd.fit_transform(data_array)
k_values = range(3, 10)
inertia_values = []
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(reduced_data)
    inertia_values.append(kmeans.inertia_)
plt.figure(figsize=(10, 6))
plt.plot(k_values, inertia_values, marker='o')
plt.xlabel('Liczba klastrów (k)')
plt.ylabel('Inercja')
plt.title('Wykres inercji dla różnych wartości k')
plt.grid(True)
plt.show()
k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(reduced_data)
reduced_df = pd.DataFrame(reduced_data, columns=['SVD_1', 'SVD_2', 'SVD_3', 'SVD_4', 'SVD_5'])
reduced_df['Cluster'] = clusters
print(reduced_df.head())
sns.pairplot(reduced_df, hue='Cluster', palette='tab10')
plt.show()