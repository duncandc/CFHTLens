#!/usr/bin/python

#Author: Duncan Campbell
#Written:  August 14, 2013
#Yale University
#Description: Read in ascii CFHTLS photo-z catalogues and save as HDF5 files.
#data from: ftp://ftpix.iap.fr/pub/CFHTLS-zphot-T0007/

###packages###
import sys
import glob
import gc
import h5py
import custom_utilities as cu
from astropy.io import ascii

def main():
    filepath = cu.get_data_path() + 'CFHTLens/queries/'
    savepath = cu.get_output_path() + 'processed_data/CFHTLens/catalogues/'

    filenames = glob.glob('/scratch/dac29/data/CFHTLens/queries/*.tsv')
    for filename in filenames: print filename


    field = 'test'
    print 'reading in:',field
    filename = 'test.tsv'
    data = ascii.read(filepath+filename, delimiter='\t', \
                      guess=True, Reader=ascii.Basic)
    print 'saving as hdf5 file...'
    f = h5py.File(savepath+field+'.hdf5', 'w')
    dset = f.create_dataset(field, data=data)
    f.close()
    gc.collect()
    print 'done.'

    '''
    #let's split this field into two parts...
    field='W1'
    print 'reading in:',field, 'part 1'
    filename = 'CFHTLens_2013-09-03T20:10:04.tsv'
    data = ascii.read(filepath+filename, delimiter='\t', \
                    guess=True, Reader=ascii.Basic, data_end=5114944)
    print 'saving as hdf5 file...'
    f = h5py.File(savepath+field+'_1.hdf5', 'w')
    dset = f.create_dataset(field, data=data)
    f.close()
    data = 0
    gc.collect()
    print 'done.'

    field='W1'
    print 'reading in:',field, 'part 2'
    filename = 'CFHTLens_2013-09-03T20:10:04.tsv'
    data = ascii.read(filepath+filename, delimiter='\t', \
                    guess=True, Reader=ascii.Basic, data_start=5114945)
    print 'saving as hdf5 file...'
    f = h5py.File(savepath+field+'_2.hdf5', 'w')
    dset = f.create_dataset(field, data=data)
    f.close()
    data = 0
    gc.collect()
    print 'done.'

    #combine the wo parts into one big set!!!
    field = 'W1'
    f1 = h5py.File(savepath+field+'_1.hdf5', 'r')
    dset1 = f1.get(field)
    f2 = h5py.File(savepath+field+'_2.hdf5', 'r')
    dset2 = f2.get(field)
    f = h5py.File(savepath+field+'.hdf5', 'w')
    print dset1.dtype
    length = len(dset1)+len(dset2)
    dset = f.create_dataset(field, (length,), dtype=dset1.dtype)
    print 'len(dset1)=',len(dset1),'len(dset2)=', len(dset2),\
          'len(dset1)+len(dset2)=', len(dset1)+len(dset2), 'len(dset)=', len(dset)
    print len(dset[0:len(dset1)]), len(dset[len(dset1):len(dset1)+len(dset2)+1])
    print len(dset[0:len(dset1)]), len(dset[len(dset1):len(dset1)+len(dset2)])
    print 0,len(dset1),len(dset1)+1, len(dset1)+len(dset2)+1
    dset[0:len(dset1)] = dset1
    dset[len(dset1):len(dset1)+len(dset2)+1] = dset2
    f1.close()
    f2.close()
    f.close()
    dset=0
    dset1=0
    dset2=0
    gc.collect()
    '''
    
    field='W2'
    print 'reading in:',field
    filename = 'CFHTLens_2013-09-03T20:15:29.tsv'
    data = ascii.read(filepath+filename, delimiter='\t', \
                    guess=True, Reader=ascii.Basic)
    print 'saving as hdf5 file...'
    f = h5py.File(savepath+field+'.hdf5', 'w')
    dset = f.create_dataset(field, data=data)
    f.close()
    data = 0
    gc.collect()
    print 'done.'

    '''
    field='W3'
    print 'reading in:',field
    filename = 'CFHTLens_2013-09-03T20:16:44.tsv'
    data = ascii.read(filepath+filename, delimiter='\t', \
                    guess=True, Reader=ascii.Basic)
    print 'saving as hdf5 file...'
    f = h5py.File(savepath+field+'.hdf5', 'w')
    dset = f.create_dataset(field, data=data)
    f.close()
    data = 0
    gc.collect()
    print 'done.'
    '''

    field='W4'
    print 'reading in:',field
    filename = 'CFHTLens_2013-09-03T20:18:01.tsv'
    data = ascii.read(filepath+filename, delimiter='\t', \
                    guess=True, Reader=ascii.Basic)
    print 'saving as hdf5 file...'
    f = h5py.File(savepath+field+'.hdf5', 'w')
    dset = f.create_dataset(field, data=data)
    f.close()
    data = 0
    gc.collect()
    print 'done.'


if __name__ == '__main__':
    main()
