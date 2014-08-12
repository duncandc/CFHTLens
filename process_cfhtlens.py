#!/usr/bin/python

#Author: Duncan Campbell
#Written: August 14, 2013
#Yale University
#Description: Read in hdf5 CFHTLS photo-z catalogues and process the pdz column into something more useable.

###packages###
import numpy as np
import h5py
import sys

def main():
    ###make sure to change these when running in a new enviorment!###
    #location of data directory
    filepath = '/scratch/dac29/output/processed_data/CFHTLens/catalogues/'
    savepath = filepath
    #################################################################

    print ''
    field = 'W4'
    filename = field
    print filename
    f =  h5py.File(filepath+filename+'.hdf5', 'r')
    dset = f.get(field)
    print 'length:', len(dset)
    print 'columns:'
    for name in dset.dtype.descr: print name

    dtype = dset.dtype.descr
    dtype[69]=('PZ_full', np.float64, (70,))
    dtype = np.dtype(dtype)

    string = np.array(dset['PZ_full'])

    W = np.recarray((len(dset),),dtype=dtype)

    
    for i in range(0,69):
        print i
        W[W.dtype.names[i]] = dset[W.dtype.names[i]]
    for i in range(0,len(W)):
        print i
        W[W.dtype.names[69]][i] = np.array([float(x) for x in string[i].split(',')])
    for i in range(70,100):
        print i
        W[W.dtype.names[i]] = dset[W.dtype.names[i]]   
        
    f = h5py.File(savepath+field+'_processed.hdf5', 'w')
    dset = f.create_dataset(field, data=W)
    f.close()
    

if __name__ == '__main__':
  main()
