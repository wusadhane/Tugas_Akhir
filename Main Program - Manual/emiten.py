import sqlite3
import pandas as pd
import random
import itertools

# 1. Membaca data dari database
conn = sqlite3.connect('database.db')
query = "SELECT ID, Nama_Sektor, Nama_SubSektor, Nama_Emiten FROM Data"
data = pd.read_sql_query(query, conn)

# 2. Menampilkan data kolom yang diinginkan
row = ['Nama_Emiten']  
data_terpilih = data[row]

# 3. Memfilter data
filter = data_terpilih[data['Nama_SubSektor'] == 'marine shipping']
list = filter.loc[:, 'Nama_Emiten'].tolist()

# print(list)

# num_assets = 3

# # Jumlah kombinasi portofolio yang diinginkan
# num_portfolios = 5

# for i in range(num_portfolios):
#     # Pilih secara acak aset-aset dari list
#     selected_assets = random.sample(list, num_assets)

#     # Buat alokasi bobot secara acak (dalam persen)
#     weights = [random.uniform(0, 1) for _ in range(num_assets)]
#     total_weight = sum(weights)
#     weights = [w / total_weight * 100 for w in weights]  # Normalisasi ke dalam persen

#     # Hitung nilai portofolio
#     portfolio_value = 1000000  
#     asset_values = [portfolio_value * w / 100 for w in weights]

#     # Menampilkan hasil untuk setiap kombinasi
#     print("Portfolio", i+1)
#     print("Selected Assets:", selected_assets)
#     print("Weights:", weights)
#     print("Asset Values:", asset_values)
#     print()