import pandas as pd
import numpy as np
import seaborn as sns

#시리즈 vs  숫자
'''
student1 = pd.Series({'korean':100, 'eng':80, 'math':90})
print(student1)
print("\n")

percentage = student1/200
print(percentage)
print("\n")
'''
#시리즈 vs 시리즈
'''
student1 = pd.Series({'korean':100, 'eng':80, 'math':90})
student2 = pd.Series({'eng':70,'korean':90, 'math':50})
student3 = pd.Series({'eng':70,'korean':90, 'sci':80})

addition = student1 + student2
sub = student1 - student2

print(addition)
print("\n")
print(sub)
print("\n")


k = student1 + student3
print(k)
print("\n")
d = student1.add(student3, fill_value = 0)
print(d)
'''

#데이터프레임 vs 데이터프레임
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print("\n")
add = df + 10
print(add.head())
print("\n")

k = add - df
print(k.head())
