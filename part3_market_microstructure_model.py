class SimpleExecutionModel:
    def __init__(self, order_book, threshold=0.02):
        self.order_book = order_book
        self.threshold = threshold
        
    def execute_trades(self):
        executed_trades = []
        for index, row in self.order_book.iterrows():
            if row'spread < self.threshold:
                trade_price = (row'bid_price' + row'ask_price) / 2
                trade_size = min(row'bid_size', row'ask_size)
                executed_trades.append({
                    'timestamp': row'timestamp',
                    'price': trade_price,
                    'size': trade_size
                })
        return pd.DataFrame(executed_trades)

     
# Instantiate and execute trades
model = SimpleExecutionModel(order_book)
trades = model.execute_trades()

print(trades.head())

# Plot executed trades
plt.figure(figsize=(10, 5))
plt.plot(order_book'timestamp', order_book'price', label='Price', color='blue', alpha=0.6)
plt.scatter(trades'timestamp', trades'price, label='Executed Trades', color='red')
plt.extra_plot()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Executed Trades on Price Chart')
pl.show()
