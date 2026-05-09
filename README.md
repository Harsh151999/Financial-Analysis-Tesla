# Financial Analysis [Tesla, Inc. (TSLA) (2012–2020)]

#Tesla-financial-data-analytics/
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

# Jupyter notebook
git clone https://github.com/YOUR_USERNAME/tesla-financial-data-analytics.git
cd tesla-financial-data-analytics
pip install -r requirements.txt
jupyter notebook tesla_analysis.ipynb


# Streamlit app
bashpip install -r requirements.txt
streamlit run app.py
Option 3 — Docker
bashdocker build -t tesla-analytics .
docker run -p 8501:8501 tesla-analytics

No yfinance? The notebook automatically uses a realistic synthetic dataset so every cell executes without errors.


#Authors

Harsh Parashar — Python, data wrangling, visualisation, Monte Carlo, dashboard
Kanishk Raj — Research & fundamental analysis
Abhishek Kashyap — Valuation & report writing
Supervised by Dr. Vijay Agarwal, Dept. of Management, BIT Mesra
BBA Final Year Project — Birla Institute of Technology, Mesra, Ranchi
