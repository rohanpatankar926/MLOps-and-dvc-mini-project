# raw data splitting
# save it in data/processed folder


import os 
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def train_test_split_and_save(config_path):
    config=read_params(config_path)
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    train_data=config["split_data"]["train_path"]
    test_data=config["split_data"]["test_path"]
    split_ratio=config["split_data"]["test_size"]
    # rand_state=config["base"]["random_state"]
    
    data=pd.read_csv(raw_data_path,sep=",")
    train,test=train_test_split(data,test_size=split_ratio,random_state=42)
    train.to_csv(train_data,sep=",",index=False,encoding="UTF-8")
    test.to_csv(test_data,sep=",",index=False,encoding="UTF-8")
    
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data=train_test_split_and_save(config_path=parsed_args.config)