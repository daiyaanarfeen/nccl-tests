import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--nproc', type=int)
parser.add_argument('--nnode', type=int)
args = parser.parse_args()

data = pd.read_csv('output.csv', header=None)
if os.path.exists('./results_nproc=%d,nnode=%d.csv'%(args.nproc, args.nnode)):
    results = pd.read_csv('results_nproc=%d,nnode=%d.csv'%(args.nproc, args.nnode), header=None)
    results[-1] = data.iloc[:, 6]
    results.to_csv('results_nproc=%d,nnode=%d.csv'%(args.nproc, args.nnode), header=None, index=False)
else:
    data.iloc[:, 6].to_csv('results_nproc=%d,nnode=%d.csv'%(args.nproc, args.nnode), header=None, index=False)
