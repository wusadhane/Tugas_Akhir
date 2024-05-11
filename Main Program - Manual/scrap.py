import yfinance as yf
import pandas as pd

def scrape_stock_prices(ticker_symbols):
    stock_data = yf.download(ticker_symbols, start="2020-01-01", end="2024-05-01") # Ubah tanggal sesuai kebutuhan
    return stock_data['Adj Close']

def save_to_csv(data, filename):
    data.to_csv(filename)

if __name__ == "__main__":
    # Daftar ticker simbol saham sektor marine shipping Indonesia
    list_saham = ["BBRM.JK", "BESS.JK", "BSML.JK", "BULL.JK", "CANI.JK", "HAIS.JK", "HATM.JK",
                      "HITS.JK", "IPCC.JK", "MITI.JK", "NELY.JK", "PSSI.JK", "RIGS.JK", "SHIP.JK",
                      "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK"]

    # Ambil data harga saham
    stock_prices = scrape_stock_prices(list_saham)
    
    # Simpan data ke dalam file CSV
    save_to_csv(stock_prices, "Harga_saham.csv")
