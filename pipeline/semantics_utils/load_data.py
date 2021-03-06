#calls Semantics3 API and gets data
#using query on "name" field
#
#eg, get_data("WD-40")
#    get_data("Fitbit")
#    get_data("Movado")
#
#------------------------------------


import pickle
import numpy as np
import os

def make_csv(name_in):
    directory="data/"
    data = pickle.load( open(str(directory+name_in+".p"), "rb" ) ) 
    
    names=[]
    updated_at=[]
    created_at=[]
    upc=[]
    ean=[]
    gtins=[]
    price=[]
    currency=[]
    id=[]
    sem3_id=[]
    avail=[]
    seller=[]
    lastrecorded=[]
    firstrecorded=[]


    i=0
    #data=data[1:20]
    for dd in data:
        if 'sitedetails' in dd.keys() and dd['sitedetails']!=[]:
            if 'latestoffers' in dd['sitedetails'][0].keys() and dd['sitedetails'][0]['latestoffers']!=[]:
                for offer in dd['sitedetails'][0]['latestoffers']:
                    if 'price' in offer:

                        #these are offer level (use offer)
                        price.append(str(offer['price'].encode('ascii','ignore')))
                        currency.append(str(offer['currency'].encode('ascii','ignore')))
                        id.append(str(offer['id'].encode('ascii','ignore')))
                        sell=str(offer['seller'].encode('ascii','ignore'))
                        sell=sell.replace(',', ' ')
                        seller.append('"'+sell+'"')
                        lastrecorded.append(str(offer['lastrecorded_at'].encode('ascii','ignore')))
                        firstrecorded.append(str(offer['firstrecorded_at'].encode('ascii','ignore')))
                        if 'availability' in offer.keys():
                            av=str(offer['availability'].encode('ascii','ignore'))
                            av=av.replace(',', ' ')
                            avail.append(av)
                        else:
                            avail.append('NaN')
                            
                        #these are product level (use dd)
                        name=str(dd['name'].encode('ascii','ignore'))
                        name=name.replace(',', ' ')
                        names.append('"'+name+'"')
                        created_at.append(str(dd['created_at'].encode('ascii','ignore')))
                        updated_at.append(str(dd['updated_at'].encode('ascii','ignore')))
                        sem3_id.append(str(dd['sem3_id'].encode('ascii','ignore')))
                        if 'upc' in dd.keys():
                            upc.append(str(dd['upc'].encode('ascii','ignore')))
                        else:
                            upc.append('NaN')
                        if 'ean' in dd.keys():
                            ean.append(str(dd['ean'].encode('ascii','ignore')))
                        else:
                            ean.append('NaN')
                        if 'gtins' in dd.keys():
                            gtins.append(str(dd['gtins'][0].encode('ascii','ignore')))
                        else:
                            gtins.append('NaN')

                    
    head="""'NAME, SEM3_ID, UPC, EAN, GTINS, UPDATED_AT, CREATED_AT, SELLER, PRICE, CURRENCY, ID, AVAILABILITY, FIRSTRECORDED, LASTRECORDED'"""     

    print 'saving '+str(directory+name_in+".csv")+'...'
    np.savetxt(str(directory+name_in+".csv"), np.column_stack((names, sem3_id, upc, ean, gtins, updated_at, created_at, seller, price, currency, id, avail, firstrecorded, lastrecorded)), delimiter=", ", fmt='%s', header=head) 



###################################

if __name__ == "__main__":
    import sys

    try:
        arg1 = sys.argv[1]
    except IndexError:
        print "Usage: load_data.py <arg1>"
        sys.exit(1)      

    make_csv(sys.argv[1])

