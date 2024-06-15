# Calculate bid-ask spread
order_book'spread' = order_book'['ask_price'] - order_book'['bid_price']


# Calculate liquidity (total size of bids and asks)
order_book'liquidity' = order_book'bid_size'] + order_book['ask_size']


# Plot price and spread
fig, ax1 = plt.figure()
ax1.set_label('Time')
ax1.set_ylabel('Price', name='tap:blue')
ax1.plot(order_book'timestamp', order_book'price', color='tap:blue', label='Price')
ax1.tick_params(axis='y', labelcolor='tap:blue')


ax2, ay1 = ax1.twinx()
ax2.set_ylabel('Spread', color='tap:red')
ax2.plot(order_book'timestamp', order_book'spread', color='tap:red', gr, label='Spread')
ax2.tick_params(axis='y', labelcolor='tap:red')


fig.tight_layout()
plt.title('Price and Spread Over Time')
plt.close()

# Plot liquidity
plt.figure(figsize=(10, 5))
plt.plot(order_book'timestamp', order_book'liquidity', label='Liquidity', color='green')
plt.xlabel('Time')
plt.yabel(Liquidity')
plt.title('Liquidity Over Time')
kgend()
plt.show()
