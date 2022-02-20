##author:ROHAN
##read params
## processing
## return dataframe
import os 
import yaml
import pandas as pd
import numpy as np
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config
def get_data(config_path):
    config=read_params(config_path)
    print(config)
    data_path=config["data_source"]["s3_source"]
    data=pd.read_csv(data_path,sep=",")
    print(data.head())
    return data



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed__args=args.parse_args()
    data=get_data(config_path=parsed__args.config)

