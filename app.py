import streamlit as st
import matplotlib.pyplot as plt

from data import get_data
from strategy import check_cointegration
from strategy import calculate_beta, calculate_spread, calculate_zscore
from strategy import generate_signals
from backtest import backtest_strategy

st.title("Pairs Trading – Data Check")

ko = get_data("KO")
pep = get_data("PEP")

st.subheader("Coca-Cola (KO)")
st.write(ko.head())

st.subheader("Pepsi (PEP)")
st.write(pep.head())


p_value = check_cointegration(ko, pep)

st.subheader("Spread & Z-Score")

beta = calculate_beta(ko, pep)
st.write(f"Beta (hedge ratio): {beta:.4f}")

spread = calculate_spread(ko, pep, beta)
z_score = calculate_zscore(spread)

st.write("Latest Z-score:", z_score.dropna().iloc[-1])

signals = generate_signals(z_score)

strategy_returns, cumulative_returns = backtest_strategy(
    ko, pep, beta, signals
)

st.subheader("Backtest Results")
fig, ax = plt.subplots()
ax.plot(z_score.index, z_score, label="Z-score")
ax.axhline(2, color="red", linestyle="--")
ax.axhline(-2, color="green", linestyle="--")
ax.axhline(0, color="black", linestyle="-")
ax.legend()
st.write("Final cumulative return:", cumulative_returns.dropna().iloc[-1])

st.subheader("Z-Score Plot")
st.subheader("Equity Curve")

fig2, ax2 = plt.subplots()
ax2.plot(cumulative_returns.index, cumulative_returns, label="Strategy Equity")
ax2.legend()

st.pyplot(fig2)




st.pyplot(fig)

st.subheader("Cointegration Test Result")
st.write(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    st.success("Stocks are cointegrated ✅")
else:
    st.error("Stocks are NOT cointegrated ❌")
