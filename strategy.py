import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint


def check_cointegration(series1, series2):
    score, p_value, _ = coint(series1, series2)
    return p_value


def calculate_beta(series1, series2):
    beta = np.polyfit(series2, series1, 1)[0]
    return beta


def calculate_spread(series1, series2, beta):
    spread = series1 - beta * series2
    return spread


def calculate_zscore(spread, window=30):
    mean = spread.rolling(window).mean()
    std = spread.rolling(window).std()
    z_score = (spread - mean) / std
    return z_score


def generate_signals(z_score, entry_threshold=2, exit_threshold=0):
    signals = pd.DataFrame(index=z_score.index)
    signals["position"] = 0

    signals.loc[z_score > entry_threshold, "position"] = -1
    signals.loc[z_score < -entry_threshold, "position"] = 1
    signals.loc[abs(z_score) < exit_threshold, "position"] = 0

    return signals
