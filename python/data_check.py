import pandas as pd

sales = pd.read_csv("data/ACPA_CAMAData/Sales.txt",sep="\t")

#look at the head of the dataset
sales.head( n = 10)
sales.info()

#look at min and max of sales data
sales.Sale_Price.max()
sales.Sale_Price.min()

sales.describe()
sales['Sale_Price'].min()
sales['Sale_Price'].max()

float(sales['Sale_Price'].max())


#get an average
sales.Sale_Price.mean(skipna=True)
