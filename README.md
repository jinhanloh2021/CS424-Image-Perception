# SMU Logo bounding box detection

Design an algorithm to identify all images of SMU from a set of random images. A bounding box should be drawn around the SMU logo whenever it appears in an image.

When an SMU logo occurs in an image, a bounding box should be drawn around it. Logo identification will be evaluated by its F1 score.

## Setup

Install dependencies

```bash
pip install -r requirements.txt

```

Install PyTorch manually, as it depends on your CUDA versions and GPU. PyTorch 2.2.1 with CUDA 11.8 works for me. See [docs](https://pytorch.org/get-started/locally/) for setup.
Add the environment variables in a `.env` file. Adjust the train settings based on your GPU specifications.
Create an empty `/predictions` folder for the output of predicted images.

## Run

Run the jupyter notebook.
