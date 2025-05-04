import pandas as dp

data = {"Name":["john","Anna","Peter","Mike","Sara"],
        "Age":[28,35,22,41,30],
        "TestScore":[90,85,92,75,69]}  

df = dp.DataFrame(data)

total_score = df["Score"].sum()
print(f"Total Score:{total_score}")
