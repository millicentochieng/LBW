import pandas as  pd

def get_data(path):
    '''Read data in csv format'''
    with open (path, 'r') as datafile:
        df = pd.read_csv(datafile)
        return df