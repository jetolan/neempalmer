#this function takes the csv files of offers and builds grand csv file

import os
import numpy as np
import pandas as pd
from datetime import datetime

def build_offers(company):
    #company='fitbit'
    
    #list of offer files
    directory=str("data/"+company)
    fn=os.listdir(directory)


    for file in fn:

        sem3_id=file[0:-4]
        print sem3_id
        data=pd.read_csv(str(directory+'/'+file), sep=', ', header=0, engine='python')


        price_diff=[]
        frac_price_change=[]
                     
        for j in range(len(data)):
            dd=data.loc[j]
            #check if seller is nan
            if dd['# SELLER'] == 'NAN' or dd['# SELLER'] != dd['# SELLER']: 
                two=[False]*len(data)
            else:
                two=np.array(dd['# SELLER']==data['# SELLER'])
            listings=data[two]
        
            #find change in price at minimum time difference
            time_dd=datetime.strptime(dd["LASTRECORDED"], '%Y-%m-%dT%H:%M:%S.000Z')
            time_list=[datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.000Z') for x in listings["LASTRECORDED"]]
            ta=np.zeros(len(time_list))
            i=0
            for det in time_list:
                diff=det-time_dd
                ta[i]=diff.total_seconds()
                i=i+1

            #now use ta to find differnce in price
            if len(listings)>1 and min(ta)<0:
                before=ta[ta<0]
                latest_time=max(before)
                prices=listings['PRICE']
                pp=prices[ta==latest_time]
                if len(pp)>1:
                    pp=pp.iloc[0]
                last_price=float(pp)
                price=float(dd['PRICE'])
                g=pd.Series({"PRICE_DIFF":str(price-last_price)})
                if last_price==0: #prevent zero division
                    last_price=float('NaN')
                gg=pd.Series({"FRACTIONAL_PRICE_CHANGE":str((price-last_price) / last_price)})
                sem=pd.Series({"SEM3_ID":sem3_id})
                df = pd.concat([sem, dd, g,gg])
                if 'data2' not in locals():
                    data2=pd.DataFrame(df).transpose()
                else:
                    data2=data2.append(pd.DataFrame(df).transpose())


    if 'data2' not in locals():
      print 'did not find offers from same seller at multiple dates'
    else:    
        #print to csv
        data2.to_csv(str(directory+"mod.csv"))           


###################################

if __name__ == "__main__":
    import sys

    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        print "Usage: build_offer.py <arg1> <arg2>"
        sys.exit(1)      

    get_offer(sys.argv[1], sys.argv[2])     
