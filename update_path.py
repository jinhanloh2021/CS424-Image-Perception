import os
import yaml
from dotenv import load_dotenv

load_dotenv()
data_version = os.getenv("DATA_VERSION")
path_to_data = (
    f'{os.getenv("PATH_TO_PROJECT")}/tree-type-detection-{data_version}'
)

# Define the path to the data.yaml file
yaml_path = f"{path_to_data}/data.yaml"

# Get the absolute file paths of the test, train, and valid directories
test_path = f"{path_to_data}/test"
train_path = f"{path_to_data}/train"
valid_path = f"{path_to_data}/valid"

# Load the data.yaml file
with open(yaml_path, "r") as file:
    data = yaml.safe_load(file)

# Update the test, train, and valid paths
data["test"] = test_path
data["train"] = train_path
data["val"] = valid_path

# Write the updated data to the data.yaml file
with open(yaml_path, "w") as file:
    yaml.dump(data, file)
