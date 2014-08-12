#!/usr/bin/python

#Author: Duncan Campbell
#Written: August 12, 2013
#Yale University
#Description: Read CFHTLens masks files

###packages###
import numpy as np
from astropy.io import fits
from astropy import wcs
import os
import fnmatch
import sys
import custom_utilities as cu
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def main():
    filepath = cu.get_data_path() + 'CFHTLens/masks/'
    savepath = cu.get_output_path() + 'processed_data/CFHTLens/masks/'

    field='W1'

    filenames = os.listdir('/scratch/dac29/data/CFHTLens/masks/')
    filenames = fnmatch.filter(filenames, field+'*.fits')
    
    #for filename in filenames:
    filename = filenames[0]
    hdulist = fits.open(filepath+filename, memmap=True)
    header = hdulist[0].header
    print header
    nxpix = header['NAXIS1']
    nypix = header['NAXIS2']
    tile  = header['OBJECT']
    w = wcs.WCS(hdulist[0].header)
    corners = np.array([[0,0],[0,nypix-1],[nxpix-1,nypix-1],[nxpix-1,0]], np.float_)
    world = w.wcs_pix2world(corners, 1)
    print world
    data = hdulist[0].data
    hdulist.close()
        



if __name__ == '__main__':
  main()
