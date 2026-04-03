import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
sentiment = pd.read_csv("data/fear_greed_index.csv")
trades = pd.read_csv("data/historical_data.csv")

# Convert dates
sentiment['date'] = pd.to_datetime(sentiment['date'])
trades['Timestamp'] = pd.to_datetime(trades['Timestamp'], unit='ms')

sentiment['Date'] = sentiment['date'].dt.date
trades['Date'] = trades['Timestamp'].dt.date

# Rename columns
sentiment.rename(columns={'classification': 'Sentiment'}, inplace=True)
trades.rename(columns={'Closed PnL': 'PnL'}, inplace=True)

# Convert numeric
trades['PnL'] = pd.to_numeric(trades['PnL'], errors='coerce')
trades['Size USD'] = pd.to_numeric(trades['Size USD'], errors='coerce')

# Merge
df = trades.merge(sentiment[['Date', 'Sentiment']], on='Date', how='left')

# Feature Engineering
df['win'] = df['PnL'] > 0

# -------------------------
# ANALYSIS
# -------------------------

# PnL vs Sentiment
sns.boxplot(x='Sentiment', y='PnL', data=df)
plt.xticks(rotation=45)
plt.title("PnL Distribution by Sentiment")
plt.show()

# Win Rate
win_rate = df.groupby('Sentiment')['win'].mean()
print("\nWin Rate:\n", win_rate)

# Trade Frequency
df['Sentiment'].value_counts().plot(kind='bar', title="Trade Count by Sentiment")
plt.show()

# Trade Size
sns.boxplot(x='Sentiment', y='Size USD', data=df)
plt.xticks(rotation=45)
plt.title("Trade Size by Sentiment")
plt.show()

# Buy/Sell behavior
df.groupby(['Sentiment', 'Side']).size().unstack().plot(kind='bar')
plt.title("Buy vs Sell by Sentiment")
plt.show()

# -------------------------
# SEGMENTATION
# -------------------------

# Size segment
df['size_segment'] = df['Size USD'].apply(
    lambda x: 'High' if x > df['Size USD'].median() else 'Low'
)

# Frequency segment
trade_counts = df['Account'].value_counts()
df['freq_segment'] = df['Account'].apply(
    lambda x: 'Frequent' if trade_counts[x] > trade_counts.median() else 'Infrequent'
)

# Consistency segment
pnl_std = df.groupby('Account')['PnL'].std()
df['consistency'] = df['Account'].apply(
    lambda x: 'Consistent' if pnl_std[x] < pnl_std.median() else 'Inconsistent'
)

print("\nSegmentation Done ✅")