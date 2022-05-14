import pandas as pd
import numpy as np
people = pd.DataFrame(np.random.randn(5, 5), columns=['a'
,
'b'
,
'c'
,
'd'
,
'e'], index=['Joe'
,
'Steve'
,
'Wes'
,
'Jim'
,
'Travis'])
people.iloc[2:3, [1, 2]] = np.nan # Add a few NA values
print(people)
print(people.groupby(len).sum())
