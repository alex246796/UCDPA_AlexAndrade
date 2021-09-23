#>>>>>>>>>>>>>  GO TO ROW 80

#import pandas
import pandas as pd


#load csv file
ppri = pd.read_csv("Property_Price_Register_Ireland-28-05-2021.csv",parse_dates=['SALE_DATE'])

#data investigation
print(ppri)
print(ppri.head())
print(ppri.tail())
print(ppri.describe())
print(ppri.describe(include='object'))
print(ppri.info())
print(ppri.shape)

missing_values = ppri.isnull()
print(missing_values)

missing_values_count = ppri.isnull().sum()
print(missing_values_count)


#data cleaning
ppri['IF_MARKET_PRICE'] = ppri.IF_MARKET_PRICE.astype(object)
ppri['IF_VAT_EXCLUDED'] = ppri.IF_VAT_EXCLUDED.astype(object)

#Creating a new column with Year
ppri['SALE_YEAR'] = pd.DatetimeIndex(ppri['SALE_DATE']).year


#Dropping duplications
ppri2= ppri.drop_duplicates()
print(ppri.shape,ppri2.shape)


#Dropping unneeded columns
ppri3 = ppri2.drop(['POSTAL_CODE','IF_MARKET_PRICE','IF_VAT_EXCLUDED', 'PROPERTY_SIZE_DESC'], axis = 1)

#Reassessing structure of data after deleting columns
print(ppri3.head())
print(ppri3.info())
missing_values_count3 = ppri3.isnull().sum()
print(missing_values_count3)

#Dropping duplications
ppri4= ppri3.drop_duplicates()
print(ppri3.shape,ppri4.shape)
print(ppri4.head())
print(ppri4.columns.tolist())
print(ppri4.tail())

#Filtering only 10 years period between 2011-2020
start_date = '01-01-2011'
end_date = '31-12-2020'
filter = (ppri4['SALE_DATE'] >= start_date) & (ppri4['SALE_DATE'] <= end_date)
ppri5 = ppri4.loc[filter]
print(ppri5)



#Groupping/indexing
ppri6 = (ppri5.groupby(['SALE_YEAR','COUNTY']) .agg(UNITS_SOLD=('SALE_DATE',"count"),AVERAGE_SALE_PRICE=('SALE_PRICE',"mean")).reset_index())
print(ppri6)





#Rounding AVERAGE_SALE_PRICE by converting into int
ppri6['AVERAGE_SALE_PRICE'] = ppri6.AVERAGE_SALE_PRICE.astype(int)
print(ppri6)
print(ppri6.info())




#Creation of a list to subset a dataframe
condition = [2020]
ppri7 = ppri6[ppri6['SALE_YEAR'].isin(condition)]
print(ppri7)


#Sorting
ppri8 = ppri7.sort_values(by=['AVERAGE_SALE_PRICE'])
print(ppri8)
print(ppri8.info())


#Creating chart with matplotlib
import matplotlib.pyplot as plt
ppri8.plot(x="COUNTY", y="AVERAGE_SALE_PRICE", kind="scatter", rot=55,title='Average price per county in 2020')
plt.xticks(ppri6['COUNTY'])
plt.xlabel('COUNTY')
plt.ylabel('AVERAGE PRICE')
plt.show()
