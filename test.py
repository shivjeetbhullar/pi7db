import csv as csvm
from pi7db import csv,GT,LT,OR
import quandl
import quandl
quandl.ApiConfig.api_key = 'yBszqj3yZqpk5j2PVy8y'

#data = quandl.get('NSE/MARUTI')
#data = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")

dat = '''
SYMBOL,SERIES,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,ISIN,\n20MICRONS,EQ,31,32.3,30.75,31.75,31.8,29.5,204437,6486718.85,08-JUN-2020,1636,INE144J01027,\n21STCENMGM,EQ,10.75,10.9,10.75,10.9,10.9,10.7,144,1567.5,08-JUN-2020,6,INE253B01015,\n3IINFOTECH,EQ,2.1,2.1,2.1,2.1,2.1,1.95,1551570,3258297,08-JUN-2020,533,INE748C01020,\n3MINDIA,EQ,18090,18350,18028.15,18271.7,18250,17979.25,4664,84990812.65,08-JUN-2020,1855,INE470A01017,\n3PLAND,EQ,5.1,5.1,5.1,5.1,5.1,4.9,1106,5640.6,08-JUN-2020,1,INE105C01023,\n509GS2022,GS,102.9,102.9,97,100.1,98.5,98,192,19219.9,08-JUN-2020,6,IN0020200021'''

print("got data")

#data = data.to_csv(index=False)

csvdb = csv()

data = csvdb.csv_read(csv_str=dat)
print(data)
#print(csvdb.csv_write(data,write=False))

#csvdb = csv('maruti.csv')


#data = csvdb.read(FIRST=5)

#data = csvdb.filter({"Open":(GT,170)},dict=data)

#print(data,csvdb.rows_num)






