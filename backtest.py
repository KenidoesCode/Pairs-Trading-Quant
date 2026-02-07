import pandas as pd

def backtest_strategy(ko, pep, beta, signals):
    returns_ko = ko.pct_change()
    returns_pep = pep.pct_change()

    spread_returns = returns_ko - beta * returns_pep

    strategy_returns = signals["position"].shift(1) * spread_returns

    cumulative_returns = (1 + strategy_returns).cumprod()

    return strategy_returns, cumulative_returns
