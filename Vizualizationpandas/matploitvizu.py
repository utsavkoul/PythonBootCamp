import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("employees.csv")
print(df)
print(df.describe())
print(df.head())
# No of missing values in each column
mv = df.isnull().sum()
print("Missing Values:", mv)
# Average of Salary Column
avg = df["Salary"].mean()
print(f"Average Salary is {avg}")
uv = df["Team"].nunique()
print("Unique Values of Team are :",uv)
leg_emp = df[df["Team"] == "Legal"]
print(leg_emp)
max_salary = df["Salary"].max()
max_salary_emp = df[df["Salary"]==max_salary]
print("Maximum Salary Employee", max_salary_emp)
team_count = df["Team"].value_counts()
print("Employee in each Team", team_count)

sort = df.sort_values(by="Salary", ascending=False)
print("Sort values:",sort)
plt.figure(figsize = (10,10))
plt.pie(team_count, labels = team_count.index, autopct="%1.1f%%", startangle=140)
plt.title("Teams")
plt.show()