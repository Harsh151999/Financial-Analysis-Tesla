# Financial Analysis-Tesla

# Tesla, Inc. — Interactive Financial Dashboard (2012–2020)

**BBA Final Project | Department of Management, BIT Mesra, Ranchi**  
Submitted by: Kanishk Raj · Abhishek Kashyap · Harsh Parashar  
Supervised by: Dr. Vijay Agarwal  

---

## Overview

This project delivers an interactive financial dashboard visualising Tesla, Inc.'s performance from 2012 to 2020, built from Tesla's official 10-K SEC filings. It covers revenue growth, profitability, vehicle deliveries, R&D investment, cash flow, and peer valuation comparisons.

---

## Files

| File | Description |
|------|-------------|
| `Tesla_Dashboard.html` | Standalone browser dashboard — open directly, no install needed |
| `Tesla_Dashboard.ipynb` | Jupyter notebook with full Plotly charts, styled tables, and analysis |
| `Tesla_Final_Complete_docx.pdf` | Source report (BBA Final Project) |

---

## Quick Start

### Option 1 — HTML (easiest)
Just open `Tesla_Dashboard.html` in any browser. No Python, no server, no internet connection required. All chart libraries are bundled inside.

### Option 2 — Jupyter Notebook

**Requirements**
- Python 3.8+
- pip

**Install dependencies**
```bash
pip install plotly pandas jupyter
```

**Run**
```bash
jupyter notebook Tesla_Dashboard.ipynb
```
Or open in VS Code with the Jupyter extension, or upload to [Google Colab](https://colab.research.google.com).

---

## Dashboard Tabs

| Tab | Charts |
|-----|--------|
| Revenue & Profit | Grouped bar (revenue vs gross profit) + gross margin % line |
| Net Income | Colour-coded bar with milestone annotations |
| Cash Flow & PP&E | Operating cash flow + Gigafactory PP&E build-out |
| R&D | R&D spend (bar) + R&D as % of revenue (line, dual axis) |
| Deliveries | Stacked bar by model (S/X vs 3/Y) |
| 2020 Mix | Donut charts — revenue breakdown & cost structure |
| Valuation | Horizontal bar — EV/EBITDA vs Ford, GM, Volkswagen |

---

## Data Sources

All data sourced from Tesla's official SEC filings:

- Tesla 10-K Annual Reports (2012–2020) — [sec.gov](https://sec.gov)
- Tesla Investor Relations — [ir.tesla.com](https://ir.tesla.com)
- IEA Global EV Outlook 2021
- BloombergNEF Electric Vehicle Outlook 2020

---

## Key Findings

- Revenue grew **76×** from $413M (2012) to $31.54B (2020)
- First full-year **GAAP profit** achieved in 2020 ($690M net income)
- **$1.6B** in regulatory credit sales was critical to 2020 profitability
- Vehicle deliveries scaled from **2,650** (2012) to **499,550** (2020)
- Operating cash flow swung from **−$524M** (2015) to **+$5.94B** (2020)
- Market cap surged from $78B to ~**$700B** in 2020 alone (700%+)
- Tesla traded at **157× EV/EBITDA** vs 12–37× for traditional peers

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Data processing |
| Pandas | Data wrangling |
| Plotly | Interactive charts (notebook) |
| Chart.js | Interactive charts (HTML dashboard) |
| Jupyter | Notebook environment |

---

## License

Academic project — for educational and non-commercial use only.
