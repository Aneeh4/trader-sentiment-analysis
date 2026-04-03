 Trader Performance vs Market Sentiment  
 An Analysis of Behavioral Patterns and Profitability on Hyperliquid  


 Objective  

This project analyzes how Bitcoin market sentiment (Fear vs Greed) impacts trader behavior and performance.  

The goal is to uncover patterns in trading activity and derive actionable insights for smarter trading strategies.

---

 Datasets  
 Market Sentiment Dataset  
- Contains daily Fear/Greed classification  
- Fields: `date`, `classification`  

 Historical Trading Data  
- Contains trader-level execution data  
- Fields: `Account`, `Timestamp`, `Size USD`, `Side`, `Closed PnL`  

---

 Methodology  

 Data Preparation  
- Cleaned missing and duplicate values  
- Converted timestamps to daily format  
- Merged datasets on Date  

---

 Feature Engineering  
- PnL (Profit & Loss)  
- Win Rate  
- Trade Frequency  
- Position Size  
- Buy/Sell behavior  

---

 Analysis  
- Compared performance across sentiment categories  
- Studied trading behavior changes  
- Identified behavioral patterns  

---
 Trader Segmentation  
- High vs Low position size  
- Frequent vs Infrequent traders  
- Consistent vs Inconsistent traders  

---
 Key Insights  

- Greed markets show higher profits but also higher volatility  
- Traders overtrade during Greed periods  
- Fear markets promote disciplined and consistent trading  
- Market sentiment strongly influences trader psychology  

---

 Strategy Recommendations  

- Reduce position size and avoid overtrading during Greed  
- Focus on disciplined trading during Fear  
- Limit daily trades for frequent traders  

---

Project Structure
trader-sentiment-analysis/
│── data/
│ ├── fear_greed_index.csv
│ └── historical_data.csv
│
│── notebook.ipynb
│── analysis.py
│── README.md
│── requirements.txt


---
How to Run  

```bash
pip install -r requirements.txt
python analysis.py




