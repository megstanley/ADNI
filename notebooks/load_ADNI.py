from scipy.io import loadmat
import os
import numpy as np
from pathlib import Path
import pandas as pd

def find_data_path():
    '''
    Returns path of the data
    '''
    here_dir    = os.path.dirname(os.path.realpath('__file__'))
    par_dir = os.path.abspath(os.path.join(here_dir, os.pardir))
    dataset_dir = os.path.join(par_dir, 'data')
    return dataset_dir

def load_baselines_into_dataframes():
    '''
    Returns array (1x3) of dictionaries containing data for years (1,3,5) of ADNI patients
    '''
    dataset_dir = find_data_path()
    adni = [Path(dataset_dir + 'vec_a2b_1y_atr_factor.mat'),
            Path(dataset_dir + 'vec_a2b_3y_atr_factor.mat'),
            Path(dataset_dir + 'vec_a2b_5y_atr_factor.mat')]
    adni = [loadmat(adni[0]),loadmat(adni[1]),loadmat(adni[2])]

    #ignore the metadata on .mat file and load the actual matrices
    adni = [adni[0]['vec_a2b_1y_atr_factor'],adni[1]['vec_a2b_3y_atr_factor'],adni[2]['vec_a2b_5y_atr_factor']]

    #create pandas dataframe with desired names
    adni_df = [pd.DataFrame({
                        'ID'                        : [int(adni[j][i][0]) for i in range(len(adni[j]))],
                        'Baseline Dx'               : [int(adni[j][i][1]) for i in range(len(adni[j]))],
                        '1y Dx'                     : [int(adni[j][i][2]) for i in range(len(adni[j]))],
                        'End-of-study Dx'           : [int(adni[j][i][3]) for i in range(len(adni[j]))],
                        'Baseline atrophy'          : [adni[j][i][4:90] for i in range(len(adni[j]))],
                        'Future atrophy'            : [adni[j][i][90:176] for i in range(len(adni[j]))],
                        'Genetic Info (APOE4)'      : [adni[j][i][176] for i in range(len(adni[j]))],
                        'bl Age'                    : [adni[j][i][177] for i in range(len(adni[j]))],
                        'gender'                    : [adni[j][i][178] for i in range(len(adni[j]))],
                        'education year'            : [adni[j][i][179] for i in range(len(adni[j]))],
                        'marriage'                  : [adni[j][i][180] for i in range(len(adni[j]))],
                        'bl ADAS11'                 : [adni[j][i][181] for i in range(len(adni[j]))],
                        'bl ADAS13'                 : [adni[j][i][182] for i in range(len(adni[j]))],
                        'bl RAVLT_immediate'        : [adni[j][i][183] for i in range(len(adni[j]))],
                        'bl RAVLT_learning'         : [adni[j][i][184] for i in range(len(adni[j]))],
                        'bl RAVLT_forgetting'       : [adni[j][i][185] for i in range(len(adni[j]))],
                        'bl RAVLT_perc_forgetting'  : [adni[j][i][186] for i in range(len(adni[j]))],
                        'bl FAQ'                    : [adni[j][i][187] for i in range(len(adni[j]))],
                        'bl CDR'                    : [adni[j][i][188] for i in range(len(adni[j]))],
                        'bl MMSE'                   : [adni[j][i][189] for i in range(len(adni[j]))],
                        'ft Age'                    : [adni[j][i][190] for i in range(len(adni[j]))],
                        'gender'                    : [adni[j][i][191] for i in range(len(adni[j]))],
                        'education year'            : [adni[j][i][192] for i in range(len(adni[j]))],
                        'marriage'                  : [adni[j][i][193] for i in range(len(adni[j]))],
                        'ft ADAS11'                 : [adni[j][i][194] for i in range(len(adni[j]))],
                        'ft ADAS13'                 : [adni[j][i][195] for i in range(len(adni[j]))],
                        'ft RAVLT_immediate'        : [adni[j][i][196] for i in range(len(adni[j]))],
                        'ft RAVLT_learning'         : [adni[j][i][197] for i in range(len(adni[j]))],
                        'ft RAVLT_forgetting'       : [adni[j][i][198] for i in range(len(adni[j]))],
                        'ft RAVLT_perc_forgetting'  : [adni[j][i][199] for i in range(len(adni[j]))],
                        'ft FAQ'                    : [adni[j][i][200] for i in range(len(adni[j]))],
                        'ft CDR'                    : [adni[j][i][201] for i in range(len(adni[j]))],
                        'ft MMSE'                   : [adni[j][i][202] for i in range(len(adni[j]))],
                        'bl Intracranial Volume'    : [adni[j][i][203] for i in range(len(adni[j]))],
                        'ft Intracranial Volume'    : [adni[j][i][204] for i in range(len(adni[j]))],
                        'end-of-study is_convert'   : [adni[j][i][205] for i in range(len(adni[j]))],
                        'number of months from bl'  : [adni[j][i][206] for i in range(len(adni[j]))]
                         }) for j in range(3)]
    return(adni_df)

def test_pathfinder():
    find_data_path()

def main():
    adni_df = load_baselines_into_dataframes()
    adni_df[0]['Future atrophy']
    # adni_df[0]

if __name__ == "__main__":
    #main()
    test_pathfinder()
