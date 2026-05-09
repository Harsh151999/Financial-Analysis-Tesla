# Financial Data Analytics (Tesla)

> End-to-end stock analysis (2012–2020) — risk metrics, Monte Carlo simulation, and an interactive executive dashboard.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Plotly](https://img.shields.io/badge/Plotly-Dash-3F4F75?logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

<!-- If you host the dashboard on GitHub Pages, add the link here -->
<!-- **Live dashboard:** [Tesla_Dashboard.html](https://YOUR_USERNAME.github.io/tesla-financial-data-analytics/Tesla_Dashboard.html) -->

---

## Project overview

A full data-analyst workflow applied to Tesla (TSLA): **acquire → wrangle → engineer features → model risk → communicate**. Mirrors the analytical cycle used by market-risk, investment-analytics, and FP&A teams at financial institutions.

---

## Analysis modules

### 1 · Data collection & wrangling
- Historical OHLCV via `yfinance`, aligned with Tesla SEC 10-K fundamentals
- Handles missing values, date alignment, and multi-source merging
- Auto-generates realistic synthetic data when `yfinance` is unavailable — every cell always runs

### 2 · Technical indicator engineering

| Category | Indicators |
|---|---|
| Trend | SMA (20/50/200), EMA (12/26), MACD & Signal |
| Volatility | Bollinger Bands (±2σ), 30-day rolling volatility |
| Momentum | RSI (14-day) |
| Returns | Daily returns, log returns, cumulative returns |

### 3 · Risk & statistical analysis

| Metric | Description |
|---|---|
| CAGR | Compound annual growth rate over the period |
| Annual volatility | Annualised std dev of daily returns |
| Sharpe ratio | Risk-adjusted return vs the risk-free rate |
| VaR (95%) | Worst expected single-day loss at 95% confidence |
| CVaR (95%) | Expected loss conditional on breaching VaR |
| Max drawdown | Largest peak-to-trough decline in the period |
| Skewness / kurtosis | Return distribution shape and tail-risk behaviour |

### 4 · Monte Carlo price simulation (GBM)

Method: Geometric Brownian Motion — 1,000 simulations × 252 trading days.

| Scenario | 1-year price target (from Dec 2020) |
|---|---|
| Bear | ~$500 |
| Base | ~$700 |
| Bull | ~$1,000+ |

Output includes percentile-based fan charts directly usable for stress-testing and scenario analysis.

### 5 · Financial statement integration

Manually collected revenue, net income, delivery numbers, and cash-flow data from Tesla SEC 10-K filings (2012–2020). Key finding: 2020 GAAP profit was entirely dependent on $1.6 B in regulatory-credit sales.

### 6 · Visualisation & dashboard

- Static publication-quality charts via `matplotlib` and `seaborn`
- Interactive charts via `Plotly` — zoom, hover tooltips, and exportable figures
- `Tesla_Dashboard.html` — self-contained executive dashboard (open in any browser)
- `Streamlit` app for live parameter exploration — adjust simulation inputs and see results update instantly

---

## Key insights

- **Unsustainable profit driver.** Tesla's first-ever GAAP profit depended entirely on $1.6 B in regulatory-credit sales; core auto operations remained loss-making.
- **Cash inflection point.** Operating cash flow swung from –$524 M (2015) to +$5.94 B (2020), signalling genuine financial maturity.
- **Extreme risk premium.** EV/EBITDA of 157× versus 12–14× for legacy automakers — high momentum, high volatility, and a tech-like multiple baked in.
- **Delivery explosion.** 188× increase in units delivered (2,650 → 499,550) drove the top line and ultimately the cash-flow turnaround.

---

## Repository structure

```
tesla-financial-data-analytics/
│
├── tesla_analysis.ipynb        # Main analysis notebook (data → insights)
├── Tesla_Dashboard.html        # Interactive executive dashboard
├── Tesla_BBA_Report.pdf        # Full academic report
├── requirements.txt            # Python dependencies
├── README.md
│
├── data/
│   └── tsla_ohlcv.csv          # Saved OHLCV data (optional)
│
└── images/
    ├── technical_dashboard.png
    ├── returns_risk_analysis.png
    └── monte_carlo_simulation.png
```

---

## Tech stack

| Tool | Category | Purpose |
|---|---|---|
| Python 3.8+ | Core | Primary language |
| `yfinance` | Data | Historical OHLCV acquisition |
| `pandas` | Data | Wrangling & transformation |
| `numpy` | Data | Numerical computing |
| `scipy` | Analysis | Statistical computations (skew, kurtosis, VaR) |
| `scikit-learn` | Modelling | Regression, clustering, cross-validation |
| `statsmodels` | Modelling | Time-series analysis, OLS, ARIMA |
| `Prophet` | Modelling | Trend decomposition & forecasting |
| `matplotlib`, `seaborn` | Visualisation | Static publication-quality charts |
| `Plotly` | Visualisation | Interactive charts with hover & zoom |
| `Dash` | Visualisation | Web-based analytical dashboard |
| `Streamlit` | Visualisation | Live parameter exploration app |
| `SQLite` | Storage | Lightweight local data persistence |
| `PostgreSQL` | Storage | Production-grade relational data store |
| `Apache Spark` | Scale | Distributed processing for large datasets |
| `Docker` | DevOps | Containerised, reproducible environment |
| `FastAPI` | API | REST endpoints to serve model outputs |
| `Tableau` | BI | Executive-level visual reporting |
| Jupyter Notebook | Environment | Interactive analysis & prototyping |
| Git | Version control | Source history & collaboration |

---

## Quick start

**Option 1 — Jupyter notebook**
```bash
git clone https://github.com/YOUR_USERNAME/tesla-financial-data-analytics.git
cd tesla-financial-data-analytics
pip install -r requirements.txt
jupyter notebook tesla_analysis.ipynb
```

**Option 2 — Streamlit app**
```bash
pip install -r requirements.txt
streamlit run app.py
```

**Option 3 — Docker**
```bash
docker build -t tesla-analytics .
docker run -p 8501:8501 tesla-analytics
```

> No `yfinance`? The notebook automatically uses a realistic synthetic dataset so every cell executes without errors.

---

## Authors

**Harsh Parashar** — Python, data wrangling, visualisation, Monte Carlo, dashboard  
Kanishk Raj — Research & fundamental analysis  
Abhishek Kashyap — Valuation & report writing  

*Supervised by Dr. Vijay Agarwal, Dept. of Management, BIT Mesra*  
BBA Final Year Project — Birla Institute of Technology, Mesra, Ranchi

---

## Disclaimer

This project is for academic and portfolio demonstration purposes only. It does not constitute financial advice. All data is historical and publicly sourced. Past performance does not guarantee future results.
