import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# Number of students
n = 1000

# Generate student data
data = {
    "Student_ID": [f"STU{i:04d}" for i in range(1, n + 1)],
    "Study_Hours": np.round(np.random.uniform(0.5, 8, n), 1),
    "Attendance": np.round(np.random.uniform(40, 100, n), 1),
    "Previous_Marks": np.round(np.random.uniform(30, 100, n), 1),
    "Assignments": np.round(np.random.uniform(20, 100, n), 1),
    "Internal_Marks": np.round(np.random.uniform(20, 100, n), 1)
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a performance score
performance_score = (
    df["Study_Hours"] * 3
    + df["Attendance"] * 0.2
    + df["Previous_Marks"] * 0.3
    + df["Assignments"] * 0.15
    + df["Internal_Marks"] * 0.25
)

# Add some randomness to make the dataset more realistic
performance_score += np.random.normal(0, 8, n)

# Create Pass/Fail result
df["Final_Result"] = np.where(
    performance_score >= 50,
    "Pass",
    "Fail"
)

# Save dataset
df.to_csv("dataset/student_performance.csv", index=False)

print("Dataset created successfully!")
print(f"Total students: {len(df)}")
print("\nFirst 5 records:")
print(df.head())