#name_in="WD-40"
name_in="Movado"
#name_in="Fitbit"


#-----------------------------------------
import os
from semantics_utils import get_data
from semantics_utils import load_data
from semantics_utils import drive_offers

#if data file doesn't exist, make it
directory="data"
data_file=str(directory+"/"+name_in+".p")
if not os.path.exists(data_file):
 print 'making '+data_file+'...'   
 get_data.company(name_in)


#if csv file doesn't exist, make it
data_file=str(directory+"/"+name_in+".csv")
if not os.path.exists(data_file):
 print 'making '+data_file+'...'
 load_data.make_csv(name_in)

 
#once data file exists, go through and get all sem3_id's in it
drive_offers.control(name_in)
