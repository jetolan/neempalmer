#calls Semantics3 API and gets data
#using query on "name" field
#
#eg, get_data("WD-40")
#    get_data("Fitbit")
#    get_data("Movado")

#------------------------------------

from semantics3 import Products
from time import sleep
import os
import pickle
import semantics

def company(name_in):

    sem3=semantics.apikey()
    
    # Build the request
    sem3.products_field("name", name_in)
    sem3.products_field("isotime", 1)
    
    # Run the request
    results = sem3.get_products()
    
    #this is how many results were
    #found for the query
    print 'There are this many entries for your query: '+str(results['total_results_count'])

    # Specify a cache size
    sem3.cache(5)

    # Iterate through the results
    page_no = 0
    data=[]
    for i in sem3.iter():
        page_no += 1
        print "We are at page = %s" % page_no + " of " + str(results['total_results_count']) 
        #print "The results for this page are:"
        #print i
        data.append(i)
        sleep(1) #respect rate limit

    #save data as pickle in data directory
    directory="data/"
    if not os.path.exists(directory):
     os.makedirs(directory)    

    pickle.dump(data, open(str(directory+name_in+".p"), "wb" ) )
    
    return
