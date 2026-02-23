#Create a DataFrame from Dict of ndarrays/ Lists
# importing the pandas library
import pandas as pd
info = {'ID' :[101, 102, 103],'Department' :['B.Sc','B.Tech','M.Tech',]}
df = pd.DataFrame(info)
print (df)

#Create a DataFrame from Dict of Series:
# importing the pandas library
import pandas as pd
info = {'one' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),  'two' : pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}
d1 = pd.DataFrame(info)
print (d1)

# importing the pandas library
import pandas as pd
info = {'one' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}
d1 = pd.DataFrame(info)
print (d1 ['one'])

# importing the pandas library
import pandas as pd

info = {'one': pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
        'two': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}
df = pd.DataFrame(info)
# Add a new column to an existing DataFrame object
print("Add new column by passing series")
df['three'] = pd.Series([20, 40, 60], index=['a', 'b', 'c'])
print(df)
print("Add new column using existing DataFrame columns")
df['four'] = df['one'] + df['three']
print(df)

# importing the pandas library
import pandas as pd

info = {'one': pd.Series([1, 2], index=['a', 'b']),
        'two': pd.Series([1, 2, 3], index=['a', 'b', 'c'])}

df = pd.DataFrame(info)
print("The DataFrame:")
print(df)
# using del function
print("Delete the first column:")
del df['one']
print(df)
# using pop function
print("Delete the another column:")
df.pop('two')
print(df)


# importing the pandas library
import pandas as pd
info = {'one' : pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e']),
   'two' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f'])}
df = pd.DataFrame(info)
print (df[2:5])


import pandas as pd

d = pd.DataFrame([[7, 8], [9, 10]], columns=['x','y'])
d2 = pd.DataFrame([[11, 12], [13, 14]], columns=['x','y'])
# Use concat instead of append
d = pd.concat([d, d2], ignore_index=True)
print(d)

import pandas as pd
import numpy as np
info = pd.DataFrame({'col1':[7,1,8,3],'col2':[8,12,4,9]})
info_2 = info.sort_values(by='col2')
print(info_2)

import pandas as pd

info_marks = pd.DataFrame({
    'name': ['Parker', 'Smith', 'William', 'Terry'],
    'Maths': [78, 84, 67, 72],
    'Science': [89, 92, 61, 77],
    'English': [72, 75, 64, 82]
})

# Use a valid existing path
output_path = r'C:\Users\HP\PycharmProjects\PythonProject\output.xlsx'

with pd.ExcelWriter(output_path) as writer:
    info_marks.to_excel(writer, index=False)

print('DataFrame is written successfully to the Excel File.')

