import matplotlib.pyplot as plt
import numpy as np
from house_data import fetch_price_data
from matplotlib.ticker import FuncFormatter

prices = fetch_price_data()
if prices is None:
    print("No location data to cluster.")
else: 
    prices_float = [float(price) for price in prices]
    fig, ax = plt.subplots()
    ax.boxplot(prices_float)

    def currency_formatter(x,pos):
        if x >= 1e6:
            return f'${x/1e6:.1f}M'
        elif x >= 1e3:
            return f'${x/1e3:.0f}K'
        else:
            return f'${x:.0f}'
    
    ax.yaxis.set_major_formatter(FuncFormatter(currency_formatter))
    
    plt.title("Boxplot of House Prices")
    plt.ylabel("Price")
    plt.show()
