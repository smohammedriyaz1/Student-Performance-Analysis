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

import matplotlib.pyplot as plt 

dept_count=df["Department"].value_counts()
print(dept_count)
dept_count.plot(kind="bar")
plt.title("student of each dept")
plt.xlabel("dept")
plt.ylabel("Number of students")
plt.savefig("images/department_chart.png")
plt.show()

#----------- Average Marks by Department-----------------
import matplotlib.pyplot as plt
avg_marks=df.groupby("Department")["Marks"].mean()
plt.plot(avg_marks.index,avg_marks.values,marker="o")
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.savefig("images/avg_marks_chart.png")
plt.show()

# --------------------bar
# import matplotlib.pyplot as plt
# avg_marks = df.groupby("Department")["Attendance"].mean()
# plt.plot(
#     avg_marks.index,
#     avg_marks.values,
#     color="green",
#     linestyle="--",
#     marker="o",
#     markersize=10,
#     linewidth=3
# )
# plt.title("Average Attendance by Department")
# plt.xlabel("Attendance")
# plt.ylabel("Average Attendance")
# plt.grid(True)
# plt.savefig("images/avg_attendence.png")
# plt.show()

# -------------pie

# import matplotlib.pyplot as plt
# gender_count = df["Gender"].value_counts()
# plt.figure(figsize=(6,6))
# plt.pie(
#     gender_count,
#     labels=gender_count.index,
#     autopct="%1.1f%%"
# )
# plt.title("Gender Distribution")
# plt.savefig("images/Gender_pie.png")
# plt.show()

# # --------------histogram

# plt.figure(figsize=(7,5))
# plt.hist(
#     df["Marks"],
#     bins=5,
#     color="orange",
#     edgecolor="black"
# )
# plt.title("Distribution of Student Marks")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.grid(axis="y") #horizontal lines  #plt.grid(True)   vertical lines   #plt.grid(axis="x") oth
# plt.savefig("images/dismarks_hist.png")
# plt.show()

# --------------scatter

# import matplotlib.pyplot as plt
# plt.figure(figsize=(7,5))
# plt.scatter(
#     df["Attendance"],
#     df["Marks"],
#     color="blue",
#     marker="o",
#     s=100
# )
# plt.title("Marks vs Attendance")
# plt.xlabel("Attendance")
# plt.ylabel("Marks")
# plt.grid(True)
# plt.savefig("images/imgvsattnd_scatter.png")
# plt.show()


# ------boxplot----

# plt.figure(figsize=(7,5))
# plt.boxplot(
#     df["Marks"],
#     vert=False,
#     showmeans=True,
#     patch_artist=True
# )
# plt.title("Marks vs Attendance")
# plt.grid(True)
# plt.show()

# --------method 1
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))

# ------------------------
plt.subplot(2,2,1)

dept = df["Department"].value_counts()

plt.bar(dept.index, dept.values)

plt.title("Departments")

# ------------------------
plt.subplot(2,2,2)

plt.hist(df["Marks"], bins=5)

plt.title("Marks")

# ------------------------
plt.subplot(2,2,3)

plt.scatter(df["Attendance"], df["Marks"])

plt.title("Attendance vs Marks")

# ------------------------
plt.subplot(2,2,4)

plt.boxplot(df["Marks"])

plt.title("Marks Boxplot")

plt.tight_layout()

plt.show()

#-------method2
fig, ax = plt.subplots(2,2,figsize=(12,8))
# Graph 1
dept = df["Department"].value_counts()
ax[0][0].bar(dept.index, dept.values)
ax[0][0].set_title("Students by Department")
# Graph 2
ax[0][1].hist(df["Marks"], bins=5)
ax[0][1].set_title("Marks Distribution")
#Graph 3
ax[1][0].scatter(
    df["Attendance"],
    df["Marks"]
)
ax[1][0].set_title("Attendance vs Marks")
#Graph 4
ax[1][1].boxplot(df["Marks"])
ax[1][1].set_title("Marks Box Plot")
plt.tight_layout()
plt.savefig("images/dashboard.png")
plt.show()