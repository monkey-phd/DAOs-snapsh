import os
# Import relevant libraries
import pandas as pd

# working directory to the parent directory of the script's location
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load the CSV file
follows = pd.read_csv("input/snapshot-hub-mainnet-2023-08-30-follows_0.csv")

# Rename columns for clarity
follows.rename(columns={"created": "start_follow_space"}, inplace=True)

# Select only the specified columns
selected_columns = follows[["follower", "space", "start_follow_space"]]

# Save the DataFrame as a CSV file
selected_columns.to_csv("processed/follows.csv", index=False)

# Save the DataFrame as a pickle file
selected_columns.to_pickle("processed/follows.pkl")
