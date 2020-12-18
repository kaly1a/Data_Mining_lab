/* Program to implement binning method */

import statistics
import random
dataset = random.sample(range(0,200),50)
print(dataset)
print("")
print("Sorted order of data:")
dataset.sort()
print(dataset)
print("")
print("Bins are:")
bin1 = []
bin2 = []
mbin1 = []
mbin2 = []
Mbin1 = []
Mbin2 = []
for i in range(0,20):
  bin1.append(dataset[i])
print(bin1)
for i in range(20,40):
  bin2.append(dataset[i])
print(bin2)
m1 = round((statistics.mean(bin1)))
m2 = round((statistics.mean(bin2)))
print("")
print("Smoothing by bin means:")
for i in range(20):
  mbin1.append(m1)
  mbin2.append(m2)
print(mbin1)
print(mbin2)
print("")
print("Smoothing by bin median:")
M1 = round((statistics.median(bin1)))
M2 = round((statistics.median(bin2)))
for i in range(20):
  Mbin1.append(M1)
  Mbin2.append(M2)
print(Mbin1)
print(Mbin2)
print("")
print("Smoothing by bin boundary:")
max1 = max(bin1)
min1 = min(bin1)
max2 = max(bin2)
min2 = min(bin2)
for i in range(20):
  if ( bin1[i]-min1 < max1 - bin1[i]):
    bin1[i] = min1
  else:
    bin1[i] = max1
  if ( bin2[i]-min2 < max2 - bin2[i]):
    bin2[i] = min2
  else:
    bin2[i] = max2
print(bin1)
print(bin2)
