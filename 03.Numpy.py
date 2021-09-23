# Creating arrays with numpy of the years that Will be worked in the project

import numpy as np

Years_array1 = np.array(['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
print(Years_array1)



# Creating arrays with numpy of the years that Will be worked in the comparisons with rent market through the API
indexing_array = np.array([0,5])
Years_array2 = Years_array1[indexing_array]
print(Years_array2)



# Define a custom function to create reusable code


