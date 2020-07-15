import pandas as pd

dict_data = {'c0': [1,2,3],'c1': [4,5,6],'c2': [7,8,9],'c3': [10,11,12],'c4': [13,14,15]}

df = pd.DataFrame(dict_data, index = [4,5,6])
print(df)


df_2 = pd.DataFrame([[15,'man', 'a'],[17,'women', 'b']], index = ['name1', 'name2'], columns=['age', 'm/w', 'school'])
print(df_2)


#삭제
exam_data = {'math': [90,80,70], 'english':[98,87,57], 'music':[80,75,96], 'sci':[84,98,100]}
df1 = pd.DataFrame(exam_data, index = ['a', 'b', 'c'])
print(df1)

df2 = df1[:]
df2.drop('a', inplace = True)
print(df2)

df3 = df1[:]
df3.drop(['a', 'b'], inplace= True)
print(df3)



df = pd.DataFrame(exam_data, index = ['a', 'b', 'c'])
print(df)

print("\n")

label1 = df.loc['a']
position1 = df.iloc[0]
print(label1)
print("\n")
print(position1)

print("\n")

label2 = df.loc[['a', 'b']]
position2 = df.iloc[[0,1]]
print(label2)
print("\n")
print(position2)

print("\n")

label3 = df.loc['a':'c']
position3 = df.iloc[0:2]
print(label3)
print("\n")
print(position3)





exam_data = {'name':['a','b','c'], 'math': [75,98,65], 'eng':[75,89,62], 'sci':[78,95,87]}
df = pd.DataFrame(exam_data)
print(df)

print("\n")

math1 = df["math"]
math2 = df.math
print(math1)
print("\n")
print(math2)

print('\n')

math_eng = df[['math','eng']]
print(math_eng)



exam_data = {'name':['a','b','c'], 'math': [75,98,65], 'eng':[75,89,62], 'sci':[78,95,87]}
df = pd.DataFrame(exam_data, index = ['kang','lee','kim'])

print(df)







