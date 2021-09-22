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


missing_values_count = ppri.isnull().sum()
print(missing_values_count)


#data cleaning
ppri['IF_MARKET_PRICE'] = ppri.IF_MARKET_PRICE.astype(object)
ppri['IF_VAT_EXCLUDED'] = ppri.IF_VAT_EXCLUDED.astype(object)

drop_duplicates= ppri.drop_duplicates()
print(ppri.shape,drop_duplicates.shape)
