import pandas as pd
import math

#read data

dataT=pd.read_csv('/content/drive/MyDrive/IT-262/262-CBA.csv')
print(dataT)


discountRate=.05
# the compounding discount over the years

# create a list of 4 0 elements
discountFactor=[0,0,0,0]

for year in dataT['years']:
  discountFactor[year]=1/math.pow(1+discountRate, year)

dataT['discountFactor']=[round(num,2) for num in discountFactor]
print(dataT)

#calculate NEt benefit/cost for each year
#you sum all the benefit & cost values

#initial a list of 4 - i have years 0 to 4
NetBC=[0,0,0,0]
for year in dataT['years']:
  NetBC[year]= dataT['developmentCost'][year]+dataT['operationalCost'][year]+dataT['valueOfBenefits'][year]

dataT['NetBC']=NetBC
print(dataT)

# calculate net present value

#initialize an empty list of 4 items - 1 for each year
NPV=[0,0,0,0]

for year in dataT['years']:
  NPV[year]=dataT['NetBC'][year]*dataT['discountFactor'][year]

dataT['NPV']=[round(num,2) for num in NPV]
print(dataT)