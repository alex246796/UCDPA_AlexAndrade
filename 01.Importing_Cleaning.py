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

