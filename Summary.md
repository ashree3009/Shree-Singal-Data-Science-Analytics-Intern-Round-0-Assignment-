## 📊 Summary Report

### 🔹 Methodology

The analysis combines Bitcoin market sentiment data with historical trader data.
Timestamps were standardized and aligned at a daily level to merge both datasets.

Key features such as daily PnL, win rate, trade size, and trade frequency were derived.
Exploratory Data Analysis (EDA) was performed to compare performance and behavior across sentiment regimes.

Additionally, trader segmentation and a simple predictive model were implemented to identify behavioral patterns.

---

### 🔹 Key Insights

1. **Performance is highest during Extreme Greed**

   * Highest average PnL and win rate
   * Lowest average losses

2. **Trading activity spikes during Extreme Fear**

   * Highest number of trades per day
   * Indicates reactive or panic-driven trading

3. **Risk-taking behavior differs by sentiment**

   * Larger position sizes during Fear
   * More short positions during Extreme Greed (contrarian behavior)

4. **Frequent traders are not necessarily profitable**

   * High activity often correlates with inconsistent performance

---

### 🔹 Strategy Recommendations

1. **Sentiment-Based Risk Adjustment**

   * Increase exposure during Extreme Greed (higher success rates)
   * Reduce position size during Fear (higher losses)

2. **Avoid Overtrading**

   * Focus on high-quality trades rather than frequent trades
   * Infrequent traders tend to show better consistency

3. **Leverage Behavioral Signals**

   * Monitor sentiment to adjust trading bias (long vs short)
   * Use Fear periods for selective opportunities, not aggressive scaling

---

## 🧠 Conclusion

Market sentiment significantly influences both trader behavior and performance.
Incorporating sentiment signals into trading strategies can improve decision-making and risk management.
