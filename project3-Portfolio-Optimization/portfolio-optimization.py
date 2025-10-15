import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dat = pd.read_csv('/content/modified_stock_data.csv')
dat

dat = dat[['Date','Adj Close_AAPL','Adj Close_AMZN','Adj Close_META','Adj Close_TSLA','Volume_AAPL','Volume_AMZN','Volume_META','Volume_TSLA']]
print(dat)

dat.isnull().sum()

dat.describe()

"""**Visualization of Volume Trends Over Days**"""

dat.loc[:, 'Date'] = pd.to_datetime(dat['Date']) # updates date columns in proper date format with date, month and year
# Plotting for the first  dates
first_dates = dat[(dat['Date'] >= pd.to_datetime('2021-08-20')) & (dat['Date'] <= pd.to_datetime('2021-08-28'))]

plt.figure(figsize=(8, 6))
for column in ['Volume_AAPL', 'Volume_AMZN', 'Volume_META', 'Volume_TSLA']:
    plt.plot(first_dates['Date'], first_dates[column], label=column.replace('Volume_', ''), linewidth=2)

plt.xlabel('Date', fontsize=12)
plt.ylabel('Volumes', fontsize=12)
plt.title('Stock Volumes Over Days', fontsize=14)
plt.legend(fontsize=12) # Identify each stocks name
plt.grid(True, linestyle='--', alpha=0.7) # Gridlines with dashed lines and slightly transparent lines making the plot easier to read and visualize
plt.xticks(rotation=45, ha='right') # rotate axis labels
plt.tight_layout() # adjust spacing to prevent overlapping of elements
plt.show()

"""**Visualization of Volume Trends over weeks**"""

dat.loc[:, 'Date'] = pd.to_datetime(dat['Date'])

week_data = dat[(dat['Date'] >= pd.to_datetime('2020-11-20')) & (dat['Date'] <= pd.to_datetime('2021-01-01'))]

# Plotting
plt.figure(figsize=(8, 6))
for column in ['Volume_AAPL', 'Volume_AMZN', 'Volume_META', 'Volume_TSLA']:
    plt.plot(week_data['Date'], week_data[column], label=column.replace('Volume_', ''), linewidth=2)

