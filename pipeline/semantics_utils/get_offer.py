


from semantics3 import Products
from time import sleep
import pickle
import semantics
import os
import numpy as np




def get_offer(company, sem3_id):
 data=run_query(company, sem3_id)
 make_csv(company, sem3_id, data)
 return



def run_query(company, sem3_id):
 sem3=semantics.apikey()

 #sem3_id='4buXkdTf9sWCi0OIsYAIuS'
 #company='fitbit'

 # Build the request
 sem3.offers_field("sem3_id", sem3_id)
 sem3.offers_field("isotime", 1)
 sem3.offers_field("offset", 0)

 # Run the request
 results = sem3.get_offers()

 #this is how many results were
 #found for the query
 print 'There are this many entries for your query: '+str(results['total_results_count'])

 # Specify a cache size
 sem3.cache(5)
 # Iterate through the results
 page_no = 0

 data=[]
 if results['results_count']==0:
  return data
 
 no_pages=(int(results['total_results_count']))/int(results['results_count'])
 for i in range(no_pages):
     results = sem3.get_offers()
     print "We are at page = %s" % page_no
     #print "The results for this page are:"
     #print results['results']

     #append to results
     for r in results['results']:
         data.append(r)

     #increment by 1
     page_no += 1
     sem3.offers_field("offset", i*int(results['results_count']))
     sleep(1) #respect rate limit

 return data    

def make_csv(company, sem3_id, data):

 #if directory doesn't exist, make it
 directory=str("data/"+company)
 if not os.path.exists(directory):
  os.makedirs(directory)

 fname= directory+"/"+sem3_id+".csv"
 
 #now make variables from dictionary:
 avail=[]
 condition=[]
 currency=[]
 firstrecorded_at=[]
 id=[]
 lastrecorded_at=[]
 price=[]
 seller=[]
 shipping=[]
 sitedetails_name=[]
 sku=[]

 head="""SELLER, PRICE, CONDITION, CURRENCY, ID, AVAILABILITY, FIRSTRECORDED, LASTRECORDED, SITEDETAILS_NAME, SKU""" 
 
 #if data was empty, just save empty file
 if not data:
   np.savetxt(str(fname), np.column_stack((seller, price, condition, currency, id, avail, firstrecorded_at, lastrecorded_at, sitedetails_name, sku)), delimiter=", ", fmt='%s', header=head) 
   return

 
 for offer in data:
    if 'availability' in offer.keys():
     av=str(offer['availability'].encode('ascii','ignore'))
     av=av.replace(',', ' ')
     avail.append(av)
    else:
     avail.append('NaN')
    if 'condition' in offer.keys(): 
     condition.append(str(offer['condition'].encode('ascii','ignore')))
    else:
     condition.append('NaN')
    currency.append(str(offer['currency'].encode('ascii','ignore')))
    firstrecorded_at.append(str(offer['firstrecorded_at'].encode('ascii','ignore'))) 
    lastrecorded_at.append(str(offer['lastrecorded_at'].encode('ascii','ignore')))
    id.append(str(offer['id'].encode('ascii','ignore')))
    price.append(str(offer['price'].encode('ascii','ignore')))
    if 'availability' in offer.keys():
     sell=str(offer['seller'].encode('ascii','ignore'))
     sell=sell.replace(',', ' ')
     seller.append(sell)
    else:
     seller.append('NaN')
    sitedetails_name.append(str(offer['sitedetails_name'].encode('ascii','ignore')))
    sku.append(str(offer['sku'].encode('ascii','ignore')))
    

 #-----#
 print "saving "+fname+"..."
 np.savetxt(str(fname), np.column_stack((seller, price, condition, currency, id, avail, firstrecorded_at, lastrecorded_at, sitedetails_name, sku)), delimiter=", ", fmt='%s', header=head)  
 
 return

###################################

if __name__ == "__main__":
    import sys

    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        print "Usage: get_offer.py <arg1> <arg2>"
        sys.exit(1)      

    get_offer(sys.argv[1], sys.argv[2]) 
