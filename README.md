#  — Financial & Product Analysis Tesla, Inc. (TSLA) (2012–2020)

> A comprehensive financial analysis of Tesla, Inc. combining quantitative Python-based stock analysis with fundamental research, valuation modelling, and strategic insights.

---

#  

Authors

| Name | Roll No. | Role |
|------|----------|------|
| Kanishk Raj | BBA/15073/19 | Research & Fundamental Analysis |
| Abhishek Kashyap | BBA/15083/19 | Valuation & Report Writing |
| Harsh Parashar | BBA/15102/19 | ⚙️ Tech Lead — Python, Data & Visualisation |

**Supervised by:** Dr. Vijay Agarwal, Head of Department — Management
**Institution:** Birla Institute of Technology, Mesra, Ranchi
**Degree:** Bachelor of Business Administration (BBA) — Final Year Project

---

# Project Overview

This project delivers an end-to-end analysis of Tesla, Inc. from 2012 to 2020 — spanning:

- **Technical stock analysis** using Python (yfinance, pandas, matplotlib)
- **Fundamental financial analysis** based on SEC 10-K filings
- **Macroeconomic & industry landscape** including EV market growth and COVID-19 impact
- **Valuation modelling** via DCF and Comparable Company Analysis (CCA)
- **Monte Carlo price simulation** using Geometric Brownian Motion (GBM)
- **Strategic outlook** covering Gigafactories, FSD, and energy storage

---

# Repository Structure

tesla-financial-analysis/
│
├── tesla_analysis.ipynb        # Python notebook — technical & quantitative analysis
├── Tesla_BBA_Report.pdf        # Full academic report (BBA Final Project)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── data/
│   └── tsla_ohlcv.csv          # Optional: saved OHLCV data from Yahoo Finance
│
└── images/
├── technical_dashboard.png
├── returns_risk_analysis.png
├── financial_highlights.png
└── monte_carlo_simulation.png


---

## 🔧 Tech Stack
> Technical implementation by **Harsh Parashar** (Tech Lead)

| Tool | Purpose |
|------|---------|
| `Python 3.8+` | Core programming language |
| `yfinance` | Live stock data from Yahoo Finance |
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computations |
| `matplotlib` | Data visualisation |
| `seaborn` | Statistical plots |
| `scipy` | Statistical analysis (skewness, kurtosis, VaR) |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/tesla-financial-analysis.git
cd tesla-financial-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the notebook
```bash
jupyter notebook tesla_analysis.ipynb
```

> **Note:** If `yfinance` is unavailable, the notebook automatically falls back to
> synthetic TSLA-like data so all cells run without errors.

---

#  Analysis Modules

### 1. Technical Indicators
- Simple Moving Averages: SMA 20 / 50 / 200
- Exponential Moving Averages: EMA 12 / 26 → MACD & Signal Line
- Bollinger Bands (20-day, ±2σ)
- RSI — 14-day Relative Strength Index
- Daily / Log Returns, Cumulative Return, 30-day Rolling Volatility

### 2. Risk Analysis

| Metric | Description |
|--------|-------------|
| Annual Return (CAGR) | Compound annual growth rate |
| Annual Volatility | Annualised standard deviation of returns |
| Sharpe Ratio | Risk-adjusted return |
| VaR 95% | Value at Risk — worst expected daily loss (95% confidence) |
| CVaR 95% | Conditional VaR — expected loss beyond VaR threshold |
| Max Drawdown | Peak-to-trough price decline |
| Skewness / Kurtosis | Return distribution shape and tail risk |

### 3. Annual Financial Highlights (SEC Data)

Tesla's revenue grew **76× from $413M (2012) to $31.54B (2020)**. Key milestones:

| Year | Revenue | Net Income | Highlight |
|------|---------|------------|-----------|
| 2012 | $0.41B | $(0.40)B | Model S launch |
| 2017 | $11.76B | $(1.96)B | Model 3 ramp begins |
| 2019 | $24.58B | $(0.86)B | Shanghai Gigafactory opens |
| 2020 | $31.54B | **$0.69B** | ✅ First full-year GAAP profit |

### 4. Monte Carlo Simulation
- **Method:** Geometric Brownian Motion (GBM)
- **Parameters:** 1,000 simulations × 252 trading days (1 year)
- **Output:** Percentile-based price scenarios (Bear / Base / Bull)

---

## 💡 Key Findings

1. **Regulatory credit dependency:** Tesla's 2020 GAAP profit ($721M) was enabled by
   $1.6B in regulatory credit sales — without these, core operations would have been loss-making.

2. **Technology premium:** Tesla traded at 157× EV/EBITDA vs. 12–14× for Ford/GM,
   reflecting the market's view of Tesla as a tech company, not an automaker.

3. **Cash flow inflection:** Operating cash flow turned sharply positive in 2020
   ($5.94B), up from –$524M in 2015 — signalling financial maturation.

4. **Delivery ramp:** From 2,650 units (2012) to 499,550 units (2020) — a 188×
   increase driven by Model 3 and Model Y.

5. **Monte Carlo range (1-year from Dec 2020):**
   - Bear case (5th pct): ~$500
   - Base case (50th pct): ~$700
   - Bull case (95th pct): ~$1,000+

---

# Data Sources

- [Tesla SEC 10-K Annual Reports](https://www.sec.gov/cgi-bin/browse-edgar) (2012–2020)
- [Tesla Investor Relations](https://ir.tesla.com) — Delivery & production reports
- [Yahoo Finance](https://finance.yahoo.com) via `yfinance` — OHLCV stock data
- IEA Global EV Outlook 2021
- BloombergNEF Electric Vehicle Outlook 2020

---

# Disclaimer

This project is for **academic and educational purposes only**. It does not constitute
financial advice. All analysis is historical and based on publicly available data.
Past performance is not indicative of future results.

---

# License

BBA Final Year Project — BIT Mesra. All rights reserved by the authors.
For academic reference only.

---

*"Tesla's 2012–2020 journey stands as a paradigmatic case study in disruptive innovation,
strategic patience, and the market's willingness to price in transformative long-term potential."*
