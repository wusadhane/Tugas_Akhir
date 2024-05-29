import yfinance as yf
import pandas as pd
import numpy as np
import cvxpy as cp

# Daftar ticker saham yang ingin dianalisis
tickers = ["BBRM.JK", "BESS.JK", "BSML.JK", "BULL.JK", "CANI.JK"]

# Periode data historis
start_date = '2023-05-17'
end_date = '2024-05-17'

# Mengunduh data harga saham
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Menghitung return harian
returns = data.pct_change().dropna()

# Menghitung rata-rata return dan matriks kovariansi
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Expected return yang diinginkan
target_return = 0.02 / 252  # Misalnya, annualized return target adalah 2%

# Jumlah saham
n = len(mean_returns)

# Variabel optimasi
weights = cp.Variable(n)

# Expected return portofolio
portfolio_return = mean_returns.values @ weights

# Risiko portofolio (variansi)
portfolio_variance = cp.quad_form(weights, cov_matrix.values)

# Fungsi tujuan: meminimalkan risiko
objective = cp.Minimize(portfolio_variance)

# Batasan-batasan
constraints = [weights >= 0, 
               cp.sum(weights) == 1, 
               portfolio_return >= target_return]

# Problem
problem = cp.Problem(objective, constraints)

# Solusi
problem.solve()

# Bobot optimal
optimal_weights = weights.value

# Membuat DataFrame hasil
portfolio = pd.DataFrame({'Saham': tickers, 'Bobot': optimal_weights})
print(portfolio)
