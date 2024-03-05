import yaml


def update_path(data_version: str, path_to_project: str) -> None:
    path_to_data = f"{path_to_project}/tree-type-detection-{data_version}"

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


def convert_bbox_format(prediction):
    # Extract information from the prediction object
    image_path = prediction.path.split("\\")[-1]  # Extract image name
    box = prediction.boxes.xyxy.tolist()[
        0
    ]  # Get top-left and bottom-right coordinates

    # Calculate width and height
    width = box[2] - box[0]
    height = box[3] - box[1]

    return [image_path, box[0], box[1], width, height]


def get_f1(results_dict) -> float:
    return 2 / (
        (1 / results_dict["metrics/precision(B)"])
        + (1 / results_dict["metrics/recall(B)"])
    )
