import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "dataset.csv"
df = pd.read_csv(file_path)

# Group data by Gender and calculate mean for CGPA and SGPA
gender_performance = df.groupby("Gender")[["CGPA", "CGPA100", "CGPA200", "CGPA300", "CGPA400", "SGPA"]].mean()

# Plot performance trend over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=gender_performance.T, marker="o")     
plt.title("Academic Performance Trend by Gender")
plt.xlabel("Year of Study")
plt.ylabel("Average GPA")
plt.legend(title="Gender")
plt.grid()
plt.show()
