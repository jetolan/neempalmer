import pandas as pd
import numpy as np
from datetime import datetime
from get_offer import get_offer


def control(name_in):
 #step through all sem3_id's in company csv and run
 #Semantics3 API for offers for each one,
 #saving output in csv

 #name_in='Fitbit'
 directory="../data/"
 data=pd.read_csv(str(directory+name_in+".csv"), sep=', ', header=0, engine='python')
 
 for id in np.unique(data['SEM3_ID']):
     print name_in, id
     get_offer(name_in, id)

 return    
    
    
