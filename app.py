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

#load the preprocessed dataset
turnover_df = pd.read_csv("./Data/avg_turnover_per_company.csv")
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

#plot
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
#load the preprocessed dataset
top_5_df = pd.read_csv("./Data/top_5_companies.csv")

#plot
plt.figure(figsize=(8, 4))
sns.barplot(data=top_5_df, x="Turnover", y="Brand_Name",palette="Set1")
plt.title("Top 5 Companies by Average Turnover")
plt.xlabel("Average Turnover")
plt.ylabel("Brand Name")
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
###  Year-over-Year Turnover Growth (Before COVID)

This line chart visualizes turnover growth trends **from 2017 to 2019**:

- **Tesla, Netflix, Amazon, and 3M** had rapid growth in 2018 — over 500% in some cases.
- **Growth slowed in 2019** for most brands, with some even showing negative rates (e.g., Spotify, Southwest Airlines).
- Stable brands had flatter lines, indicating steady revenue.

This analysis helps pinpoint which companies were expanding vs. stagnating right before the pandemic.
""")

#load the preprocessed dataset
yoy_growth_before_covid = pd.read_csv("./Data/yoy_df2.csv")

#plot
plt.figure(figsize=(12, 10))
sns.lineplot(data=yoy_growth_before_covid, x="year", y="YoY_Growth (%)", hue="Brand_Name", marker="o")
plt.title("Year-over-Year Growth in Turnover by Brand (Before COVID)")
plt.xlabel("Year")
plt.ylabel("YoY Growth Rate (%)")
plt.axhline(0, color='black', linestyle='--')
plt.legend(title="Brand Name", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
###  Year-over-Year Turnover Growth (After COVID)

This chart tracks turnover trends **from 2021 to 2025**:

- **2023–2024**: Companies like **Cisco, Airbnb, and Coinbase** saw sharp recoveries.
- **2025**: Many brands showed **decline or slowdown** in turnover.
- **Logitech, Philips, Zoom** consistently showed poor growth, possibly due to fading remote-work demand.

The data shows a post-COVID rebound followed by rebalancing in growth.
""")

#load the preprocessed dataset
yoy_growth_after_covid = pd.read_csv("./Data/YoY_df.csv")

#plot
plt.figure(figsize=(12, 12))
sns.lineplot(data=yoy_growth_after_covid, x="year", y="YoY_Growth (%)", hue="Brand_Name", marker="o")
plt.title("Year-over-Year Growth in Turnover by Brand (After COVID)")
plt.xlabel("Year")
plt.ylabel("YoY Growth Rate (%)")
plt.axhline(0, color='black', linestyle='--')
plt.legend(title="Brand Name", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
###  Brand-wise Mean Turnover Contribution

This pie chart shows how much each brand contributes to total average turnover.

- **Tesla** dominates the share (approx. 18.1%), followed by **Apple**, **Nvidia**, **Amazon**, and **Microsoft**.
- Many other brands (e.g., **Spotify, Nike, Airbnb, Roblox**) contribute **less than 1%**.

This emphasizes a highly concentrated market, with only a few brands holding most of the trading power.
""")

#load the preprocessed dataset
contribution_avg_turnover = pd.read_csv("./Data/turnover_per_company.csv")

#plot
fig = px.pie(
    contribution_avg_turnover,
    names="Brand_Name",
    values="turnovers_%",
    hover_data=["total_mean_turnover"],
    title="Brand-wise Mean Turnover Contribution"
)
fig.update_layout(width=1000, height=800, legend_title="Brand Names")
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig)

st.markdown("""
###  Fluctuation Percent by Brand and Period

This bar chart compares the **stock price fluctuation percentages** for different brands during three major periods:
- **Before COVID**
- **During COVID**
- **After COVID**

Key observations:
- Many brands like **Coinbase, Puma, Uber, and The Coca-Cola Company** showed extreme fluctuation during the **post-COVID** phase.
- **Southwest Airlines, Delta Airlines**, and some tech companies like **Peloton** saw high fluctuation **during COVID**.
- **Most fluctuations were moderate** for established companies like **Apple, Microsoft, and Johnson & Johnson**.

This visualization reveals how different companies adapted or struggled through market instability across pandemic phases.
""")

# Load the preprocessed dataset
final_df= pd.read_csv("./Data/melted.csv")

# Plot using seaborn
plt.figure(figsize=(14, 20))
sns.barplot(data=final_df, x="Fluctuation", y="Brand_Name", hue="Period")
plt.title("Fluctuation Percent by Brand and Period")
plt.xlabel("Fluctuation (%)")
plt.ylabel("Brand")
plt.legend(title="Period", loc="upper right")
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
###  Brand-wise Stock Price Volatility

This bar chart visualizes the **volatility** of each brand's stock price, measured by the **standard deviation of daily returns**.

- Brands like **Coinbase, Peloton, Roblox, Pinterest, Shopify, and Tesla** exhibit **high volatility**, indicating significant daily price swings.
- On the other hand, **Johnson & Johnson, Coca-Cola, Procter & Gamble, and McDonald's** show **low volatility**, representing more stable stocks.
- This analysis helps investors gauge **risk levels** across brands and industries.

Higher volatility may imply greater opportunity — but also higher risk.
""")

# Load the dataset with standard deviation values
voladility = pd.read_csv("./Data/std_daily_returns.csv", index_col=0)

