"""
Tesla Financial Analysis
========================
A comprehensive financial analysis script for Tesla (TSLA) covering:
  - Stock price history & returns
  - Moving averages & Bollinger Bands
  - RSI (Relative Strength Index)
  - Volume analysis
  - Revenue & earnings trend (hardcoded financials)
  - Monte Carlo simulation for price forecasting
  - Correlation heatmap

Requirements:
    pip install yfinance pandas numpy matplotlib seaborn scipy
"""

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from scipy import stats

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False
    print("yfinance not installed. Using synthetic data. Run: pip install yfinance")

# ── Configuration ──────────────────────────────────────────────────────────────
TICKER       = "TSLA"
START_DATE   = "2019-01-01"
END_DATE     = "2024-12-31"
MC_SIMULATIONS = 1000
MC_DAYS        = 252          # 1 trading year forecast

COLORS = {
    "primary":   "#E31937",   # Tesla red
    "secondary": "#1A1A1A",   # dark
    "accent":    "#5C6BC0",
    "positive":  "#26A69A",
    "negative":  "#EF5350",
    "neutral":   "#78909C",
}

plt.rcParams.update({
    "figure.facecolor": "#F8F9FA",
    "axes.facecolor":   "#FFFFFF",
    "axes.grid":        True,
    "grid.alpha":       0.3,
    "font.family":      "DejaVu Sans",
})


# ── 1. Data Loading ─────────────────────────────────────────────────────────────
def load_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Download historical OHLCV data from Yahoo Finance or generate synthetic data."""
    if YFINANCE_AVAILABLE:
        print(f"Downloading {ticker} data from Yahoo Finance...")
        df = yf.download(ticker, start=start, end=end, progress=False)
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
    else:
        print("Generating synthetic TSLA-like data...")
        dates = pd.date_range(start=start, end=end, freq="B")
        np.random.seed(42)
        n = len(dates)
        returns = np.random.normal(0.001, 0.035, n)
        price = 60.0 * np.exp(np.cumsum(returns))
        df = pd.DataFrame({
            "Open":   price * np.random.uniform(0.98, 1.00, n),
            "High":   price * np.random.uniform(1.00, 1.04, n),
            "Low":    price * np.random.uniform(0.96, 1.00, n),
            "Close":  price,
            "Volume": np.random.randint(50_000_000, 200_000_000, n).astype(float),
        }, index=dates)
    df = df.dropna()
    print(f"  Loaded {len(df)} trading days  ({df.index[0].date()} → {df.index[-1].date()})")
    return df


# ── 2. Technical Indicators ─────────────────────────────────────────────────────
def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Add SMA, EMA, Bollinger Bands, RSI, and daily return columns."""
    close = df["Close"]

    # Moving averages
    df["SMA_20"]  = close.rolling(20).mean()
    df["SMA_50"]  = close.rolling(50).mean()
    df["SMA_200"] = close.rolling(200).mean()
    df["EMA_12"]  = close.ewm(span=12, adjust=False).mean()
    df["EMA_26"]  = close.ewm(span=26, adjust=False).mean()
    df["MACD"]    = df["EMA_12"] - df["EMA_26"]
    df["Signal"]  = df["MACD"].ewm(span=9, adjust=False).mean()

    # Bollinger Bands (20-day, ±2σ)
    df["BB_Mid"]   = close.rolling(20).mean()
    df["BB_Std"]   = close.rolling(20).std()
    df["BB_Upper"] = df["BB_Mid"] + 2 * df["BB_Std"]
    df["BB_Lower"] = df["BB_Mid"] - 2 * df["BB_Std"]

    # RSI (14-day)
    delta = close.diff()
    gain  = delta.clip(lower=0).rolling(14).mean()
    loss  = (-delta.clip(upper=0)).rolling(14).mean()
    rs    = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # Returns
    df["Daily_Return"] = close.pct_change()
    df["Cum_Return"]   = (1 + df["Daily_Return"]).cumprod() - 1
    df["Log_Return"]   = np.log(close / close.shift(1))

    # Rolling volatility (30-day annualised)
    df["Volatility_30"] = df["Daily_Return"].rolling(30).std() * np.sqrt(252)

    return df


# ── 3. Tesla Annual Financials (hardcoded from SEC / earnings reports) ──────────
def get_annual_financials() -> pd.DataFrame:
    """Return Tesla annual financial highlights (2018-2023)."""
    data = {
        "Year":          [2018,  2019,  2020,  2021,   2022,   2023],
        "Revenue_B":     [21.46, 24.58, 31.54, 53.82,  81.46,  96.77],
        "GrossProfit_B": [4.46,  4.07,  6.63,  13.66,  20.85,  17.66],
        "NetIncome_B":   [-0.98, -0.86, 0.72,  5.52,   12.56,  14.99],
        "FreeCashFlow_B":[[-1.0, -1.0,  2.79,  4.98,   7.57,   4.36]][0],
        "GrossMargin_Pct":[20.8, 16.6,  21.0,  25.4,   25.6,   18.2],
        "Deliveries_K":  [245,   367,   500,   936,    1314,   1809],
    }
    return pd.DataFrame(data)


