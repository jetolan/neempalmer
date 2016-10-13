name_in="WD-40"
#name_in="Movado"
#name_in="Fitbit"


#-----------------------------------------

from semantics_utils import load_data
from semantics_utils import add_fields
from semantics_utils import plot_prices


#convert raw dump to csv
load_data.make_csv(name_in)

#do some math and make more columns in csv
add_fields.price_change(name_in)

#plot shit
plot_prices.plot_timeseries(name_in)
