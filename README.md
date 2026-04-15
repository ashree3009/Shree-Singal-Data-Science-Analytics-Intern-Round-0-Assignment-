# 📊 Bitcoin Sentiment vs Trader Behavior Analysis

## 🔹 Overview

This project analyzes how Bitcoin market sentiment (Fear/Greed) impacts trader behavior and performance using historical trading data.

---

## 📂 Datasets Used

1. **Bitcoin Market Sentiment**

   * Date, Classification (Fear/Greed)

2. **Historical Trader Data**

   * Account, Execution Price, Size USD, Side, Timestamp IST, Closed PnL, etc.

---

## ⚙️ Setup Instructions

1. Clone the repository or download files

2. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

3. Run Jupyter Notebook for analysis:

```bash
jupyter notebook
```

4. Run Streamlit dashboard:

```bash
python -m streamlit run app.py
```

---

## ▶️ How It Works

* Data preprocessing (timestamp conversion, merging datasets)
* Feature engineering (PnL, win rate, trade size)
* Exploratory analysis (sentiment vs performance)
* Trader segmentation
* Predictive modeling & clustering
* Interactive dashboard for visualization

---

## 📊 Outputs

* Performance comparison across sentiment regimes
* Trader behavior analysis
* Segmentation insights
* Interactive dashboard

---

## 🚀 Tech Stack

* Python (Pandas, NumPy)
* Visualization (Matplotlib, Seaborn)
* ML (Scikit-learn)
* Dashboard (Streamlit)
