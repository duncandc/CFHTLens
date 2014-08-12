#!/usr/bin/python

#Author: Duncan Campbell
#Written: August 14, 2013
#Yale University
#Description: Read in hdf5 CFHTLS photo-z catalogues and print out column names

###packages###
import numpy as np
import h5py
import sys

def main():
    ###make sure to change these when running in a new enviorment!###
    #location of data directory
    filepath = '/scratch/dac29/output/processed_data/CFHTLens/catalogues/'
    #################################################################

    print ''
    field = 'W1'
    filename = field
    print filename
    f =  h5py.File(filepath+filename+'.hdf5', 'r')
    dset = f.get(field)
    print 'length:', len(dset)
    print 'columns:'
    i=0
    for name in dset.dtype.descr: 
        print i, name
        i=i+1
    f.close()

    print ''
    field = 'W1'
    filename = field+'_abbreviated'
    print filename
    f =  h5py.File(filepath+filename+'.hdf5', 'r')
    dset = f.get(field)
    print 'length:', len(dset)
    print 'columns:'
    for name in dset.dtype.descr: print name
    f.close()

    
    
    

if __name__ == '__main__':
  main()
