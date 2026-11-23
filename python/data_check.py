import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

#right now this script exercises some basic data exploration
# using various python libraries

sales = pd.read_csv("data/ACPA_CAMAData/Sales.txt",sep="\t")
property = pd.read_csv("data/ACPA_CAMAData/Property.txt",sep="\t")
geo = gpd.read_file("data/publicparcels/PublicParcels.shp")

#plot the shapefile quickly to see
map = geo.plot(column="Shape_Area", legend=True)
map.set_title("Areas for Alachua County Parcels")

#look at the head of the dataset(s)
sales.head( n = 10)
sales.info()
sales.Sale_Qualified.unique()

property.head( n = 10)


#look at min and max of sales data
sales.Sale_Price.max()
sales.Sale_Price.min()

sales.describe()
sales['Sale_Price'].min()
sales['Sale_Price'].max()

float(sales['Sale_Price'].max())


#get an average
sales.Sale_Price.mean(skipna=True)

#plot histograms
sales.Sale_Price.hist()

plt.show()
