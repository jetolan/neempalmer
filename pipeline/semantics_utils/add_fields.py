import pandas as pd
import numpy as np
from datetime import datetime

def price_change(name_in):

    directory="data/"
    data=pd.read_csv(str(directory+name_in+".csv"), sep=', ', header=0, engine='python')
                     
    price_diff=[]
    frac_price_change=[]
                     
    for j in range(len(data)):
        dd=data.loc[j]
        one=np.array(dd['SEM3_ID']==data['SEM3_ID'])
        two=np.array(dd['SELLER']==data['SELLER'])
        listings=data[one*two]

        #find change in price at minimum time difference
        time_dd=datetime.strptime(dd["LASTRECORDED'"], '%Y-%m-%dT%H:%M:%SZ')
        time_list=[datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ') for x in listings["LASTRECORDED'"]]
        ta=np.zeros(len(time_list))
        i=0
        for det in time_list:
          #diff=time_dd-det
          diff=det-time_dd
          ta[i]=diff.total_seconds()
          i=i+1

        #now use ta to find differnce in price
        if len(listings)>1 and min(ta)<0:
          before=ta[ta<0]
          latest_time=max(before)
          prices=listings['PRICE']
          last_price=float(prices[ta==latest_time])
          price=float(dd['PRICE'])
          frac_price_change.append(str((price-last_price) / last_price))
          price_diff.append(str(price-last_price))
        else:
          frac_price_change.append('0')
          price_diff.append('0')   


    #fill into data frame        
    g=pd.DataFrame({"PRICE_DIFF":price_diff})
    gg=pd.DataFrame({"FRACTIONAL_PRICE_CHANGE":frac_price_change})
    df = pd.concat([data, g,gg], axis=1)


    #print to csv
    df.to_csv(str(directory+name_in+"_mod.csv"))

###################################


if __name__ == "__main__":
    import sys

    try:
        arg1 = sys.argv[1]
    except IndexError:
        print "Usage: add_fields.py <arg1>"
        sys.exit(1)  
    
    
    price_change(sys.argv[1])
