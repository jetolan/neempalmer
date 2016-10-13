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


for dd in data:
    avail.append(str(offer['avail'].encode('ascii','ignore')))
    condition.append(str(offer['condition'].encode('ascii','ignore')))
    currency.append(str(offer['currency'].encode('ascii','ignore')))
    first_recorded_at.append(str(offer['first_recorded_at'].encode('ascii','ignore'))) 
    last_recorded_at.append(str(offer['last_recorded_at'].encode('ascii','ignore')))
    id.append(str(offer['id'].encode('ascii','ignore')))
    price.append(str(offer['price'].encode('ascii','ignore')))
    seller.append(str(offer['seller'].encode('ascii','ignore')))
    sitedetails_name.append(str(offer['sitdetails_name'].encode('ascii','ignore')))
    sku.append(str(offer['sky'].encode('ascii','ignore')))
    
head="""'SELLER, PRICE, CONDITION, CURRENCY, ID, AVAILABILITY, FIRSTRECORDED, LASTRECORDED, SITEDETAILS_NAME, SKU'"""     

print 'saving '+str(directory+name_in+".csv")+'...'
np.savetxt(str(directory+name_in+".csv"), np.column_stack((seller, price, condition, currency, id, avail, firstrecorded, lastrecorded, sitedeails_name, sku)), delimiter=", ", fmt='%s', header=head)  
