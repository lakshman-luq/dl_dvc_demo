from src.utils.all_utils import read_yaml, create_directory
import argparse, os
import pandas as pd 
import shutil
from tqdm import tqdm

def copy_file(source, local):
    list_of_files = os.listdir(source)
    N = len(list_of_files)
    for file in tqdm(list_of_files, total=N, desc=f'copying file from {source} to {local}', colour='green'):
        src = os.path.join(source, file)
        dest = os.path.join(local, file)
        shutil.copy(src, dest)

def get_data(config_path):
    config = read_yaml(config_path)

    source_download_dirs = config['source_download_dirs']
    local_data_dirs = config['local_data_dirs']

    for source_download_dir, local_data_dir in tqdm(zip(source_download_dirs, local_data_dirs), total=2, desc= 'list of folders', colour='red'):
        create_directory([local_data_dir])
        copy_file(source_download_dir, local_data_dir)

if __name__=="__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)