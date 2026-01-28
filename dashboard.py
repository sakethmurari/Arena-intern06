from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Create subplot layout
df = pd.read_csv("sales_data (4).csv")
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=[
        "Sales Trend Over Time", "Sales by Region",
        "Sales Distribution", "Profit Distribution",
        "Product Performance", "Feature Correlation"
    ],
    vertical_spacing=0.12,
    horizontal_spacing=0.08
)

# 1️⃣ Sales Trend
fig.add_trace(
    go.Scatter(x=df['Date'], y=df['Total_Sales'],
               mode='lines+markers', name="Sales"),
    row=1, col=1
)

# 2️⃣ Sales by Region
region_sales = df.groupby('Region')['Total_Sales'].sum().reset_index()
fig.add_trace(
    go.Bar(x=region_sales['Region'], y=region_sales['Total_Sales'],
           name="Region Sales"),
    row=1, col=2
)

# 3️⃣ Sales Distribution
fig.add_trace(go.Box(y=df['Total_Sales'], name="Sales"), row=2, col=1)

# 4️⃣ Price Distribution
fig.add_trace(go.Violin(y=df['Price'], name="Price"), row=2, col=2)

# 5️⃣ Product Performance
product_sales = df.groupby('Product')['Total_Sales'].sum().reset_index()
fig.add_trace(
    go.Bar(x=product_sales['Product'], y=product_sales['Total_Sales'],
           name="Product Sales"),
    row=3, col=1
)

# 6️⃣ Correlation Heatmap
corr = df.corr(numeric_only=True)
fig.add_trace(
    go.Heatmap(z=corr.values,
               x=corr.columns,
               y=corr.columns),
    row=3, col=2
)

# Dashboard Styling
fig.update_layout(
    height=900,
    width=1200,
    title_text="📊 Interactive Sales Performance Dashboard",
    title_x=0.5,
    template="plotly_white",
    showlegend=False
)

fig.show()
