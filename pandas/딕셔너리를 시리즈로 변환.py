import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3}

sr = pd.Series(dict_data)

print(type(sr))
print("\n")
print(sr)

list_data = [123,456,"abc"]
sr_2 = pd.Series(list_data, index = ['a', 'b', 'c'])
print(sr_2)