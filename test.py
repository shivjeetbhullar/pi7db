import csv as csvm
from pi7db import csv,GT,LT,OR
import quandl
import quandl
quandl.ApiConfig.api_key = 'yBszqj3yZqpk5j2PVy8y'

data = quandl.get('NSE/MARUTI')

print("got data")

data = data.to_csv(index=False)

csvdb = csv()

print(csvdb.read(csv_str=data)['data'][0])



#csvdb = csv('maruti.csv')


#data = csvdb.read(FIRST=5)

#data = csvdb.filter({"Open":(GT,170)},dict=data)

#print(data,csvdb.rows_num)






