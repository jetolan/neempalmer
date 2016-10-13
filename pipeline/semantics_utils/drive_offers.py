import os
import pandas as pd
import numpy as np
from datetime import datetime
from get_offer import get_offer
from build_offers import build_offers


def control(name_in):
 #step through all sem3_id's in company csv and run
 #Semantics3 API for offers for each one,
 #saving output in csv
 directory="data/"
 data=pd.read_csv(str(directory+name_in+".csv"), sep=', ', header=0, engine='python')

 #if directory doesn't exist, make it
 if not os.path.exists(directory+'/'+name_in):
  os.makedirs(directory+'/'+name_in)

 for id in np.unique(data['SEM3_ID']):
     if id+'.csv' not in os.listdir(directory+'/'+name_in):
      print name_in, id
      get_offer(name_in, id)

 #now combine all the offers into one csv
 #we can then use this to build models or make
 #figures
 build_offers(name_in)
      
 return    
    
    
