#!/usr/bin/env python
# Function to calculate if a point is within the CFHTLS Wide field and within
# which field id.

import numpy as np;

racen,deccen=np.loadtxt("./fldid_f.txt",usecols=(4,5),unpack=1);

def within_tile(qra,qdec,center_ra,center_dec):
    from math import sin, cos, pi 
    global racen, deccen

    value = False
    #first check the declination is within range
    if(qdec > center_dec - 0.5 and qdec < center_dec + 0.5):
        radiff = 0.5 / cos(pi / 180.0 * qdec)
        ramin = center_ra - radiff
        ramax = center_ra + radiff
        #now check ra
        if(qra > ramin and qra < ramax):
            value = True

    return value

def num_tile(qra, qdec):
    from math import sin, cos, pi 
    global racen, deccen

    simplechk=0;
    if(qra>25.0 and qra < 40.0 and qdec >-15.0 and qdec < 0.0):
        simplechk=1
    if(qra>130.0 and qra < 138.0 and qdec >-8.0 and qdec < 0.0):
        simplechk=1
    if(qra>328.0 and qra < 338.0 and qdec >-4.0 and qdec < 7.0):
        simplechk=1
    if(qra>200.0 and qra < 225.0 and qdec >50.0 and qdec < 60.0):
        simplechk=1
    if (simplechk==0):
        return 0; #point is in no field(outside of survey)
    N = 0 #count the number of tiles the field is within
    for i in np.arange(racen.size):
        # First check the declination is within range
        if(qdec>deccen[i]-0.5 and qdec<deccen[i]+0.5):
            radiff = 0.5/cos(pi/180.0*qdec)
            ramin = racen[i] - radiff
            ramax = racen[i] + radiff
            # Now check ra
            if(qra>ramin and qra<ramax):
                N = N + 1
                
    return N;

def inside_survey(qra, qdec):
    from math import sin, cos, pi 
    global racen, deccen

    simplechk=0;
    if(qra>25.0 and qra < 40.0 and qdec >-15.0 and qdec < 0.0):
        simplechk=1
    if(qra>130.0 and qra < 138.0 and qdec >-8.0 and qdec < 0.0):
        simplechk=1
    if(qra>328.0 and qra < 338.0 and qdec >-4.0 and qdec < 7.0):
        simplechk=1
    if(qra>200.0 and qra < 225.0 and qdec >50.0 and qdec < 60.0):
        simplechk=1
    if (simplechk==0):
        return False; #point is in no field(outside of survey)
    result = False #count the number of tiles the field is within
    for i in np.arange(racen.size):
        # First check the declination is within range
        if(qdec>deccen[i]-0.5 and qdec<deccen[i]+0.5):
            radiff = 0.5/cos(pi/180.0*qdec)
            ramin = racen[i] - radiff
            ramax = racen[i] + radiff
            # Now check ra
            if(qra>ramin and qra<ramax):
                result = True
                
    return result
    
