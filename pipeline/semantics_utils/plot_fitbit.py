import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import time
from matplotlib.gridspec import GridSpec
from datetime import timedelta

name_in='fitbit'

directory="../data/"
data=pd.read_csv(str(directory+name_in+"mod.csv"), sep=',', header=0, engine='python')

time_dd=np.array([datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.000Z') for x in data["LASTRECORDED"]])

delt=np.array([float(x) for x in data['FRACTIONAL_PRICE_CHANGE']])

#these are too big
dd1=delt[delt<3]
tt1=time_dd[delt<3]

#these are zero
dd=dd1[dd1!=0]
tt=tt1[dd1!=0]

#order by time
x=np.array([time.mktime(x.timetuple()) for x in tt])
aa=np.argsort(x)
xt=x[aa]
dt=dd[aa]

#remove the first two points
xt=xt[2:]
dt=dt[2:]

#convert back to datetime
xx = np.array([datetime.fromtimestamp(x) for x in xt])

#plotting setup
plt.figure(0, figsize=(12, 8))
gs1 = GridSpec(2, 3)
gs1.update(left=0.15, right=0.95, wspace=0.3, hspace=0.15)
ax1 = plt.subplot(gs1[:,:])
   

#these are negative change
s1=plt.scatter(xx[dt<0], dt[dt<0], c='r', s = 20, lw = 0, alpha=0.7)

#these are postive change
s2=plt.scatter(xx[dt>0], dt[dt>0], c='b', s = 20, lw = 0, alpha=0.7)

#plot the running average
N=100
g=np.convolve(dt, np.ones((N,))/N, mode='valid')
lin,=plt.plot(xx[N/2:-(N/2-1)], g, 'g', linewidth=2, alpha=.7)

plt.plot(xx, np.zeros(len(xx)), '--', color='gray')

quarters=['1990-03-31', '1990-06-30', '1990-09-30', '1990-12-31']
quarters_dt=np.array([datetime.strptime(x, '%Y-%m-%d') for x in quarters])
for y in range(30):
   quarters_dt=quarters_dt + timedelta(days=366)
   for i in quarters_dt:
      plt.plot([i,i], [-1,1], color='gray')
      
plt.ylabel('Fractional change')
#plt.xlabel('Date')
plt.ylim([-1,1])
plt.xlim(xx[0]-timedelta(weeks=12), xx[-1]+timedelta(weeks=12))
plt.title(str(name_in))
plt.legend([s2,s1,lin], ['Increase in vendor price', 'Decrease in vendor price', 'running average (N='+str(N)+')'], loc=2) 



#--------------------------------------------
#plot middle figure

#find mean in each quarter
val=[]
num=[]
bins_sec=[]
quarters_dt=np.array([datetime.strptime(x, '%Y-%m-%d') for x in quarters])
for y in range(30):
 #print quarters_dt
 quarters_dt=quarters_dt + timedelta(days=365, hours=6)
 int=[time.mktime(x.timetuple()) for x in quarters_dt]
 for i in int:
  bins_sec.append(i)

for i in range(len(bins_sec)-1):
    overlap=np.logical_and(bins_sec[i]<xt, xt<=bins_sec[i+1])
    val.append(np.nanmean(dt[overlap]))
    num.append(np.nansum(overlap))

#add zero at end
val.append(0)
num.append(0)

bins=[datetime.fromtimestamp(x) for x in bins_sec]

#ax2 = plt.subplot(gs1[1,:])
#height,ind=np.unique(val, return_index=True)
#height=height[np.argsort(ind)]

gray=plt.plot([bins[0],bins[-1]+timedelta(weeks=12)], [0,0], '--', color='gray', alpha=0.7)
rects = plt.bar(bins, val, width=90, color='b', alpha=1)
plt.xlim([datetime(2012, 9, 1),datetime(2017, 1, 1)])
plt.ylabel('Fractional change')
plt.legend([rects], ['Average vendor price change'], loc=2, frameon=False) 



   
plt.show()
plt.savefig(str(name_in+'2.pdf'), format='pdf')



