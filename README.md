# Tesla (TSLA) – Comprehensive Financial Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)](https://jupyter.org/)

A complete financial & technical analysis of **Tesla (TSLA)** stock, covering:

- Historical price data (2019–2024) with technical indicators (SMA, Bollinger Bands, RSI, MACD)
- Daily returns, cumulative return, and rolling volatility
- Annual financial fundamentals (revenue, net income, free cash flow, vehicle deliveries)
- Monte Carlo simulation of 1‑year future price paths (1,000 simulations)
- Risk metrics: annualised volatility, Sharpe ratio, Value‑at‑Risk (VaR), maximum drawdown

The analysis is available as both a **Python script** (`tesla_financial_analysis.py`) and an **interactive Jupyter Notebook** (`tesla_financial_analysis.ipynb`).

---

## 📊 Key Visual Results

### 1. Technical Dashboard
![Technical Analysis](outputs/01_technical_analysis.png)

### 2. Returns & Risk Analysis
![Returns and Risk](outputs/02_returns_risk.png)

### 3. Annual Financial Highlights (2018–2023)
![Financials](outputs/03_financials.png)

### 4. Monte Carlo Forecast (1 Year)
![Monte Carlo](outputs/04_monte_carlo.png)

### 5. Summary Metrics Card
![Summary](outputs/05_summary.png)

---

## 📈 Key Findings (from the analysis)

| Metric                     | Value                |
|----------------------------|----------------------|
| Current Price              | $3,536.14 *          |
| Period High                | $4,572.88            |
| Period Low                 | $40.17               |
| Total Return (period)      | **5686.2%**          |
| Annual Return (CAGR)       | **55.4%**            |
| Annual Volatility          | **55.4%**            |
| Sharpe Ratio               | **2.24**             |
| Max Drawdown               | **-55.4%**           |
| Monte Carlo – Bear (5th)   | $2,808.59            |
| Monte Carlo – Base (Median)| $6,925.58            |
| Monte Carlo – Bull (95th)  | $17,290.42           |

> *Note: The absolute price values shown are from the **simulated/synthetic** data included in the fallback mode of the script. Real‑world TSLA prices (split‑adjusted) are far lower. Replace with live `yfinance` data for actual figures.*

---

## Features

- **Data acquisition** – downloads live TSLA data from Yahoo Finance (or generates realistic synthetic data if `yfinance` is unavailable).
- **Technical indicators** – SMA 20/50/200, Bollinger Bands, RSI (14), MACD, signal line.
- **Risk analysis** – daily return distribution, rolling 30‑day volatility, VaR (95%), CVaR, maximum drawdown.
- **Fundamentals** – annual revenue, gross profit, net income, FCF, deliveries (2018–2023).
- **Monte Carlo simulation** – 1,000 Geometric Brownian Motion (GBM) paths over 252 trading days.
- **Publication‑ready plots** – 5 high‑resolution charts summarising all aspects.
- **Console summary** – prints a clean metrics table at the end.

---

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/Harsh151999/Financial-Analysis-Tesla.git
cd Financial-Analysis-Tesla
pip install -r requirements.txt

Usage
Run the full analysis script
bash
python tesla_financial_analysis.py
All charts are saved to the outputs/ folder.

Run the Jupyter Notebook interactively
bash
jupyter notebook tesla_financial_analysis.ipynb
Execute cells one by one to see intermediate outputs and modify parameters (e.g., ticker, date range, number of Monte Carlo simulations).

 Methodology
Technical Indicators
Bollinger Bands – 20‑day SMA ± 2 standard deviations.

RSI – standard 14‑day formula (100 – 100/(1 + RS)).

MACD – 12‑day EMA minus 26‑day EMA; signal line is 9‑day EMA of MACD.

Statistical Risk Metrics
Annualised volatility = daily std × √252

Sharpe ratio = (CAGR – risk‑free rate) / annual volatility (risk‑free assumed 0 for simplicity)

VaR 95% – 5th percentile of daily returns

CVaR (Expected Shortfall) – average of returns ≤ VaR

Monte Carlo Simulation (GBM)
Uses historical daily log‑returns to estimate μ and σ

Simulates 1,000 independent price paths:

S
t
+
1
=
S
t
⋅
e
(
μ
−
σ
2
2
)
Δ
t
+
σ
Δ
t
 
Z
S 
t+1
​
 =S 
t
​
 ⋅e 
(μ− 
2
σ 
2
 
​
 )Δt+σ 
Δt
​
 Z
 
where 
Z
∼
N
(
0
,
1
)
Z∼N(0,1) and Δt = 1 day.

Project Structure
text
Financial-Analysis-Tesla/
├── tesla_financial_analysis.py     # Single‑file Python script
├── tesla_financial_analysis.ipynb  # Interactive Jupyter notebook
├── outputs/                        # Generated charts
│   ├── 01_technical_analysis.png
│   ├── 02_returns_risk.png
│   ├── 03_financials.png
│   ├── 04_monte_carlo.png
│   └── 05_summary.png
├── requirements.txt
└── README.md
