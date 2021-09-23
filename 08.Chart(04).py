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
ppri6 = (ppri5.groupby(['SALE_YEAR']) .agg(UNITS_SOLD=('SALE_DATE',"count"),AVERAGE_SALE_PRICE=('SALE_PRICE',"mean")).reset_index())
print(ppri6)




#Rounding AVERAGE_SALE_PRICE by converting into int
ppri6['AVERAGE_SALE_PRICE'] = ppri6.AVERAGE_SALE_PRICE.astype(int)
print(ppri6)
print(ppri6.info())
print(ppri6.tail())






#Creating a new columns by adding a list
COUNTY = ['Ireland', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Ireland', 'Ireland']

ppri6['COUNTY'] = COUNTY
print(ppri6)




#Groupping other counties to compare historical average of country vs lowest and highest prices as at 2020
ppri8 = (ppri5.groupby(['SALE_YEAR','COUNTY']) .agg(UNITS_SOLD=('SALE_DATE',"count"),AVERAGE_SALE_PRICE=('SALE_PRICE',"mean")).reset_index())
print(ppri8)

#Rounding AVERAGE_SALE_PRICE by converting into int
ppri8['AVERAGE_SALE_PRICE'] = ppri8.AVERAGE_SALE_PRICE.astype(int)
print(ppri8)
print(ppri8.info())
print(ppri8.tail())


#concatenate all counties data + average of the country
frames = [ppri6, ppri8]

ppri9 = pd.concat(frames)
print (ppri9)


#Silicing Ireland, and the Max and Min Dublin and Roscommon
condition = ['Ireland', 'Dublin', 'Roscommon']
ppri10 = ppri9[ppri9['COUNTY'].isin(condition)]
print(ppri10)


#Sorting
ppri11 = ppri10.sort_values(by=['COUNTY','SALE_YEAR'])
print(ppri11)
print(ppri11.info())

#distributing the data in different datasets
ppri_Ireland = ppri11[ppri11.COUNTY == 'Ireland']
print(ppri_Ireland)

ppri_Dublin = ppri11[ppri11.COUNTY == 'Dublin']
print(ppri_Dublin)

ppri_Roscommon = ppri11[ppri11.COUNTY == 'Roscommon']
print(ppri_Roscommon)




#Chart
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(ppri_Ireland["SALE_YEAR"], ppri_Ireland["AVERAGE_SALE_PRICE"], color='b')
ax.set_xlabel("YEARS")
ax.set_ylabel("AVERAGE PRICE")

ax.plot(ppri_Dublin["SALE_YEAR"], ppri_Dublin["AVERAGE_SALE_PRICE"], linestyle='--', color='r')
ax.plot(ppri_Roscommon["SALE_YEAR"], ppri_Roscommon["AVERAGE_SALE_PRICE"], linestyle='--', color='g')
plt.legend(["Ireland", "Dublin", "Roscommon"])
ax.title.set_text('Average price of houses in the last 10 years')
plt.show()



