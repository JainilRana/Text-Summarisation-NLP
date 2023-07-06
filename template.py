import os
from pathlib import Path
import logging

# this will log all the changes during runtime
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    # this acts as the yaml file while doing CICD deployment, so on commit it will automatically commit in deployment
    ".github.com/workflows/.gitkeep",
    # wherever the constructor file is present it is called the local package (aka. folder)
    f"src/{project_name}/_init_.py", # this construction file is required whenever we will the install local package 
    f"src/{project_name}/components/_init_.py",
    f"src/{project_name}/utils/_init_.py",
    f"src/{project_name}/utils/common.py", # this file contains all the utilities
    f"src/{project_name}/logging/_init_.py",
    f"src/{project_name}/config/_init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init_.py", # this file contains the training and prediction pipeline
    f"src/{project_name}/entity/_init_.py",
    f"src/{project_name}/constant/_init_.py",
    "config/config.yaml",
    "params.yaml", # contails all the model related params
    "app.py",
    "main.py",
    "Dockerfile.txt",
    "setup.py", # ths will help in local package setup
    "research/trials.ipynb", # contains all the jupyter notebooks
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) # it will detect OS and give path
    # for seperating folder and file
    filedir, filename = os.path.split(filepath)
    # checking for empty directory

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    # if file does not exist ie. size of the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} is already existing")
