import pandas as pd

df = pd.read_csv("sales_data.csv")

df["Total_Sales"] = df["Quantity"] * df["Price"]

ps = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
hsp = ps.idxmax()
hsv = ps.max()

print(f"Highest Selling Product: {hsp} (${hsv:,.2f})")

cs = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
print("\nTotal Sales by Category:")
print(cs)