# ── 4. Monte Carlo Simulation ───────────────────────────────────────────────────
def monte_carlo(df: pd.DataFrame, simulations: int = 1000, days: int = 252):
    """GBM-based Monte Carlo price simulation."""
    log_returns = df["Log_Return"].dropna()
    mu    = log_returns.mean()
    sigma = log_returns.std()
    last  = float(df["Close"].iloc[-1])

    dt      = 1
    results = np.zeros((days, simulations))
    for s in range(simulations):
        prices = [last]
        for _ in range(days - 1):
            shock = np.random.normal(mu * dt, sigma * np.sqrt(dt))
            prices.append(prices[-1] * np.exp(shock))
        results[:, s] = prices

    return results


# ── 5. Plotting ─────────────────────────────────────────────────────────────────
def plot_price_and_indicators(df: pd.DataFrame):
    fig = plt.figure(figsize=(16, 14))
    fig.suptitle("Tesla (TSLA) – Technical Analysis Dashboard", fontsize=18,
                 fontweight="bold", color=COLORS["secondary"], y=0.98)
    gs = gridspec.GridSpec(4, 1, figure=fig, hspace=0.05,
                           height_ratios=[3, 1, 1, 1])

    # ── Price + Bollinger + SMAs ──
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(df.index, df["Close"],    color=COLORS["primary"],   lw=1.5, label="Close")
    ax1.plot(df.index, df["SMA_20"],   color=COLORS["accent"],    lw=1.0, linestyle="--", label="SMA 20")
    ax1.plot(df.index, df["SMA_50"],   color="orange",            lw=1.0, linestyle="--", label="SMA 50")
    ax1.plot(df.index, df["SMA_200"],  color="purple",            lw=1.0, linestyle="--", label="SMA 200")
    ax1.fill_between(df.index, df["BB_Upper"], df["BB_Lower"],
                     alpha=0.08, color=COLORS["accent"], label="Bollinger Bands")
    ax1.plot(df.index, df["BB_Upper"], color=COLORS["accent"], lw=0.6, linestyle=":")
    ax1.plot(df.index, df["BB_Lower"], color=COLORS["accent"], lw=0.6, linestyle=":")
    ax1.set_ylabel("Price (USD)", fontweight="bold")
    ax1.legend(loc="upper left", fontsize=8, ncol=3)
    ax1.set_xticklabels([])

    # ── Volume ──
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    colors_vol = [COLORS["positive"] if r >= 0 else COLORS["negative"]
                  for r in df["Daily_Return"].fillna(0)]
    ax2.bar(df.index, df["Volume"] / 1e6, color=colors_vol, alpha=0.7, width=1)
    ax2.set_ylabel("Volume (M)", fontweight="bold")
    ax2.set_xticklabels([])

    # ── RSI ──
    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    ax3.plot(df.index, df["RSI"], color=COLORS["accent"], lw=1.2)
    ax3.axhline(70, color=COLORS["negative"], linestyle="--", lw=0.8, alpha=0.8)
    ax3.axhline(30, color=COLORS["positive"], linestyle="--", lw=0.8, alpha=0.8)
    ax3.fill_between(df.index, df["RSI"], 70,
                     where=(df["RSI"] >= 70), alpha=0.2, color=COLORS["negative"])
    ax3.fill_between(df.index, df["RSI"], 30,
                     where=(df["RSI"] <= 30), alpha=0.2, color=COLORS["positive"])
    ax3.set_ylim(0, 100)
    ax3.set_ylabel("RSI (14)", fontweight="bold")
    ax3.set_xticklabels([])

    # ── MACD ──
    ax4 = fig.add_subplot(gs[3], sharex=ax1)
    ax4.plot(df.index, df["MACD"],   color=COLORS["primary"], lw=1.2, label="MACD")
    ax4.plot(df.index, df["Signal"], color="orange",           lw=1.0, linestyle="--", label="Signal")
    macd_hist = df["MACD"] - df["Signal"]
    ax4.bar(df.index, macd_hist,
            color=[COLORS["positive"] if v >= 0 else COLORS["negative"] for v in macd_hist.fillna(0)],
            alpha=0.5, width=1)
    ax4.axhline(0, color="black", lw=0.5)
    ax4.set_ylabel("MACD", fontweight="bold")
    ax4.legend(loc="upper left", fontsize=8)

    plt.savefig("/mnt/user-data/outputs/01_technical_analysis.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  Saved: 01_technical_analysis.png")


