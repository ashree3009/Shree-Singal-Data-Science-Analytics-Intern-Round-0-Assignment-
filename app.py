import streamlit as st
import pandas as pd

# Load Original Data
sentiment_df = pd.read_csv('fear_greed_index.csv')
trader_df = pd.read_csv('historical_data.csv')

# Preprocessing (same as notebook)

# Convert dates
sentiment_df['date'] = pd.to_datetime(sentiment_df['date'], errors='coerce')
sentiment_df['date'] = sentiment_df['date'].dt.date

trader_df['Timestamp IST'] = pd.to_datetime(
    trader_df['Timestamp IST'],
    dayfirst=True,
    errors='coerce'
)
trader_df['date'] = trader_df['Timestamp IST'].dt.date

# Merge
df = pd.merge(
    trader_df,
    sentiment_df[['date', 'classification']],
    on='date',
    how='left'
)

# UI

st.title("Trader Behavior Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['classification'].dropna().unique(),
    default=df['classification'].dropna().unique()
)

account_filter = st.sidebar.multiselect(
    "Select Account",
    options=df['Account'].unique(),
    default=df['Account'].unique()[:10]
)

# Apply filters
filtered_df = df[
    (df['classification'].isin(sentiment_filter)) &
    (df['Account'].isin(account_filter))
]

# Metrics
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total PnL", round(filtered_df['Closed PnL'].sum(), 2))
col2.metric("Avg Trade Size", round(filtered_df['Size USD'].mean(), 2))
col3.metric("Win Rate", round((filtered_df['Closed PnL'] > 0).mean(), 2))

# Charts

st.subheader("PnL by Sentiment")
st.bar_chart(filtered_df.groupby('classification')['Closed PnL'].sum())

st.subheader("Trades per Day")
st.line_chart(filtered_df.groupby('date').size())

st.subheader("Avg Trade Size")
st.bar_chart(filtered_df.groupby('classification')['Size USD'].mean())

# Data Preview
st.subheader("Data Preview")
st.dataframe(filtered_df.head())