# Customize the plot
plt.xlabel('Date', fontsize=12)
plt.ylabel('Volumes', fontsize=12)
plt.title('Stock Volumes for Weeks', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""**Visualization of Volume Trends Across Months**"""

month_data = dat[(dat['Date'] >= pd.to_datetime('2020-11-20')) & (dat['Date'] <= pd.to_datetime('2021-04-20'))]

# Plotting
plt.figure(figsize=(8, 6))
for column in ['Volume_AAPL', 'Volume_AMZN', 'Volume_META', 'Volume_TSLA']:
    plt.plot(month_data['Date'], month_data[column], label=column.replace('Volume_', ''), linewidth=2)

# Customize the plot
plt.xlabel('Date', fontsize=12)
plt.ylabel('Volumes', fontsize=12)
plt.title('Volumes of Stocks for Month', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""Visualization of Volumes Trends across a Year"""

# Filter data for the year 2020
year_data = dat[(dat['Date'] >= pd.to_datetime('2021-01-01')) & (dat['Date'] <= pd.to_datetime('2021-12-31'))]

# Plotting
plt.figure(figsize=(10, 6))  # Slightly increase figure size for clarity
for column in ['Volume_AAPL', 'Volume_AMZN', 'Volume_META', 'Volume_TSLA']:
    plt.plot(year_data['Date'], year_data[column], label=column.replace('Volume_', ''), linewidth=2)

# Customize the plot
plt.xlabel('Date', fontsize=12)
plt.ylabel('Volumes', fontsize=12)
plt.title('Stock Volumes in Year', fontsize=14)  # Update title for clarity
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""**Visualization of Volume Trends Over the Years**"""

dat.loc[:, 'Date'] = pd.to_datetime(dat['Date'])  # updates date columns in proper date format with  year

# Plotting
plt.figure(figsize=(8, 6))
# Iterate through columns to plot each stock's adjusted close price
for column in ['Volume_AAPL', 'Volume_AMZN', 'Volume_META', 'Volume_TSLA']:
    plt.plot(dat['Date'], dat[column], label=column.replace('Volume_', ''), linewidth=2)

# Customize the plot
plt.xlabel('Date', fontsize=12)
plt.ylabel('Volumes', fontsize=12)
plt.title('Volumes of Stocks for Years', fontsize=14)
plt.legend(fontsize=12)  # # Identify each stocks name
plt.grid(True, linestyle='--', alpha=0.7)  # Gridlines with dashed lines and slightly transparent lines making the plot easier to read and visualize
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better visibility
plt.tight_layout() # adjust spacing to prevent overlapping of elements
# Show the plot
plt.show()

"""**Visualization of Adjusted Close Trends price Over dates**"""

dat.loc[:, 'Date'] = pd.to_datetime(dat['Date']) # updates date columns in proper date format with date, month and year
# Plotting for the first  dates
first_dates = dat[(dat['Date'] >= pd.to_datetime('2021-08-20')) & (dat['Date'] <= pd.to_datetime('2021-08-28'))]

plt.figure(figsize=(8, 6))
for column in ['Adj Close_AAPL', 'Adj Close_AMZN', 'Adj Close_META', 'Adj Close_TSLA']:
    plt.plot(first_dates['Date'], first_dates[column], label=column.replace('Adj Close_', ''), linewidth=2)

plt.xlabel('Date', fontsize=12)
plt.ylabel('Adjusted Close Price', fontsize=12)
plt.title('Adjusted Close Prices of Stocks for Days', fontsize=14)
plt.legend(fontsize=16) # Identify each stocks name
plt.grid(True, linestyle='--', alpha=0.7)  # Gridlines with dashed lines and slightly transparent lines making the plot easier to read and visualize
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""**Visualization of Adjusted Close Trends price Over weeks**"""

dat.loc[:, 'Date'] = pd.to_datetime(dat['Date'])

week_data = dat[(dat['Date'] >= pd.to_datetime('2020-11-20')) & (dat['Date'] <= pd.to_datetime('2021-01-01'))]

# Plotting
plt.figure(figsize=(8, 6))
for column in ['Adj Close_AAPL', 'Adj Close_AMZN', 'Adj Close_META', 'Adj Close_TSLA']:
    plt.plot(week_data['Date'], week_data[column], label=column.replace('Adj Close_', ''), linewidth=2)

# Customize the plot
plt.xlabel('Date', fontsize=12)
plt.ylabel('Adjusted Close Price', fontsize=12)
plt.title('Weekly Adjusted Close Prices of Stocks', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""**Visualization of Adjusted Close Trends price Over months**"""

one_month_data = dat[(dat['Date'] >= pd.to_datetime('2020-11-20')) & (dat['Date'] <= pd.to_datetime('2021-04-20'))]

# Plotting
plt.figure(figsize=(8, 6))
for column in ['Adj Close_AAPL', 'Adj Close_AMZN', 'Adj Close_META', 'Adj Close_TSLA']:
    plt.plot(one_month_data['Date'], one_month_data[column], label=column.replace('Adj Close_', ''), linewidth=2)

# Customize the plot
plt.xlabel('Date', fontsize=12)
plt.ylabel('Adjusted Close Price', fontsize=12)
plt.title('Adjusted Close Price of Stocks for Month', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""Visualization of Adjusted Close Price Over a Year"""

# Filter data for the year 2020
year_data = dat[(dat['Date'] >= pd.to_datetime('2021-01-01')) & (dat['Date'] <= pd.to_datetime('2021-12-31'))]

# Plotting
plt.figure(figsize=(10, 6))  # Slightly increase figure size for clarity
for column in ['Adj Close_AAPL', 'Adj Close_AMZN', 'Adj Close_META', 'Adj Close_TSLA']:
    plt.plot(year_data['Date'], year_data[column], label=column.replace('Volume_', ''), linewidth=2)

# Customize the plot
plt.xlabel('Date', fontsize=12)
plt.ylabel('Adjusted Close Price', fontsize=12)
plt.title('Adjusted Close Price Stock in Year', fontsize=14)  # Update title for clarity
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""**Visualization of Adjusted Close Trends price Over years**"""

dat.loc[:, 'Date'] = pd.to_datetime(dat['Date']) # updates date columns in proper date format with year

# Plotting
plt.figure(figsize=(8, 6))

# Iterate through columns to plot each stock's adjusted close price
for column in ['Adj Close_AAPL', 'Adj Close_AMZN', 'Adj Close_META', 'Adj Close_TSLA']:
    plt.plot(dat['Date'], dat[column], label=column.replace('Adj Close_', ''), linewidth=2)

# Customize the plot
plt.xlabel('Date', fontsize=12)
plt.ylabel('Adjusted Close Price', fontsize=12)
plt.title('Adjusted Closing Prices of Stocks for the Years', fontsize=14)
plt.legend(fontsize=10)  # Identify each stocks name
plt.grid(True, linestyle='--', alpha=0.7)  # Gridlines with dashed lines and slightly transparent lines making the plot easier to read and visualize
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better visibility
plt.tight_layout() # Adjust layout to prevent labels from overlapping
# Show the plot
plt.show()

"""**Total Price of each asset**, \( P_t \) is given by:

$$
P_t = \sum_{i=1}^{n} P_i \quad \text{where} \quad i = 1, 2, \dots, 1257 , Pi(Price).
$$

**Total Customers of each asset**, \( V_t \) is given by:

$$
V_t = \sum_{i=1}^{n} V_i \quad \text{where} \quad i = 1, 2, \dots, 1257.
$$

"""

# List of stock columns
stocks = ['Adj Close_AAPL', 'Adj Close_AMZN', 'Adj Close_META', 'Adj Close_TSLA']

# Loop through each stock and calculate the total price
for stock in stocks:
    total_price = dat[stock].sum()  # Use the built-in sum() function
    print(f"Total {stock.split('_')[1]} price:", total_price)

# List of volume columns
shares = ['Volume_AAPL', 'Volume_AMZN', 'Volume_META', 'Volume_TSLA']

# Loop through each volume column and calculate the total volume
for stock in shares:
    total_volume = dat[stock].sum()  # Use the built-in sum() function
    print(f"Total {stock.split('_')[1]} volume:", total_volume)

"""- **Vi**: Number of assets, where \( i = 1, 2, 3, 4 \)
- **Pi** : Total price of each asset, where \( i = 1, 2, 3, 4 \)

The total value is calculated as:
$$
\sum_{i=1}^{n} V_i \times P_i
$$
The weight \( **wi** \) of each asset is given by:
$$
w_i = \frac{V_i \times P_i}{\sum_{i=1}^{n} V_i \times P_i}
$$
Sum of weights $$w_1 + w_2 + w_3 + w_4 = 1$$

"""

# weights of each asserts
assets = ['AAPL','AMZN','META','TSLA']
total_price_company = np.array([148612.635, 15833.594, 290854.92, 208738.799])
total_share_company = np.array([131359892400, 98148890000, 29813773900, 168252488600])
weights = np.array([0.2475, 0.1973, 0.1099, 0.4453])

da = {'Assets':assets,'Total Price':total_price_company,'Total Volume':total_share_company,'Weight':weights }
df = pd.DataFrame(da)
print(df)

"""Returns of each adjusted close price
$$ \text{Return} = \frac{\text{adj_close}_{t1} - \text{adj_close}_{t0}}{\text{adj_close}_{t0}} $$

"""

# Calculate daily returns for each stock
dat1 = dat[['Adj Close_AAPL',	'Adj Close_AMZN',	'Adj Close_META',	'Adj Close_TSLA']]
returns = dat1.pct_change().dropna()

# Rename columns for clarity (optional)
returns.columns = ['AAPL', 'AMZN', 'META', 'TSLA']
print(returns)

"""### Average Returns of Each Asset
The mean return times 252 days is given by:

$$
\text{Mean_Return} = \left( \sum_{i=1}^{n} \text{Return}_i \right) \times \frac{1}{V_i}\times 252
$$

Where \( V_i = 1257 \), for, i = 1, 2,..., 1257.

"""

# The mean annual returns
returns.mean()*252

"""Covariance * weights * 252 days
$$
\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} \left( \text{Return1}_i - \overline{\text{Return1}} \right) \left( \text{Return2}_i - \overline{\text{Return2}} \right) \cdot w_i \times 252
$$


"""

cov_matrix = (returns.cov()*weights)*252
print(cov_matrix)

"""**Expected annual return**
$$ \text{Expected_Return} = \sum_{i=1}^{n} (\text{returns.mean()}_i \times \text{weights}_i) \times 252 $$

"""

# Calculation of the annual portfolio return
port_returns = np.sum(returns.mean()*weights)*252
port_returns

"""Variance of the returns
$$\sigma_p^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \sigma_{ij}$$

"""

# Calculation of the portfolio variance
port_var = np.dot(weights.T, np.dot(cov_matrix, weights))
port_var

# Calculation of portfoliio standard deviation
port_std = np.sqrt(port_var)
port_std

"""Sharpe Retion
$$S = \frac{R_p - R_f}{\sigma_p}$$

where:
- \( S \) is the Sharpe Ratio
- \( R_p \) is the expected portfolio return
- \( R_f \) is the risk-free rate
- \( sigma_p \) is the standard deviation of the portfolio’s excess return

"""

# Calculation of sharpe ratio
risk_free_rate = 0.0447
sharpe = (port_returns-risk_free_rate)/port_std
sharpe

# show the expected annual returns, standard deviation and variance
perc_std = round(port_std,3)
perc_var = round(port_var,3)
perc_returns = round(port_returns,3)
sharpe = round(sharpe,3)

print('Expected annual returns:',perc_returns)
print('Annual variance:',perc_var)
print('Annual standard deviation:',perc_std)
print('Sharpe ration:', sharpe)#In general a good sharpe ratio is higher than one indicating that portfolio return reflect the amount of risk by the manager. a ratio lower than one indicating that the portfolio risk is not optimal and reduce it performance even if the funds seems to beat the market.

"""# **Portfolio Optimization Model**"""

pip install pyportfolioopt

from pypfopt import expected_returns, risk_models

numer_dat = dat.select_dtypes(include='number')
numer_dat = numer_dat[['Adj Close_AAPL','Adj Close_AMZN','Adj Close_META','Adj Close_TSLA']]

# Calcute the expected returns
exp_return = expected_returns.mean_historical_return(numer_dat)
risk = risk_models.sample_cov(numer_dat)
exp_return

print(risk)

from pypfopt import EfficientFrontier, plotting

# Initialize Efficient Frontier
ef = EfficientFrontier(exp_return, risk)

# Plot the efficient frontier with random portfolios
fig, ax = plt.subplots(figsize=(8, 5))

# Generate random portfolios
n_samples = 50000
random_weights = np.random.dirichlet(np.ones(len(exp_return)), n_samples)
random_returns = random_weights.dot(exp_return)
random_risks = np.sqrt(np.einsum('ij,ij->i', random_weights @ risk, random_weights))

sharpe_ratios = random_returns / random_risks
scatter = ax.scatter(random_risks, random_returns, c=sharpe_ratios, cmap='viridis', alpha=0.5)
plt.colorbar(scatter, label='Sharpe Ratio')

# Plot the efficient frontier
plotting.plot_efficient_frontier(ef, ax=ax, show_assets=True)

# Maximize the Sharpe ratio
ef_sharpe = EfficientFrontier(exp_return, risk)
weights = ef_sharpe.max_sharpe()
cleaned_weights = ef_sharpe.clean_weights()
performance = ef_sharpe.portfolio_performance(verbose=True)

# Plot the maximum Sharpe ratio portfolio
ret_sharpe, vol_sharpe, _ = ef_sharpe.portfolio_performance()
ax.scatter(vol_sharpe, ret_sharpe, marker='*', color='r', s=100, label='Maximum Sharpe Ratio')

# Plot the minimum volatility portfolio
ef_min_vol = EfficientFrontier(exp_return, risk) # Create a separate instance for min_volatility
ef_min_vol.min_volatility()
ret_min_vol, vol_min_vol, _ = ef_min_vol.portfolio_performance()
ax.scatter(vol_min_vol, ret_min_vol, marker='*', color='g', s=100, label='Minimum Volatility')

# Format the plot
ax.set_title('Efficient Frontier')
ax.set_xlabel('Annualized Volatility')
ax.set_ylabel('Annualized Returns')
ax.legend()
plt.show()

# Print the weights
weights

from pypfopt import objective_functions
# initialize efficient frontier object
ef = EfficientFrontier(exp_return, risk)
# add objective function
ef.add_objective(objective_functions.L2_reg, gamma = 0.1)
# calculate weights
weights = ef.max_sharpe()
# print the cleaned weights
cleaned_weights = ef.clean_weights()
cleaned_weights

# discrete allocation
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

latest_prices = get_latest_prices(numer_dat)

da = DiscreteAllocation(cleaned_weights, latest_prices, total_portfolio_value=50000)
allocation, leftover = da.lp_portfolio()

# Calculate the total amount for 'Adj Close_AAPL', 'Adj Close_META', and 'Adj Close_TSLA'
total_amount_aapl = 0
total_amount_meta = 0
total_amount_tsla = 0

for asset, quantity in allocation.items():
    if asset == 'Adj Close_AAPL':
        total_amount_aapl = quantity * latest_prices[asset]
    elif asset == 'Adj Close_META':
        total_amount_meta = quantity * latest_prices[asset]
    elif asset == 'Adj Close_TSLA':
        total_amount_tsla = quantity * latest_prices[asset]

print("Discrete Allocation:", allocation)

print("Total amount_AAPL: ${:.2f}".format(total_amount_aapl))
print("Total amount_META: ${:.2f}".format(total_amount_meta))
print("Total amount_TSLA: ${:.2f}".format(total_amount_tsla))

total_amount = total_amount_aapl + total_amount_meta + total_amount_tsla

print(f"Total amount for Adj Close_AAPL, Adj Close_META, and Adj Close_TSLA: ${total_amount:.2f}")
print("Funds Remaining: ${:.2f}".format(leftover))
