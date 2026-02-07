# 📈 Pairs Trading Strategy — Statistical Arbitrage in Python

A complete end-to-end implementation of a **pairs trading (statistical arbitrage)** strategy using real market data, hypothesis testing, and backtesting.

This project focuses on **exploiting mean reversion between two cointegrated stocks** instead of predicting future prices.

---

## 🚀 Why This Project Matters

Most beginner trading projects:
- Try to **predict stock prices** ❌  
- Rely on indicators or ML hype ❌  
- Ignore statistical validation ❌  

This project takes a **professional quant approach**:
- ✅ Uses **statistical relationships**, not predictions  
- ✅ Validates assumptions with **hypothesis testing**  
- ✅ Implements a **market-neutral long/short strategy**  
- ✅ Backtests realistically to avoid false confidence  

This is how **real quantitative strategies are researched**.

---

## 🧠 Core Idea (Intuition)

Two stocks from the same sector often move together in the long run.

Occasionally, they **temporarily diverge** due to noise, sentiment, or short-term imbalance.

📌 The strategy:
- Identifies **statistically linked stocks**
- Measures how far their relationship deviates from normal
- Trades the **reversion back to equilibrium**

> We do not predict direction.  
> We trade **relative mispricing**.

---

## 📊 Trading Rules

| Condition | Action |
|--------|--------|
| Z-score > +2 | 🔴 Short KO, 🟢 Long PEP |
| Z-score < −2 | 🟢 Long KO, 🔴 Short PEP |
| Z-score → 0 | ⚪ Exit positions |

📌 This is a **market-neutral strategy** — overall market direction is irrelevant.

---

## 🧮 Backtesting Logic

- Daily returns calculated for both stocks
- Spread returns computed using hedge ratio
- Signals are **shifted forward** to avoid look-ahead bias
- Strategy performance tracked via **cumulative returns**

📈 Results are visualized using:
- Z-score plots with entry/exit bands
- Equity curve showing strategy growth over time

---

## 🛠️ Tech Stack

- **Python**
- `pandas`, `numpy`
- `statsmodels` (cointegration testing)
- `matplotlib`
- `streamlit`
- `yfinance`

---

## 👥 Who Can Use This Project?

This project is useful for:
- 📊 Aspiring **Quantitative Analysts**
- 💻 Finance + Data Science learners
- 📈 Trading & market microstructure enthusiasts
- 🎓 Students exploring real-world statistical strategies
- 🧠 Anyone wanting to understand **how quant funds think**

---

## ⚠️ Limitations & Future Work

- Cointegration can break during regime changes
- Transaction costs are not included
- Beta is static (can be made rolling)
- Strategy tested on only one pair

🔮 Possible extensions:
- Rolling cointegration tests
- Transaction cost modeling
- Multi-pair portfolio
- Live paper trading
- Risk metrics (Sharpe, drawdown)

---

## 📌 Key Takeaway

> Markets are noisy, but **relationships are structured**.

This project demonstrates how:
- Statistical assumptions are validated
- Trading rules are formalized
- Strategies are tested *before* risking capital

---

## 📎 Disclaimer

This project is for **educational purposes only**.  
It does not constitute financial advice.  
Past performance does not guarantee future results.

---

⭐ If you found this useful, consider starring the repository.