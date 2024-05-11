from itertools import combinations
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, expected_returns
import yfinance as yf

# Fungsi untuk mengoptimalkan portofolio
def optimize_portfolio(stocks, rfr):
    data = yf.download(stocks, start="2023-01-01", end="2024-01-01")['Adj Close']
    mu = expected_returns.mean_historical_return(data)
    S = risk_models.sample_cov(data)
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    ef.portfolio_performance(risk_free_rate=rfr)
    return ef.clean_weights()

# Daftar saham yang tersedia
stocks = ["BBRM.JK", "BESS.JK", "BSML.JK", "BULL.JK", "CANI.JK", "HAIS.JK", "HATM.JK",
                      "HITS.JK", "IPCC.JK", "MITI.JK", "NELY.JK", "PSSI.JK", "RIGS.JK", "SHIP.JK",
                      "SMDR.JK", "SOCI.JK", "TCPI.JK", "TMAS.JK", "TPMA.JK", "WINS.JK"] # Tambahkan semua saham yang tersedia

# Tentukan Risk-Free Rate
rfr = 0.0675  # Contoh: 6,75% sebagai RFR

# Jumlah portofolio yang ingin dioptimalkan
num_portfolios = 3

# Menghasilkan semua kombinasi yang mungkin dari saham yang tersedia
stock_combinations = list(combinations(stocks, num_portfolios))

# Dictionary untuk menyimpan hasil optimasi setiap portofolio
optimized_portfolios = {}

# Loop melalui setiap kombinasi dan mengoptimalkan
for i, combination in enumerate(stock_combinations):
    optimized_portfolios[f"Portofolio {i+1}"] = optimize_portfolio(list(combination), rfr)

# Sekarang `optimized_portfolios` berisi hasil optimasi untuk setiap kombinasi portofolio
