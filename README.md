# Financial Analysis [Tesla, Inc. (TSLA) (2012–2020)]

Project overview
A full data-analyst workflow applied to Tesla (TSLA): acquire → wrangle → engineer features → model risk → communicate. Mirrors the analytical cycle used by market-risk, investment-analytics, and FP&A teams at financial institutions.

Analysis modules
1 · Data collection & wrangling

Historical OHLCV via yfinance, aligned with Tesla SEC 10-K fundamentals
Handles missing values, date alignment, and multi-source merging
Auto-generates realistic synthetic data when yfinance is unavailable — every cell always runs

2 · Technical indicator engineering
CategoryIndicatorsTrendSMA (20/50/200), EMA (12/26), MACD & SignalVolatilityBollinger Bands (±2σ), 30-day rolling volatilityMomentumRSI (14-day)ReturnsDaily returns, log returns, cumulative returns
3 · Risk & statistical analysis
MetricDescriptionCAGRCompound annual growth rate over the periodAnnual volatilityAnnualised std dev of daily returnsSharpe ratioRisk-adjusted return vs the risk-free rateVaR (95%)Worst expected single-day loss at 95% confidenceCVaR (95%)Expected loss conditional on breaching VaRMax drawdownLargest peak-to-trough decline in the periodSkewness / kurtosisReturn distribution shape and tail-risk behaviour
4 · Monte Carlo price simulation (GBM)
Method: Geometric Brownian Motion — 1,000 simulations × 252 trading days.
Scenario1-year price target (from Dec 2020)Bear~$500Base~$700Bull~$1,000+
Output includes percentile-based fan charts directly usable for stress-testing and scenario analysis.
5 · Financial statement integration
Manually collected revenue, net income, delivery numbers, and cash-flow data from Tesla SEC 10-K filings (2012–2020). Key finding: 2020 GAAP profit was entirely dependent on $1.6 B in regulatory-credit sales.
6 · Visualisation & dashboard

Static publication-quality charts via matplotlib and seaborn
Interactive charts via Plotly — zoom, hover tooltips, and exportable figures
Tesla_Dashboard.html — self-contained executive dashboard (open in any browser)
Streamlit app for live parameter exploration — adjust simulation inputs and see results update instantly


Key insights

Unsustainable profit driver. Tesla's first-ever GAAP profit depended entirely on $1.6 B in regulatory-credit sales; core auto operations remained loss-making.
Cash inflection point. Operating cash flow swung from –$524 M (2015) to +$5.94 B (2020), signalling genuine financial maturity.
Extreme risk premium. EV/EBITDA of 157× versus 12–14× for legacy automakers — high momentum, high volatility, and a tech-like multiple baked in.
Delivery explosion. 188× increase in units delivered (2,650 → 499,550) drove the top line and ultimately the cash-flow turnaround.


Repository structure
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

Tech stack
ToolCategoryPurposePython 3.8+CorePrimary languageyfinanceDataHistorical OHLCV acquisitionpandasDataWrangling & transformationnumpyDataNumerical computingscipyAnalysisStatistical computations (skew, kurtosis, VaR)scikit-learnModellingRegression, clustering, cross-validationstatsmodelsModellingTime-series analysis, OLS, ARIMAProphetModellingTrend decomposition & forecastingmatplotlib, seabornVisualisationStatic publication-quality chartsPlotlyVisualisationInteractive charts with hover & zoomDashVisualisationWeb-based analytical dashboardStreamlitVisualisationLive parameter exploration appSQLiteStorageLightweight local data persistencePostgreSQLStorageProduction-grade relational data storeApache SparkScaleDistributed processing for large datasetsDockerDevOpsContainerised, reproducible environmentFastAPIAPIREST endpoints to serve model outputsTableauBIExecutive-level visual reportingJupyter NotebookEnvironmentInteractive analysis & prototypingGitVersion controlSource history & collaboration

Quick start
Option 1 — Jupyter notebook
bashgit clone https://github.com/YOUR_USERNAME/tesla-financial-data-analytics.git
cd tesla-financial-data-analytics
pip install -r requirements.txt
jupyter notebook tesla_analysis.ipynb
Option 2 — Streamlit app
bashpip install -r requirements.txt
streamlit run app.py
Option 3 — Docker
bashdocker build -t tesla-analytics .
docker run -p 8501:8501 tesla-analytics

No yfinance? The notebook automatically uses a realistic synthetic dataset so every cell executes without errors.


Authors
Harsh Parashar — Python, data wrangling, visualisation, Monte Carlo, dashboard
Kanishk Raj — Research & fundamental analysis
Abhishek Kashyap — Valuation & report writing
Supervised by Dr. Vijay Agarwal, Dept. of Management, BIT Mesra
BBA Final Year Project — Birla Institute of Technology, Mesra, Ranchi
