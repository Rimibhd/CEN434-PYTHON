import pandas as pd

# Create a list of data
data = [
    ["Alice", 25, "Marketing"],
    ["Bob", 30, "Engineering"],
    ["Charlie", 22, "Sales"],
]

# Create a DataFrame from the list
df = pd.DataFrame(data, columns=["Name", "Age", "Department"])

# Print the DataFrame
print(df)

# Access specific data using indexing and slicing
name = df["Name"][1]
age_range = df["Age"][:2]

# Perform calculations on data
average_age = df["Age"].mean()

# Filter data based on conditions
marketing_employees = df[df["Department"] == "Marketing"]

# Sort data by a column
sorted_by_age = df.sort_values(by="Age")

# Create new columns based on existing data
df["Years of Experience"] = df["Age"] - 22

# Print specific information
print(f"Bob's age: {name}")
print(f"Average age: {average_age:.2f}")
print(f"Marketing employees: {marketing_employees}")

# Demonstrate additional features
print(df.describe())  # Generate descriptive statistics
print(df.head(2))  # Show the first 2 rows
print(df.tail(1))  # Show the last row

# This script demonstrates basic features of pandas like:
# - Creating DataFrames
# - Accessing data
# - Performing calculations
# - Filtering data
# - Sorting data
# - Creating new columns
# - Generating descriptive statistics
# - Selecting specific rows
