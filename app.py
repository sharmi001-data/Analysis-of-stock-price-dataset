import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# App config
st.set_page_config(page_title="Stock Price Analysis", layout="wide")
st.title(" Stock Price Analysis Project")
st.markdown("**Author: Sharmistha Das**")
st.divider()

turnover_df = pd.read_csv("avg_turnover_per_company.csv")
st.markdown("""
###  Average Turnover per Company

This bar chart displays the **average daily turnover** (traded value) of each company over the available time period.  
It helps identify which companies were the most actively traded in the stock market.

High turnover values typically indicate:
- Strong investor interest
- High liquidity
- More frequent trading activity

Companies like **Tesla, Apple, Amazon, Nvidia, Microsoft**, and **Google** show significantly higher turnover than others, 
highlighting their dominance and popularity in the market.

Lower turnover brands may indicate niche investments or less frequent trades.
""")


plt.figure(figsize=(12,16))
sns.barplot(data=turnover_df, x="Turnover", y="Brand_Name", palette="viridis")
plt.title("Average Turnover per Company")
plt.xlabel("Turnover")
plt.ylabel("Brand")
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
### Top 5 Companies by Average Turnover

This chart highlights the **top 5 companies** with the highest average turnover:

- **Tesla** leads by a large margin, followed by **Apple**, **Nvidia**, **Amazon**, and **Microsoft**.
- The significant gap between Tesla and the rest reflects its extremely high trading activity and market influence.
- The rest of the companies are relatively close in turnover values.

This ranking can help investors target high-liquidity stocks for better execution efficiency.
""")

top_5_df = pd.read_csv("top_5_companies.csv")

plt.figure(figsize=(8, 4))
sns.barplot(data=top_5_df, x="Turnover", y="Brand_Name",)
plt.title("Top 5 Companies by Average Turnover")
plt.xlabel("Average Turnover")
plt.ylabel("Brand Name")
plt.tight_layout()
st.pyplot(plt.gcf())


