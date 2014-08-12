#!/usr/bin/python

#Author: Duncan Campbell
#Written: August 14, 2013
#Yale University
#Description: Read in hdf5 CFHTLS photo-z catalogues and write a version with fewer columns.
#    id,ra,dec, and xyz vectors

###packages###
import numpy as np
import h5py
import sys

def main():
    ###make sure to change these when running in a new enviorment!###
    #location of data directory
    filepath = '/scratch/dac29/output/processed_data/CFHTLens/catalogues/'
    #################################################################
  
    fields=['W1','W2','W3','W4']

    for field in fields:
        filename = field
        print 'running for:', field
        f =  h5py.File(filepath+filename+'.hdf5', 'r')
        dset = f.get(field)
  
        dtype=[('id','S13'),('ra','<f8'),('dec','<f8'),('x','<f8'),('y','<f8'),('z','<f8')]
        dtype = np.dtype(dtype)
        data = np.recarray((len(dset),), dtype=dtype)

        data['id']  = dset['id']
        data['ra']  = dset['ALPHA_J2000']
        data['dec'] = dset['DELTA_J2000']

        print 'converting ra,dec coordinates into vectors...'
        x, y, z = spherical_to_cartesian(dset['ALPHA_J2000'],dset['DELTA_J2000'], threads=4)
        data['x'] = x
        data['y'] = y
        data['z'] = z

        print 'saving hdf5 version of the catalogue...'
        filename = filename+'_abbreviated'
        f = h5py.File(filepath+filename+'.hdf5', 'w')
        dset = f.create_dataset(field, data=data)
        f.close()

def spherical_to_cartesian(ra, dec, threads=1):
    """
    Inputs in degrees.  Outputs x,y,z
    """
    import numexpr as ne
    import math

    ne.set_num_threads(threads)

    pi = math.pi
    rar = ne.evaluate('ra*pi/180.0')
    decr = ne.evaluate('dec*pi/180.0')

    hold1=ne.evaluate('cos(decr)') 

    x = ne.evaluate('cos(rar) * hold1')
    y = ne.evaluate('sin(rar) * hold1')
    z = ne.evaluate('sin(decr)')
 
    return x, y, z

if __name__ == '__main__':
    import argparse
    main()
