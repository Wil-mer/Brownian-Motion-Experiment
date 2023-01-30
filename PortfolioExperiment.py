## Wilmer Liljenström
## Brownian motion and VaR experiment
## With a 95% confidence interval, what is the largest possible loss over a period of one month?
## Returns expected to be normally distributed

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n_days = 365*3
n_stocks = 20
z_score = 1.65

## Initialize portfolio
portfolio = np.zeros((n_stocks, n_days))

## Generate a random stock price using Brownian motion
for i in range(n_stocks):
  prices = [10]
  for j in range(1, n_days):
      prices.append(prices[j-1] + norm.rvs(loc=0))
  portfolio[i] = prices
  
portfolio_value = np.sum(portfolio,axis=0)
for i in range(n_days):
  if portfolio_value[i]<0:
    print('Portfolio blown')
    plt.plot(portfolio_value[i])
    plt.xlabel('Steps')
    plt.ylabel('Portfolio Value')
    plt.title('Value of Portfolio Over Time')
    plt.show()
    exit()
## Calculate daily rate of change
delta = np.zeros(n_days)
for i in range(2, n_days):
  delta[i]=((portfolio_value[i]-portfolio_value[i-1])/portfolio_value[i-1])

## Calculate average rate of rate of change
delta_mean = delta.mean()
print('Mean:')
print(delta_mean)

## Calculate standard deviation of rate of change
delta_std = delta.std()
print('Std:')
print(delta_std)

## Portfolio value at day n
print('Portfolio value')
print(portfolio_value[n_days-1])

## Value at risk
VAR=(delta_mean-z_score*delta_std)*portfolio_value[n_days-1]
print('VaR:')
print(VAR)

## Plot the portfolio value as a function of days
plt.plot(portfolio_value)
plt.xlabel('Steps')
plt.ylabel('Portfolio Value')
plt.title('Value of Portfolio Over Time')
plt.show()