import pandas as pd

df = pd.read_excel("sales_data_analysis.xlsx", sheet_name="Sheet1")

print("Dataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
print(df.isnull().sum())
print("\nRows with Missing Values:")
print(df[df.isnull().any(axis=1)].to_string())
# Remove rows with missing values
df = df.dropna()

# Reset index
df = df.reset_index(drop=True)

print("\nCleaned Dataset:")
print(df.shape)
print(df.isnull().sum())
print("\nSales Analysis:")

total_sales = df["TotalSales"].sum()
total_profit = df["Profit"].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("\nProduct-wise Sales:")

product_sales = df.groupby("Product")["TotalSales"].sum()

print(product_sales)
original_df = pd.read_excel("sales_data_analysis.xlsx", sheet_name="Sheet1")

print(original_df[original_df["Product"] == "Headphones"])
print(df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False).to_string())
print("\nCity-wise Sales:")

city_sales = df.groupby("City")["TotalSales"].sum()

print(city_sales.to_string())
print("Cities in original data:")
original_df = pd.read_excel("sales_data_analysis.xlsx", sheet_name="Sheet1")
print(original_df["City"].unique())
print(df["City"].value_counts(dropna=False))
print(original_df["City"].value_counts(dropna=False))
print(original_df[original_df["City"].isnull()])
city_sales = df.groupby("City")["TotalSales"].sum()

print(city_sales)
print("\nHighest Sales City:")
print(city_sales.idxmax())
best_product = df.groupby("Product")["TotalSales"].sum()

print("Best Selling Product:")
print(best_product.idxmax())

print("Highest Sales:")
print(best_product.max())
import matplotlib.pyplot as plt

product_sales = df.groupby("Product")["TotalSales"].sum()

product_sales.plot(kind="bar")

plt.title("Product-wise Sales Analysis")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.show()
city_sales = df.groupby("City")["TotalSales"].sum()

city_sales.plot(kind="bar")

plt.title("City-wise Sales Analysis")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.show()
category_sales = df.groupby("Category")["TotalSales"].sum()

print("Category-wise Sales:")
print(category_sales)
category_sales.plot(kind="bar")

plt.title("Category-wise Sales Analysis")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()
df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby("Month")["TotalSales"].sum()

print("Monthly Sales:")
print(monthly_sales)
monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.show()
df.to_csv("cleaned_sales_data.csv", index=False)

print("Cleaned dataset saved successfully!")