import pandas as dp

data = data = {"Name":["john","Anna","Peter","Mike","Sara"],
        "Age":[28,35,22,41,30],
        "Score":[90,85,92,75,69]}
df = dp.DataFrame(data)

print("Statistical analysis with pandas \n-------------")
total_score = df["Score"].sum()
print(f"The total Score:{total_score}")

max_age = df["Age"].max()
print(f"The maximum age:{max_age}")

average_score = df["Score"].mean()
print(f"The average Score:{average_score}")

rowcount = df.shape[0]
print(f"Number of rows:{rowcount}")