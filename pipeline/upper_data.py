#name_in="WD-40"
#name_in="Movado"
#name_in="Fitbit"


#-----------------------------------------
import os
from semantics_utils import get_data
from semantics_utils import load_data
from semantics_utils import drive_offers
from semantics_utils import plot_data


def fetch(name_in):
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
    
    #and finally, plot data:
    plot_data.initial(name_in)


###################################

if __name__ == "__main__":
    import sys

    try:
        arg1 = sys.argv[1]
    except IndexError:
        print "Usage: upper_data.py <arg1>"
        sys.exit(1)      

    fetch(sys.argv[1])
