import pandas as pd
retail_df = pd.read_csv("online_retail/OnlineRetail.csv", encoding="latin1")
netflix_df = pd.read_csv("netflix_shows/netflix_titles.csv")
print(netflix_df.head())
print(retail_df.head())
print(retail_df.shape)
print(retail_df.info())
print(retail_df.isnull().sum())
print(retail_df.isnull().sum() / len(retail_df)*100)
print(retail_df.duplicated().sum())
retail_df = retail_df.drop_duplicates()
print(retail_df.duplicated().sum())
print(retail_df.dtypes)
retail_df =retail_df.dropna(subset={'Description'})
retail_df['CustomerID'] = retail_df['CustomerID'].fillna(0)
print(retail_df.isnull().sum())
retail_df['InvoiceDate'] = pd.to_datetime(retail_df['InvoiceDate'])
retail_df['Description'] = retail_df['Description'].str.upper()
retail_df['Country'] = retail_df['Country'].str.upper()
retail_df.columns = retail_df.columns.str.lower()
print(retail_df[retail_df['quantity'] < 0].shape[0])
print(retail_df[retail_df['unitprice'] < 0].shape[0])
print(retail_df[['quantity', 'unitprice']].describe())
print(netflix_df.describe())
print(retail_df.groupby('description')['quantity'].sum().sort_values(ascending=False).head(5))
retail_df['revenue'] = retail_df['quantity'] * retail_df['unitprice']
print(retail_df.groupby('country')['revenue'].sum().sort_values(ascending=False).head(5))
retail_df['revenue'] = retail_df['quantity'] * retail_df['unitprice']
retail_df['month'] = retail_df['invoicedate'].dt.to_period('M')
print(retail_df.groupby('month')['revenue'].sum())
print(retail_df['description'].value_counts().head(5))
print(retail_df.groupby('customerid')['revenue'].sum().sort_values(ascending=False).head(5))
print(netflix_df['type'].value_counts())
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce')
netflix_df['year_added'] = netflix_df['date_added'].dt.year
print(netflix_df['year_added'].value_counts().sort_index())
print(netflix_df['country'].value_counts().head(5))
print(netflix_df['rating'].value_counts().head(5))
print(netflix_df['listed_in'].value_counts().head(5))












