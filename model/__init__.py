import torch
import pickle
import numpy as np
import pandas as pd
import glob
import os

__all__ = ['get_best_checkpoint_path']

def get_best_checkpoint_path(checkpoint_directory, sort_by='val_loss'):
    checkpoint_file_names = glob.glob(os.path.join(checkpoint_directory, '*.ckpt'))
    #print(checkpoint_file_names) #['models/son_height_regression_model/son_height_regression_model-epoch=29-val_loss=0.00.ckpt', 'models/son_height_regression_model/son_height_regression_model-epoch=29-val_loss=0.00-v1.ckpt']
    best_checkpoint_path = None
    def sort_func(checkpoint_file_name, sort_by=sort_by):
        for token in checkpoint_file_name.split('-'):
            if '=' in token:
                li = token.split('=')
                name = li[0]
                value = li[1]
                if '.ckpt' in value:
                    value = value.split('.ckpt')[0]
                if name == sort_by:
                    return float(value)
    checkpoint_file_names.sort(key=sort_func)
    best_checkpoint_path = checkpoint_file_names[0]
    return best_checkpoint_path
