import pandas as pd
import numpy as np
Data = pd.read_csv('Data/student.csv')
df=pd.DataFrame(Data)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
# print(df.info())
df.info()
print(df.describe())
print(df.sample(2))
print(df.dtypes)
df["Joining_Date"]=pd.to_datetime(df["Joining_Date"])

invalid_Marks=df[df["Marks"]>100]
print(invalid_Marks)
invalid_attendenc=df[df["Attendance"]>100]
print(invalid_attendenc[["Student_ID","Name"]])
missing_values=df.isnull().sum()
print(missing_values)
duplicates = df.duplicated().sum()
print(duplicates)