# Plot the volatility
plt.figure(figsize=(14, 16))
sns.barplot(x=voladility.values.flatten(), y=voladility.index, palette="viridis", orient='h')
plt.xlabel("Standard Deviation of Daily Returns (Volatility)", fontsize=12)
plt.ylabel("Brand Name", fontsize=12)
plt.title("Brand-wise Stock Price Volatility", fontsize=14)
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
###  Country-wise Market Behavior based on Average Daily Return

This bar chart represents the **average daily return of stock prices** across different countries.

- **Canada** stands out with the highest daily return, suggesting a **more aggressive or faster-growing** market behavior.
- Countries like **Switzerland** and the **USA** also show strong positive returns.
- **Japan** and **Netherlands** show relatively **lower average returns**, possibly indicating more **conservative market dynamics**.

This visualization gives an overview of how different countries perform in terms of **stock return trends**.
""")

# Load the preprocessed dataset
country_wise_behaviour = pd.read_csv("./Data/avg_return_per_country.csv")

# Plot
plt.figure(figsize=(8, 6))
sns.barplot(data=country_wise_behaviour, y="Country", x="Daily_Return", hue="Country")
plt.title("Country-wise Market Behavior based on their average daily return", fontsize=14, weight='bold')
plt.xlabel("Average Daily Return")
plt.ylabel("Country")
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
###  Yearly Average Closing Price by Industry

This line chart visualizes the **average yearly stock closing price** across different industries over time.

- The **technology** and **cryptocurrency** industries show a **sharp rise** between 2017 and 2021, followed by **noticeable drops**.
- Industries like **e-commerce, financial services, and automotive** follow with moderate growth trends.
- **Healthcare**, **consumer goods**, and **food sectors** remain **relatively stable** over the years.

This chart highlights how industry trends evolve and how certain sectors are more **volatile or growth-driven** than others.
""")

# Load the preprocessed dataset
avg_per_industry = pd.read_csv("./Data/avg_over_year_per_industry.csv")

# Plot
plt.figure(figsize=(14, 8))
sns.lineplot(data=avg_per_industry, x="year", y="Close", hue="Industry_Tag", marker="o")
plt.title("Yearly Average Closing Price by Industry", fontsize=14, weight='bold')
plt.xlabel("Month")
plt.ylabel("Average Closing Price")
plt.xticks(rotation=45)
plt.legend(title="Industry", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
### Another Way- Yearly Average Closing Price by Industry (2020–2025)

This bar chart focuses on the **closing price trends across industries** from **2020 to 2025**.

- **Technology**, **cryptocurrency**, and **e-commerce** industries had significant growth in the **early 2020s**, reflecting investor interest during and after the COVID-19 period.
- Some industries like **retail** and **finance** show **moderate fluctuations**, while **food, apparel**, and **hospitality** remained comparatively **stable**.

This visualization captures how different sectors performed in the **post-COVID market landscape**.
""")

# Load the preprocessed data
df = pd.read_csv("./Data/avg_over_year_per_industry.csv")

filtered = df[(df["year"] >= 2020) & (df["year"] <= 2025)]

# Plot
plt.figure(figsize=(14, 8))
sns.barplot(data=filtered, x="year", y="Close", hue="Industry_Tag")
plt.title("Another Way(2020-2025)-Yearly Average Closing Price by Industry", fontsize=14, weight='bold')
plt.xlabel("Month")
plt.ylabel("Average Close Price")
plt.xticks(rotation=45)
plt.legend(title="Industry", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
###  Correlation Matrix Heatmap

This heatmap visualizes the **correlation** between various numerical stock features.

- **Dark colors** indicate strong **positive** or **negative** relationships.
- Features like **Open, Close, High, and Low** show very **high correlations**, indicating they move closely together.
- **Volume** has a **weaker correlation** with price-based features, highlighting its relatively independent nature.

This chart helps us understand the **internal dependencies** within stock attributes.
""")

# Load the correlation matrix
import numpy as np
cor_df = pd.read_csv("./Data/cor.csv", index_col=0)

# Plot
plt.figure(figsize=(10, 6))
sns.heatmap(cor_df, annot=True, cmap="viridis", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
st.pyplot(plt.gcf())

st.markdown("""
###  Active Years of Each Brand

This horizontal bar chart visualizes how long each brand has remained active in the stock market dataset.

- Brands like **3M**, **Adobe**, **Amazon**, and **Apple** have had a **long-standing presence**, consistently active for over 25 years.
- Newer companies like **Roblox**, **Coinbase**, **Airbnb**, and **ZoomInfo** show **shorter active spans**—less than 6 years.

This chart provides a strong indicator of **market maturity vs. newer entrants**, useful for trend and risk analysis.
""")
# Load the preprocessed dataset
brands_active_years = pd.read_csv("./Data/active_years.csv")

brands_active_yearsd= brands_active_years.sort_values(by="Active_Years", ascending=False)

#plot
fig = px.bar(
    brands_active_years,
    x="Active_Years",
    y="Brand_Name",
    orientation="h",
    color="Active_Years",
    color_continuous_scale="viridis",
    title="Active Years of Each Brand",
    labels={"Active_Years": "Number of Years", "Brand_Name": "Brand"}
)

fig.update_layout(height=1000)
st.plotly_chart(fig)







