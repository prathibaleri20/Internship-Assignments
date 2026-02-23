import pandas as pd
import numpy as np
info = np.array(['P','a','n','d','a','s'])
a = pd.Series(info)
print(a)

#Create a Series from dict
#import the pandas library
import pandas as pd
import numpy as np
info = {'x' : 0., 'y' : 1., 'z' : 2.}
a = pd.Series(info)
print (a)

#Create a Series using Scalar:
#import pandas library
import pandas as pd
import numpy as np
x = pd.Series('VIKAS', index=[0, 1, 2, 3])
print (x)

#Retrieving Index array and data array of a series object
import numpy as np
import pandas as pd
x=pd.Series(data=[2,4,6,8])
y=pd.Series(data=[11.2,18.6,22.5], index=['a','b','c'])
print(x.index)
print(x.values)
print(y.index)
print(y.values)


#Retrieving Shape
import numpy as np
import pandas as pd
a=pd.Series(data=[1,2,3,4])
b=pd.Series(data=[4.9,8.2,5.6],index=['x','y','z'])
print(a.shape)
print(b.shape)

#Retrieving Dimension, Size and Number of bytes:
import numpy as np
import pandas as pd
a=pd.Series(data=[1,2,3,4])
b=pd.Series(data=[4.9,8.2,5.6],
index=['x','y','z'])
print(a.ndim, b.ndim)
print(a.size, b.size)
print(a.nbytes, b.nbytes)

#Pandas Series.map()
import pandas as pd
import numpy as np
a = pd.Series(['Java', 'C', 'C++', np.nan])
print(a.map({'Java': 'Core'}) )

import pandas as pd
import numpy as np
a = pd.Series(['Java', 'C', 'C++', np.nan])
a.map({'Java': 'Core'})
print(a.map('I like {}'.format, na_action='ignore')  )


