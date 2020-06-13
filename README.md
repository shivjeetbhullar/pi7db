# Pi7db.
Pi7db is a open-source powerful python package to manage directory based database in JSON format with number of features like Filter, sort, update etc.

# WHY I USE Pi7db ?
There are some reasons may you like.
- NOSQL
- Flexible Data
- No Need To Make Connection To Database. (Most Hated Stuff)
- Simple And Super Fast.
- Directory Based Databse (Place Where You Want).
- Advance Filter Options Like (Less Than, Greater Than, String Filter, List Filter etc).
- Read, Write, Sort, Update, Trash, Filter Data With Advance Features.
- Encrypt Data With Password.

# DATABASE STRUCTURE
Data is stored in binary files inside collections. Database structure is similar to mongodb.
![image](https://drive.google.com/uc?export=view&id=1BXxi6mfcQ11mnBpSot96TvczC5LpgYa3 "Pi7db Structure")

## File Structure
```json
{
   "un_id": 20202171823558180,
   "title": "This Is File", 
   "description": "This file strore information.",
   "tags": ["pi7db", "database", "NoSQL"],
   "views": 10,
   "cr_dc_path":"Blog_Database/Collection_name/FileName.bin",
   "comments": [	
      {
         "user":"john",
         "message": "My Name is Jonh"
      }
   ]
}
```
There is un_id and cr_dc_path is avalible in every file by default represent a uniqe key for file and file path in system 

# INSTALLATION
Installation with pip
```sh
 $ pip3 install pi7db 
 ```
# Getting Started
First import pi7db package in python file and create a object by passing argument Database name. It will automatically create a directory in current folder with that name where all datafiles will be stored.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")
```
### Manual Database path
if you want to store database in a specific directory then pass second argument of path. 
```python
from pi7db import pi7db
db = pi7db("Blog_Database","path/to/dir")
```
# Write Data
Write function is used for write Json data.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

data = {
       "Name":"John",
       "Surname":"Diamond",
       "Tel-Number":9876543210,
       "Age":30,
       "Subject":["Python","Ruby","Perl"],
       "comments": [
                   { "user":"Stephin",
                     "message": "John Is Best!"},
                   { "user":"Alex",
                    "message": "We Love You John!"}
                   ]
       }
       
db.write('Users',data)
# This Will Write Data In Users Collection.
```
### Write Data In Specific File Manually. 
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

data = {
       "Name":"John",
       "Surname":"Diamond",
       "Tel-Number":9876543210,
       "Age":30,
       "Subject":["Python","Ruby","Perl"],
       "comments": [
                   { "user":"Stephin",
                     "message": "John Is Best!"},
                   { "user":"Alex",
                    "message": "We Love You John!"}
                   ]
       }
       
data2 = {
       "Name":"Richard",
       "Surname":"Stallman",
       "Tel-Number":9876543000,
       "Age":40,
       "Subject":["UNIX","C","Perl"],
       "comments": [
                   { "user":"Marshal",
                     "message": "I Love C Language."},
                   { "user":"Della",
                    "message": "C Is A Fast Language"}
                   ]
       }
       
db.write('Users' , 'John' , data)

db.write('Users' , 'Richard' , data2)
# This Will Write Data In john (filename john) file inside Users Collection.
```
Following Directory Tree Will Be Created In Your PC.
![image](https://drive.google.com/uc?export=view&id=1xoXs59TFbm-9cDZPlrupMEmzQkqJy-TM "Pi7db Structure")
You can directly call file during read time this will increase speed of your program.
For Example: You Can Call Specific Blog Post By Its Name. 

# Read Data
Data read is pretty easy and fast in pi7db. With the help of read function.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.read()

# This Will Read Entire Data In Database And Return Output In Dict.
# But Read Entire Data Is Not Recomended When Your Database Size Is Large For Example 500mb.
```

# Read Data From Collection
Data read is pretty easy and fast in pi7db. With the help of read function.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.read('Users')

# This Will Read Entire Data In Users Collection And Return Output In Dict.
```
#### Output:
```json
 {"data": 
   [
   { 
    "un_id": "20202660459428127",
    "Name": "John",
    "Surname": "Diamond",
    "Tel-Number": 9876543210,
    "Age":30,
    "Subject":["Python","Ruby","Perl"],
    "comments": [
                   { "user":"Stephin",
                     "message": "John Is Best!"},
                   { "user":"Alex",
                    "message": "We Love You John!"}
                ],
    "cr_dc_path": "Blog_Database/Users/John.bin"
   },
   { 
    "un_id": "20202590449478829",
    "Name": "Richard",
    "Surname": "Stallman",
    "Tel-Number": 9876543000,
    "Age":40,
    "Subject":["UNIX","C","Perl"],
    "comments": [
                   { "user":"Marshal",
                     "message": "I Love C Language."},
                   { "user":"Della",
                    "message": "C Is A Fast Language"}
                   ],
    "cr_dc_path": "Blog_Database/Users/Richard.bin"
   }
   ], 
  "status": 1
 }
```
In output status:
 - 1 = Sucess
 - 0 = Error

# Read Data From File
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.read('Users','John')

# This Will Read Entire Data In Users Collection And Return Output In Dict.
```
#### Output:
```json
 {"data": 
   [{ 
    "unid": "20202660459428127",
    "Name": "John",
    "Surname": "Diamond",
    "Tel-Number": 9876543210,
    "Age":30,
    "Subject":["Python","Ruby","Perl"],
    "comments": [
                   { "user":"Stephin",
                     "message": "John Is Best!"},
                   { "user":"Alex",
                    "message": "We Love You John!"}
                   ],
    "cr_dc_path": "Blog_Database/Users/John.bin"
   }], 
  "status": 1
 }
```
# Read Data From File By KeyName
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.read('Users','John','Surname')

# This Will Read Entire Data In Users Collection And Return Output In Dict.
```
#### Output:
```
 Diamond
```

# FILTER DATA
 Filter Is Most Powerfull Funtion Of This Package. You Can Filter Data According To Your Choice There Are Many Number Of Features Avalible In Filter Function. In Filter Function It Is Possible To Filter Data From Nested Dict Or List Of Dicts As The Way You Want. Filter Makes This Database More Flexible And Powefull.
 Some Features Are Shown Below:
 - Operators (Used For Filter Data)
   - OR
   - AND 
   - LT (Less Than)
   - GT (Greater Than)
   - GET (Greater And Equal Than)
   - LET (Less And Equal Than)
 - String Filter (User To Filter Data According To String)
   - Forward String Filter
   - Backward String Filter
   - Center String Filter
 - List Filter (Filter Data From List)
 - Nested Filter (Filter Data From Nested Dict)
 
 ### Simple Filter
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.filter({"Name":"John"})
#This will filter all data where name is John and return output.
```
### Output
```json
{"data": [{
       "unid": "20203953408762519", 
       "Name": "John", 
       "Surname": "Diamond", 
       "Tel-Number": 9876543210, 
       "Age":30,
       "Subject":["Python","Ruby","Perl"],
       "comments": [
                   { "user":"Stephin",
                     "message": "John Is Best!"},
                   { "user":"Alex",
                    "message": "We Love You John!"}
                   ],
       "cr_dc_path": "Blog_Database/Users/John.bin"
        }],
 "status": 1
}
```
 ### AND Filter
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.filter({"Name":"John","Surname":"Diamond","Tel-Number":9876543210})
```
This Will Check In Database:
- if Name is John
- and Surname is Diamond
- and Tel-Number is 9876543210

If All These Conditions are True Then Return Output Otherwise Return Nothing.

### OR Filter
> **Note:** Before Using "OR" Operator You Have To Import It.
```python
from pi7db import pi7db, OR
db = pi7db("Blog_Database")

db.filter({"Name":"John"}, OR ,{"Surname":"Diamond","Tel-Number":9876543210})
```
This Will Check In Database:
- if Name is John
- OR Surname is Diamond and Tel-Number is 9876543210

If All These Conditions are True Then Return Output Otherwise Return Nothing.

### GT (GREATER THAN) Filter
> **Note:** Befor Using "GT" Operator You Have To Import It.
```python
from pi7db import pi7db, GT
db = pi7db("Blog_Database")

db.filter({ "Age": (GT,19) })
```
This Will Check In Database:
- if Age Greater Than 19

If This Condition is True Then Return Output Otherwise Return Nothing.

### LT (LESS THAN) Filter
> **Note:** Before Using "LT" Operator You Have To Import It.
```python
from pi7db import pi7db, LT
db = pi7db("Blog_Database")

db.filter({ "Age": (LT,39) })
```
This Will Check In Database:
- if Age Less Than 39

### LET (Less and Equal THAN) And GET (Greater and Equal Than) Filter
Use Of These Filters Are Similarly To **GT** And **LT** Operators. For Example
> **Note:** Before Using Operator You Have To Import It.
```python
from pi7db import pi7db, GET,LET
db = pi7db("Blog_Database")

#LET FILTER (Less and Equal THAN) 
db.filter({ "Age": (LET,40) })

#GET FILTER (Greater and Equal Than)
db.filter({ "Age": (GET,40) })
```
If This Condition is True Then Return Output Otherwise Return Nothing.
## STRING Filters
There Are Number Of String Filters are Avalible In pi7db.
- Forward String Filter
- Backward String Filter
- Center String Filter

### FORWARD STRING Filter
 `**` Is Used In Front Of String You Want To Filter. For Example `**String`. This Will Check If String After `**` Mathches With Any Value In DataBase. And It Will Ignore Front Portion Of String AS Shown In Code Below.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.filter({ "Name": "**ard" })
#This Will Check If Name Ends With "ard" For Example: "Richard".
```
This Will Check In Database:
- if Name Ends With **"ard"**

### BACKWARD STRING Filter
 `**` Is Used In End Of String You Want To Filter. For Example `String**`. This Will Check If String Before `**` Mathches With Any Value In DataBase. And It Will Ignore Back Portion Of String AS Shown In Code Below.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.filter({ "Name": "Ric**" })
#This Will Check If Name Starts With "Ric" For Example: "Richard".
```
This Will Check In Database:
- if Name Starts With **"Ric"**

### Output
```json
{"data": [{
       "un_id": "20202590449478829",
       "Name": "Richard",
       "Surname": "Stallman",
       "Tel-Number": 9876543000,
       "Age":40,
       "Subject":["UNIX","C","Perl"],
       "comments": [
                   { "user":"Marshal",
                     "message": "I Love C Language."},
                   { "user":"Della",
                    "message": "C Is A Fast Language"}
                   ],
       "cr_dc_path": "Blog_Database/Users/Richard.bin"
        }],
 "status": 1
}
```

### CENTER STRING Filter
 `**` Is Used In Front And Back Of String You Want To Filter. For Example `**String**`. This Will Check If String Mathches in Center With Any Value In DataBase.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.filter({ "Name": "**ich**" })
#This Will Check If "ich" is in Name. For Example: "Richard".
```
This Will Check In Database:
- if **"ich"** In Name

## LIST Filter
 It Is Also Possible To Filter Data From List. As Shown Below:
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.filter({ "Subject": ["UNIX","Perl"] })
#This Will Check If "UNIX" And "Perl" Exist In Subject.
```
This Will Check In Database:
- if **"UNIX"** Exist In List Of Subject
- if **"Perl"** Exist In List Of Subject

If Both The Conditions Are True Then It Will Return Output.

## NESTED Filter
 It Is Also Possible To Filter Data From List. As Shown Below:
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.filter({ "comments": [
                   { "user":"Marshal"}
                       ] 
         })
         
#This Will Check If user "Marshal" exist in "comments".
```
This Will Check In Database:
- if user **"Marshal"** Exist In List Of comments

### Another Example Of NESTED Filter
In Nested Filters You Can Use Any Filter Like **GT**,**GET**,**LET** etc. In This Example We Will Cover Nested Filter With String Filter.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.filter({ "comments": [
                   { "message":"**Love**"}
                       ] 
         })
         
#This Will Check If "Love" Word In message.
```
This Will Check In Database:
- if message Is About **"Love"**
If The Conditions Is True Then It Will Return Output.
## Example: Use Of Multiple Filters Together
In This Example We Will Use "OR", "And","GT" and String Filters.
First Import **GT** and **OR** From pi7db
```python
from pi7db import pi7db, OR, GT
db = pi7db("Blog_Database")

db.filter(
          "Subject":["C"],
          OR,
          { "Surname":"Stall**", "Tel-Number":9876543210 },
          OR,
          { "Age":(GT,18) }
        )
```
This Will Check Following Conditions:
- If **C** In Subject List.
- OR Surname Is "Diamond" AND TEl-Number Is 9876543210.
- OR Age Is Greater Than 18.

If Only One Condition True Then It Will Return Output. Because We Use **OR** Operator In Filter.

# DELETE DATA
Various Options Are Avalible For Delete Data.
- Delete A Key From File. For Example (delete Surname From John File In Users Collection)
- Delete A Specific File. For Example (Delete John File From Users Collection)
- Delete Entire Collection. For Example (Delete Users)

### Delete A Key From File
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.trash('Users','John','Surname')
```
This Will Delete Surname From John File In Users Collection.
### Output:
```
{'success': 'Deleted! Surname Deleted From John!', 'status': 1}
```
### Delete A File From Collection
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.trash('Users','John')
```
This Will Delete John File From Users Collection.
### Output:
```
{'success': 'Deleted! Johan!', 'status': 1}
```
### Delete A Collection
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.trash('Users')
```
This Will Delete Entire Collection.
### Output:
```
{'success': 'Deleted! Collection Users Deleted Successfully!', 'status': 1}
```
 
 # DELETE BY FILTER
 Pi7db provide number of features. It is also possible to delete data by filter.
 Two arguments **where** and **dropkey** is used for delete data.

### Delete Data With Where Argument
 ```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.trash(where={"Name":"John"})
#This will delete all The files where Name is John.

# For Delete Only From Users Collection Use db.trash("Users",where={"Name":"John"})
```
### Output:
```
True
```
This will delete all The files where Name is John. This is one from advance features of pi7db.
 
 ### Delete Data With Where Argument Using Multiple Filters
 It is Also Possible To Delete Data With Multiple Filters As Shown Below
 ```python
from pi7db import pi7db,OR,GT
db = pi7db("Blog_Database")

db.trash("Users", where = [
                   {"Name":"**jo**","Surname":"Diamond"},
                   OR,
                   {"Age":(GT,50)}
                  ] 
        )
```
This Will Check Following Conditions:
- If **jo** In Name AND Surname Is "Diamond"
- OR Age Is Greater Than 50.
If These Two Conditions Are True Then It Will Be Removed From Database.

 ### Delete Data With "Where" And "Dropkey" Argument
 Delete a key with filter
 ```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.trash('Users', where={"Name":"John"}, dropkey='Tel-Number')
#This will delete all Tel-Number Keys From All files where Name is John.
```
### Output:
```
True
```
 This will delete all Tel-Number Keys From All files where Name is John.
 You Can Use Number Of Filters To Delete Data As Shown In Filter Data Funtion Below.
 > **NOTE:** NESTED KEY DELETE IS NOT SUPPORTED IN CURRENT VERSION OF pi7db. (comming soon).
 # UPDATE Data
 If You Want To Update Data Then Use Update Function. In Update Function If is Also Possible To Update By Filter.
 
### UPDATE Data In Specific File
It Takes Three Arguments Collection_Name , File_Name And Dict Data
For Example: ` db.update("Collection_name","File_Name",{"Data":"Data"}) `
As Shown Below:
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.update('Users','John', {'Name': "Johnson",
                           "Surname":"Retchie",
                           "Father_name":"Sam"
                         })
```
### Output:
```
{'success': 'Success! Value Update in John!', 'status': 1}
```
 ### UPDATE Using Where Argument
It Takes Two Or Three Arguments Dict Data
For Example:
 - ` db.update("Collection_name",{"Data":"Data"}, where="Name":"John") ` #With Collection Name
 - ` db.update({"Data":"Data"}, where="Name":"John") `#Without Collection Name

Collection Name Is Recomended. It Will Increase Speed Of Update.

As Shown Below:
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.update({"Father_name":"Sam Diamond"}, where={"Name":"John"})
#For Pass Multiple Argument In Where Use list
#for Example where = [ {"Name":"John"} ,OR, {"Surname":"**mnd"}]
```
It Will Update Father_name Key Where Name Is John. If Father_name Key Not Exist Then It Will Add Automatically where Name Is John.
### Output:
```
True
```

### UPDATE Data In All File
Sometime We Want To Update Data In All Files Present In Database.Then We Can Use `String Filter`.
As Shown Below:
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

db.update({'Added_Date': "2020-05-21"},where={"Name":"**"})
```
This Will Update Data In All Files Where Name Key Is Present.
### Output:
```
{'success': 'Success! Value Update in John!', 'status': 1}
```

 ### UPDATE Data With INCREMENT Function
 **INCREMENT** Function Provide Help In Update Data With Less Efforts For Example If You Want To Update Age of John then `{"Age":increment(2)}`. This Will Increment John's Age By 2 For example 40 + 2 = 42.
 Increment Function Take Single Int Argement For example 9. or any other Integer.
 Example:
 > Note : You Have To Import increment Function From pi7db
 ```python
from pi7db import pi7db,increment
db = pi7db("Blog_Database")

#Using Where Argument
db.update({"Age":increment(5)}, where={"Name":"John"})
#For Pass Multiple Argument In Where Use list
#for Example (Using OR operator):- where = [ {"Name":"John"} ,OR, {"Surname":"**mnd"}]

#OR IN A SPECIFIC FILE
db.update("Users","John", {"Age":increment(5)})
```
 It Will Increment John's Age By 5
 ### Output
```
True
```
 ### UPDATE Data With decrement Function
 **DECREMENT** Function Is Opposite To Increment Function It Help In Decrement In Value. For Example:- `{"Age":decrement(3)}`. This Will Decrement John's Age By 3 For example 40 - 3 = 39.
 Decrement Function Take Single Int Argement For example 5. or any other Integer.
 Example:
 > Note : You Have To Import decrement Function From pi7db
 ```python
from pi7db import pi7db,decrement
db = pi7db("Blog_Database")

# UPDATE IN A SPECIFIC FILE
db.update("Users","John", {"Age":decrement(2)})

#OR USING WHERE ARGUMENT
db.update({"Age":decrement(2)}, where={"Name":"John"})
#For Pass Multiple Argument In Where Use list
#for Example (Using OR operator):- where = [ {"Name":"John"} ,OR, {"Surname":"**mnd"}]
```
 It Will Decrement John's Age By 2
 ### Output
```
True
```
 > **NOTE:** NESTED UPDATE IS NOT SUPPORTED IN CURRENT VERSION OF pi7db. (comming soon).
 
 # SORT Data
 For Get Sorted Data Use **sort** Function. Sort Function Take one Argument Of Data Type **set**. For Example: `db.sort({"Name"})`
 By Default Data Is In Ascending Order For Set Manually:
 - For Sort Data In Ascending Order Use `db.sort({"Name"}, order=asc)`
 - For Sort Data In Descending Order Use `db.sort({"Name"}, order=dsc)`
> **NOTE:** Import **asc** and **dsc** For Use Order.
 ```python
from pi7db import pi7db, asc, dsc
db = pi7db("Blog_Database")

# By Default Order Is Ascending
db.update({"Name"})

#For Descending Order Use
db.update({"Name"},order=dsc)
```

 
 ### SORT Data In Nested Dict
 > **Note:** Data Sortion Work Only With Nested Dict Not With list. 
 For Example We Have Data In Database In This Order:
 ```json
   {
    "User":{
            "Name":"Richard",
            "Subject":{"Science":"Chemistry","Computer":"CSE"},
            "Teacher":{"Science":"Fury","Computer":"James"},
            }
   }
 ```
 ##### How To Sort This Nested Data ?
 - For Sort By Name In This Data We Will Pass Argument Like `db.sort({"User","Name"})`
 - For Sort By Specific Subject In This Data We Will Pass Argument Like `db.sort({"User","Subject","Science"})`
 - For Sort By Specific Teacher Name We Will Pass Argument Like `db.sort({"User","Teacher","Science"})`
 
 You Can Also Pass Collection_Name Before Dict. Collection Name Is Recommended.
 For Sort In Specific Collection We Will Pass Argument Of Collection Name For Example: `db.sort("Users",{"User","Subject","Science"})`
 
 ### SORT Filtered Data
 There Is A Function `db.sortdict` In pi7db Which Is Used To Sort Filtered Data. In Other Hand `db.sort` Function Is Used To Sort All Data.for Example:
  ```python
from pi7db import pi7db,dsc
db = pi7db("Blog_Database")

filtered_data = db.filter({"Name":"**"})
db.sortdict(filtered_data,{"Surname"},order=dsc)
```
### output
```json
 {"data": 
   [{ 
    "un_id": "20202590449478829",
    "Name": "Richard",
    "Surname": "Stallman",
    "Tel-Number": 9876543000,
    "Age":40,
    "Subject":["UNIX","C","Perl"],
    "comments": [
                   { "user":"Marshal",
                     "message": "I Love C Language."},
                   { "user":"Della",
                    "message": "C Is A Fast Language"}
                   ],
    "cr_dc_path": "Blog_Database/Users/Richard.bin"
   },
   { 
    "un_id": "20202660459428127",
    "Name": "John",
    "Surname": "Diamond",
    "Tel-Number": 9876543210,
    "Age":30,
    "Subject":["Python","Ruby","Perl"],
    "comments": [
                   { "user":"Stephin",
                     "message": "John Is Best!"},
                   { "user":"Alex",
                    "message": "We Love You John!"}
                ],
    "cr_dc_path": "Blog_Database/Users/John.bin"
   }], 
  "status": 1
 }
```

# Some Other Advance Arguments:
There Are Some Other Arguments Help In Speed Of Data Read, Ignore Files, Read Data From Specific Part.
List Of Arguments:
- `FROM` (Starting Point File Number)
- `TO` (End Point Of File Number)
- `FIRST` (Read Number Of Files From Start)
- `LAST` (Read Number Of Files From Last)
- `IGNORE` (Ignore Specific File)

### `FROM` Argument
Suppose You Have 1000 Number Of Files In Database. But You Want To Ignore First 10 Files And Read Other 990 Files Then `FROM` Argument Can Help You.
For Example:
> **NOTE:** Write `FROM` In **Capital Words**
```python
from pi7db import pi7db
db = pi7db("Blog_Database")
db.read(FROM=10)
```

### `TO` Argument
Suppose You Have 1000 Files In Database. But You Want To Read From 10 To 50 Files. For Example:
> **NOTE:** Write `TO` In **Capital Words**.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")
db.read(FROM=10,TO=50)
```

### `FIRST` Argument
Suppose You Have 1000 Files In Database. But You Want To Read Only First 10 Files.For Example:
> **NOTE:** Write `FIRST` In **Capital Words**.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")
db.read(FIRST=10)
```
This Will Read And Return First 10 Files.

### `LAST` Argument
Suppose You Have 1000 Files In Database. But You Want To Read Only Last 10 Files.For Example:
> **NOTE:** Write `LAST` In **Capital Words**.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")
db.read(LAST=10)
```
This Will Read And Return LAST 10 Files.

### `IGNORE` Argument
Suppose You Want To Ignore A File During Read, Sort Or Filter Time Then Use Ignore Argumen.For Example:
> **NOTE:** Write `IGNORE` In **Capital Words**.
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

#IGNORE SINGLE FILE
db.read(IGNORE="John")

#IGNORE MULTIPLE FILES USING LIST
db.read( IGNORE= ["John","Richard"] )

```
`IGNORE = "John"` # This Will Ignore Only John File
`IGNORE = ["John","Richard"]` # This Will Ignore All Files In List

#### You Can Use These Arguments With `sort` , `filter` and `read` Functions
For Example:
```python
from pi7db import pi7db
db = pi7db("Blog_Database")

#With READ
db.read(IGNORE="John")

#With SORT
db.sort({"Name"},FROM=1,TO=10)

#With FILTER
db.filter({"Name":"J**"},FIRST=50)


```
`MORE FEATURES COMMING SOON, THANKYOU.`