def plot_returns_distribution(df: pd.DataFrame):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle("Tesla – Returns & Risk Analysis", fontsize=15,
                 fontweight="bold", color=COLORS["secondary"])

    # Daily return histogram
    ax = axes[0]
    returns = df["Daily_Return"].dropna()
    ax.hist(returns, bins=80, color=COLORS["primary"], alpha=0.7, edgecolor="white", lw=0.3)
    mu, std = returns.mean(), returns.std()
    x = np.linspace(returns.min(), returns.max(), 200)
    ax.plot(x, stats.norm.pdf(x, mu, std) * len(returns) * (returns.max()-returns.min()) / 80,
            color=COLORS["secondary"], lw=1.5, label=f"Normal fit\nμ={mu:.4f}, σ={std:.4f}")
    ax.set_title("Daily Return Distribution", fontweight="bold")
    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")
    ax.legend(fontsize=8)

    # Cumulative return
    ax = axes[1]
    ax.plot(df.index, df["Cum_Return"] * 100, color=COLORS["primary"], lw=1.5)
    ax.fill_between(df.index, df["Cum_Return"] * 100, alpha=0.15, color=COLORS["primary"])
    ax.axhline(0, color="black", lw=0.5)
    ax.set_title("Cumulative Return (%)", fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Return (%)")

    # Rolling volatility
    ax = axes[2]
    ax.plot(df.index, df["Volatility_30"] * 100, color=COLORS["accent"], lw=1.2)
    ax.fill_between(df.index, df["Volatility_30"] * 100, alpha=0.15, color=COLORS["accent"])
    ax.set_title("30-Day Rolling Volatility (Ann.)", fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volatility (%)")

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/02_returns_risk.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  Saved: 02_returns_risk.png")


def plot_financials(fin: pd.DataFrame):
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    fig.suptitle("Tesla – Annual Financial Highlights", fontsize=15,
                 fontweight="bold", color=COLORS["secondary"])

    metrics = [
        ("Revenue_B",      "Revenue ($ Billion)",        COLORS["primary"]),
        ("GrossProfit_B",  "Gross Profit ($ Billion)",   COLORS["accent"]),
        ("NetIncome_B",    "Net Income ($ Billion)",      COLORS["positive"]),
        ("FreeCashFlow_B", "Free Cash Flow ($ Billion)",  "orange"),
        ("GrossMargin_Pct","Gross Margin (%)",             "purple"),
        ("Deliveries_K",   "Vehicle Deliveries (000s)",   COLORS["negative"]),
    ]

    for ax, (col, title, color) in zip(axes.flat, metrics):
        values = fin[col]
        bar_colors = [COLORS["positive"] if v >= 0 else COLORS["negative"] for v in values]
        ax.bar(fin["Year"], values, color=bar_colors if col in ("NetIncome_B", "FreeCashFlow_B") else color,
               alpha=0.85, edgecolor="white", linewidth=0.5)
        for i, (year, val) in enumerate(zip(fin["Year"], values)):
            ax.text(year, val + (abs(val) * 0.03), f"{val:.1f}", ha="center",
                    va="bottom" if val >= 0 else "top", fontsize=8, fontweight="bold")
        ax.set_title(title, fontweight="bold")
        ax.set_xlabel("Year")
        ax.axhline(0, color="black", lw=0.5)

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/03_financials.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  Saved: 03_financials.png")


def plot_monte_carlo(df: pd.DataFrame, results: np.ndarray):
    last_price  = float(df["Close"].iloc[-1])
    final_prices = results[-1, :]
    p5, p50, p95 = np.percentile(final_prices, [5, 50, 95])

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle("Tesla – Monte Carlo Price Simulation (1-Year Forecast)",
                 fontsize=15, fontweight="bold", color=COLORS["secondary"])

    # Simulation paths
    ax = axes[0]
    days_x = np.arange(results.shape[0])
    for i in range(min(200, results.shape[1])):
        ax.plot(days_x, results[:, i], alpha=0.05, color=COLORS["primary"], lw=0.5)
    ax.plot(days_x, np.percentile(results, 95, axis=1), color=COLORS["positive"],
            lw=2, linestyle="--", label="95th pct")
    ax.plot(days_x, np.percentile(results, 50, axis=1), color=COLORS["secondary"],
            lw=2, label="Median")
    ax.plot(days_x, np.percentile(results,  5, axis=1), color=COLORS["negative"],
            lw=2, linestyle="--", label="5th pct")
    ax.axhline(last_price, color="black", lw=1, linestyle=":", label=f"Current ${last_price:.2f}")
    ax.set_xlabel("Trading Days")
    ax.set_ylabel("Simulated Price (USD)")
    ax.set_title(f"{MC_SIMULATIONS:,} Simulations", fontweight="bold")
    ax.legend(fontsize=9)

    # Final price distribution
    ax = axes[1]
    ax.hist(final_prices, bins=60, color=COLORS["primary"], alpha=0.75,
            edgecolor="white", lw=0.3)
    ax.axvline(p5,  color=COLORS["negative"], lw=2, linestyle="--", label=f"5th pct  ${p5:.2f}")
    ax.axvline(p50, color=COLORS["secondary"],lw=2, label=f"Median   ${p50:.2f}")
    ax.axvline(p95, color=COLORS["positive"], lw=2, linestyle="--", label=f"95th pct ${p95:.2f}")
    ax.axvline(last_price, color="black", lw=1.5, linestyle=":", label=f"Current  ${last_price:.2f}")
    ax.set_xlabel("Price (USD)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Simulated Final Prices", fontweight="bold")
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/04_monte_carlo.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("  Saved: 04_monte_carlo.png")
    return p5, p50, p95


def plot_summary_stats(df: pd.DataFrame, mc_p5, mc_p50, mc_p95):
    """Print and visualise a key-metrics summary card."""
    returns       = df["Daily_Return"].dropna()
    annual_return = (1 + returns.mean()) ** 252 - 1
    annual_vol    = returns.std() * np.sqrt(252)
    sharpe        = annual_return / annual_vol
    max_dd        = ((df["Close"] / df["Close"].cummax()) - 1).min()
    last_price    = float(df["Close"].iloc[-1])

    metrics = {
        "Current Price":         f"${last_price:,.2f}",
        "Period High":           f"${df['High'].max():,.2f}",
        "Period Low":            f"${df['Low'].min():,.2f}",
        "Total Return":          f"{df['Cum_Return'].iloc[-1]*100:.1f}%",
        "Annual Return (CAGR)":  f"{annual_return*100:.1f}%",
        "Annual Volatility":     f"{annual_vol*100:.1f}%",
        "Sharpe Ratio":          f"{sharpe:.2f}",
        "Max Drawdown":          f"{max_dd*100:.1f}%",
        "MC Bear (5th pct)":     f"${mc_p5:,.2f}",
        "MC Base (Median)":      f"${mc_p50:,.2f}",
        "MC Bull (95th pct)":    f"${mc_p95:,.2f}",
    }

    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor("#1A1A1A")
    ax.set_facecolor("#1A1A1A")
    ax.axis("off")
    ax.set_title("Tesla (TSLA) – Key Metrics Summary", fontsize=14,
                 fontweight="bold", color="white", pad=15)

    y = 0.95
    for key, val in metrics.items():
        color = "white"
        if "%" in val:
            num = float(val.replace("%", "").replace(",", ""))
            color = COLORS["positive"] if num > 0 else (COLORS["negative"] if num < 0 else "white")
        ax.text(0.05, y, key + ":",  transform=ax.transAxes,
                fontsize=11, color="#AAAAAA", va="top")
        ax.text(0.60, y, val,        transform=ax.transAxes,
                fontsize=11, color=color, va="top", fontweight="bold")
        y -= 0.082

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/05_summary.png", dpi=150, bbox_inches="tight",
                facecolor="#1A1A1A")
    plt.close()
    print("  Saved: 05_summary.png")

    # Also print to console
    print("\n" + "═"*45)
    print("  TESLA (TSLA) — KEY METRICS SUMMARY")
    print("═"*45)
    for k, v in metrics.items():
        print(f"  {k:<28} {v}")
    print("═"*45)


# ── Main ────────────────────────────────────────────────────────────────────────
def main():
    print("\n" + "="*55)
    print("  TESLA FINANCIAL ANALYSIS")
    print("="*55)

    # 1. Load & enrich data
    df  = load_stock_data(TICKER, START_DATE, END_DATE)
    df  = add_indicators(df)
    fin = get_annual_financials()

    # 2. Monte Carlo
    print("\nRunning Monte Carlo simulation...")
    mc_results = monte_carlo(df, MC_SIMULATIONS, MC_DAYS)

    # 3. Charts
    print("\nGenerating charts...")
    plot_price_and_indicators(df)
    plot_returns_distribution(df)
    plot_financials(fin)
    p5, p50, p95 = plot_monte_carlo(df, mc_results)
    plot_summary_stats(df, p5, p50, p95)

    print("\n✅ Analysis complete. All charts saved to outputs/")


if __name__ == "__main__":
    main()
