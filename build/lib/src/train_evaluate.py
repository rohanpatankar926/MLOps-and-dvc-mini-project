#load train and test
#model evaluation
#save metrics,params

import os 
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from get_data import read_params
import joblib
import json

def eval_metrics(act,pred):
    rmse=np.sqrt(mean_squared_error(act,pred))
    mae=mean_absolute_error(act,pred)
    r2=r2_score(act,pred)
    return rmse,mae,r2
def model_evaluation(config_path):
    config=read_params(config_path)
    test_data=config["split_data"]["test_path"]
    train_data=config["split_data"]["train_path"]
    model_dir=config["model_dir"]
    
    alpha=config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio=config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    
    target=[config["base"]["target_col"]]
    
    train=pd.read_csv(train_data,sep=",")
    test=pd.read_csv(test_data,sep=",")
    
    y_train=train[target]
    y_test=test[target]
    
    x_train=train.drop(target,axis=1)
    x_test=test.drop(target,axis=1)
    
    lr=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=42)
    
    lr.fit(x_train,y_train)
    y_pred=lr.predict(x_test)
    
    (rmse,mae,r2)=eval_metrics(y_test,y_pred)
    print(rmse,mae,r2)
    
    os.makedirs(model_dir,exist_ok=True)
    model_path=os.path.join(model_dir,"model.joblib")
    joblib.dump(lr,model_path)
    
    scores_file=config["reports"]["scores"]
    params_file=config["reports"]["params"]
    
    
    
    with open(scores_file,"w") as f:
        score={
            "rmse":rmse,
            "mae":mae,
            "r2_score":r2
        }
        json.dump(score,f,indent=4)
    with open(params_file,"w") as f:
        metrics={
            "alpha":alpha,
            "l1 ratio":l1_ratio
        }
        json.dump(metrics,f,indent=4)
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    model_evaluation(config_path=parsed_args.config)