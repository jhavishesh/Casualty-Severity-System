# Read the dataset
import pandas as pd

# Correct Google Drive link format
file_id = "1-SpAaFjNLra-KVwTh626rkSQlI0ZmHZX"
url = f"https://drive.google.com/uc?export=download&id={file_id}"
data = pd.read_csv(url)

# Show first few rows
data.head(3)

# Select independent variables (excluding column 5 which you wanted to delete)
independent_variables = data.columns.tolist()
independent_variables.remove(independent_variables[5])
data1 = data[independent_variables]

# Perform clustering to prepare a clustered dataset
from sklearn.cluster import AgglomerativeClustering
agg_cluster = AgglomerativeClustering(n_clusters=3)

# Train the agglomerative clustering model
agg_cluster.fit(data1)

# Predict the cluster label
data["Cluster Labels"] = agg_cluster.fit_predict(data1)

# Select dependent (Y) and independent variables (X)
Y = data["Casualtysev"]
independent_variables = data.columns.tolist()
independent_variables.remove("Casualtysev")  # Remove the target column
X = data[independent_variables]

# Classify using Gradient Boosted Trees
from sklearn.ensemble import GradientBoostingClassifier
gbc = GradientBoostingClassifier()

# Train the model
gbc.fit(X, Y)

# Predict using GBC Classifier
data["Predicted Casualty Severity"] = gbc.predict(X)

# Take a user input and predict casualty severity
independent_variables.remove("Cluster Labels")  # Removing cluster labels from input for user input

# Take user input and predict casualty severity
user_input = {}
for var in independent_variables:
    temp = input(f"Enter {var}: ")
    # Cast input to appropriate type (assuming everything is numeric here)
    try:
        user_input[var] = float(temp)
    except ValueError:
        user_input[var] = temp  # If it's a string, leave it as is

# Convert user input to DataFrame
user_df = pd.DataFrame(data=user_input, index=[0])

# Add user input to the dataset and calculate cluster labels
data1 = pd.concat([data1, user_df], ignore_index=True)

# Recalculate the cluster labels for the new user input
user_df["Cluster Labels"] = agg_cluster.fit_predict(data1)[-1]  # Get cluster for the last input row

# Ensure the columns in the user input are in the same order as during model training
user_request = user_df[X.columns]

# Predict severity for user input
severity = gbc.predict(user_request)[0]

# Print the severity based on prediction
if severity == 1:
    print("Casualty Severity is Slight (1)")
elif severity == 2:
    print("Casualty Severity is Severe (2)")
elif severity == 3:
    print("Casualty Severity is Fatal (3)")
