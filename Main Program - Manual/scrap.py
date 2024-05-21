# import yfinance as yf
# import pandas as pd

# # Daftar saham transportasi laut
# saham = ["BBRM.JK", "BESS.JK", "BSML.JK", "BULL.JK", "CANI.JK", "HAIS.JK", "HATM.JK", "CBRE.JK",
#          "HITS.JK", "IPCC.JK", "MITI.JK", "NELY.JK", "PSSI.JK", "RIGS.JK", "SHIP.JK",
#          "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK", "KLAS.JK", "HATM.JK"]

# # Ambil data harga saham dari Yahoo Finance
# start_date = "2023-05-17"
# end_date = "2024-05-17"
# data = yf.download(saham, start=start_date, end=end_date)["Adj Close"]

# # Resample data per bulan
# data_monthly = data.resample("M").last()

# # Simpan data ke dalam file CSV
# data_monthly.to_csv("harga_saham_transportasi_laut_per_bulan.csv")

# print("Data harga saham per bulan berhasil disimpan dalam file harga_saham_transportasi_laut_per_bulan.csv")


# IHSG

import yfinance as yf
import pandas as pd

# Simpan kode IHSG
ihsg = yf.Ticker('^JKSE')

# Dapatkan data historis selama 1 tahun
historical_data = ihsg.history(start='2023-05-17', end='2024-05-17')

# Ambil data hanya untuk setiap bulan
monthly_data = historical_data.resample('M').last()

# Simpan data dalam file CSV
monthly_data.to_csv('ihsg_monthly_data.csv', index=False)
