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

# import yfinance as yf
# import pandas as pd

# # Simpan kode IHSG
# ihsg = yf.Ticker('^JKSE')

# # Dapatkan data historis selama 1 tahun
# historical_data = ihsg.history(start='2023-05-17', end='2024-05-17')

# # Ambil data hanya untuk setiap bulan
# monthly_data = historical_data.resample('M').last()

# # Simpan data dalam file CSV
# monthly_data.to_csv('ihsg_monthly_data.csv', index=False)


import yfinance as yf
import pandas as pd

# Daftar ticker saham transportasi laut yang masih aktif (contoh)
# Anda perlu memastikan bahwa daftar ini adalah yang terbaru dan sesuai dengan kebutuhan
tickers = ["BBRM.JK", "BESS.JK", "BSML.JK", "BULL.JK", "CANI.JK", "HAIS.JK", "HATM.JK", "CBRE.JK",
        "IPCC.JK", "MITI.JK", "NELY.JK", "PSSI.JK", "RIGS.JK", "SHIP.JK",
         "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK", "KLAS.JK", "HATM.JK"]

# Fungsi untuk mengecek apakah saham masih aktif
def is_active(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return not info['quoteType'] == 'DELISTED'
    except Exception as e:
        print(f"Error checking {ticker}: {e}")
        return False

# Mengambil harga saham hanya untuk saham yang masih aktif
active_tickers = [ticker for ticker in tickers if is_active(ticker)]

# Mengambil data harga saham untuk ticker yang aktif
data = yf.download(active_tickers, start="2023-05-17", end="2024-05-17")

# Menyimpan data ke file CSV
data.to_csv('marine_transport_stock_prices.csv')

print("Data saham aktif sudah diunduh dan disimpan ke marine_transport_stock_prices.csv")
