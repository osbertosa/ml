import os
from box.exceptions import BoxError
import yaml
from src.ml import logger
import json
import joblib
from ensure import ensure_annotations
from box import configbox
from pathlib import Path
from typing import Any
import base64
from beartype import beartype
from box.exceptions import BoxValueError

@beartype
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads YAML file and returns 
    Args:
        path_to_yaml (str): Path  like input 

        Raises:
        ValueError: If the YAML file is empty
        e: empty file error
        
    Returns:
        configbox.ConfigBox type 
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("The YAML file is empty.")
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('YAML file is empty')
    except Exception as e:
        raise e
    

@beartype
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of  directories 
    Args:
        path_to_directories (list): List of paths to directories
        ignore_log (bool, optional): ignore if multiple dir are created. defaults to False
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")


@beartype
def  save_jason(path_to_json: str, data: dict) :
    """
    Save json data to file
 
    Args:
        path (str): Path to the json file
        data (dict): Data to be saved in json file
    """
with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"json file saved at: {path}")
        


@beartype
def load_json(path: str) -> configbox:
    """
    load json files data 

    Args:
        path (path): Path to the json file

    Returns:
        configbox: data as class attribution instead of dict
    """

    with open(path) as f:
        content = json.load(f)
        logger.info(f"json file loaded successfully from: {path}")
        return configbox(content)
    
@beartype
def save_bin(data:Any, path :path):

    """
    Save  binary file 

    Args:
        data (Any): Data to be saved as binary
        path (path): Path to the binary file
    """
    joblib.dump(value data,  filename path)
    logger.info(f" binary  file saved  at: {path}")

@beartype
def load_bin(path:path) -> Any:
    """
    Load binary data 

    Args:
        path (path): Path to the binary file

    Returns:
        Any: object stored in the  file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded  from: {path}")
    return data

@beartype
def get_size(path:path) -> str:
    """
    Get size in KB

    Args:
        path (path): Path of  the file
    Returns:
        str: Size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return  f'~ {size_in_kb} KB'

def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())
        
        
    