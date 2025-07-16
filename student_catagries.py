import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "./dataset.csv"  # Change to your file path
df = pd.read_csv(file_path)

# Define classification function
def classify_student(cgpa):
    if cgpa >= 3.5:
        return "High Achiever"
    elif 2.5 <= cgpa < 3.5:
        return "Average"
    else:
        return "struggling"

# Apply classification
df["Academic Category"] = df["CGPA"].apply(classify_student)

# Count category distribution
category_counts = df["Academic Category"].value_counts()

# Plot the distribution
plt.figure(figsize=(8, 5))

category_counts.plot(kind="bar",color=['blue','green','red'])

# Labels and title
plt.xlabel("Academic Category")
plt.ylabel("Number of S""tudents")
plt.title("Distribution of Academic Success Categories")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="-", alpha=0.7)

# Show the plot
plt.show()
