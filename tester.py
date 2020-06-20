from pi7db import pi7db,GET,OR,increment,decrement,dsc,asc,GT,LT,LET
db = pi7db("Blog_Database")
#db.key("Shivjeet")
from datetime import datetime
data = {
       "Name":"Shivjeet",
       "Surname":"Bhullar",
       "Tel-Number":9876543210,
       "Age":20
       }
       
db.temp_limt = 3

#db.changekey("GodIsGreat","")

#print(db.changekey('NOENC','hello'))

# print(db.js.read('h'))
# print(db.js.read('h'))
# print(db.js.read('h'))

#db.dog.test()


#print(db.write('users','jim',data))
#print(db1.move.write('hell0',dic))

#print(db1.gen.write('hell',dic))

#print(db1.gen.write('hello',dic))

#print(db.move.test_print())
#print(db.move.write('hello',{"name":{"test":"test"},"like":10}))
#print(db.write('sd','hellods',{"name":{"test":"test"},"s":"s"}))




#print(db.move.trash())
#print(OR)
#print(db.move.read('hell0','title'))
#print()


startTime = datetime.now()
import random

#fdata = db.filter({"Name":"**"})
#print(db.sortdict(fdata,{"Name"},order=dsc))
#db.update({"test":{"test1":[{"user":random.randint(0,88888)}]}},where={"Name":"Johnson"})
# for x in range(100):
#  db.write("users",str(x),{"num":x,"lvl":[{"num":1,"name":x},{"num":2,"name":x+100}]})

#db.update("users","0",{"num":1})#{"lvl":[{"num":increment(100)}]},where={"num":(GT,1)})

#db.trash(dropkey={"lvl":[{"$keys":["name"],"$where":{"name":(GT,98)}}]},where={"lvl":[{"name":(GT,98)}]})
#print(db.status())
# #print(db.write('obj',{"fi":"yo"}))
# db.write("users",'shivjeet',{'name':"shivjeet"})
# db.write("users",'joban',{'name':"joban"})

# db.write("us",'shivjeet',{'name':"shivjeet"})
# db.write("us",'joban',{'name':"joban"})
#print(db.read())
#db.update("users",{"df":1},where={"name":"shivjeet"})
#for x in db.status()['users']['Doc_Name']:
  #print(x)
# class Av:
#   def hi(self):
#     print("hello")
db.rename('users','shivjeet','shivjeetbhullar')
# print(db.read())
# data = db.read()['data'][0]['obj'][0]

# d = data
# d.hi()
#print(db.write("obj",{"obj":[Av]}))
#print(db.filter({"lvl":[{"name":0},{"name":(GT,97)}]}))

#print(db.ort({'test','test1'},order=asc))

#print(db.update({"tf":{"Name":"Messi","view":4}},where={"Name":"Jo**"}))
#print(db.update('John','s',{'Name': "Johnson","Surname":"Retchie"}))

#print(db.trash('John', where=[ {"Name":'Johsn'}, OR , {"Surname":"Retchie"} ]))

#print(db.write('John','s',data))

#print(db.write('John',data))
#print(db.write('John','s2',data))

#print(db.filter({'unid':"**"})['data'])

#db.trash("John")
#print(db.write('col2','st',dic))

#for x in range(1000):
# print(db.temp.write({"this i":"s Temp"}))


#print(len(db.temp.read()['data']))
#db.temp.update({"Date:":datetime.now()},where={"unid":"**"})
#print(db.temp.filter({"this i":"**"}))
#db.update('df','file',{"lhe":"men","d":"2"})

# for x in range(10000):
#   print(db.write("users",str(x),data))
#print(db.update({"Date:":datetime.now()},where={"unid":"**"}))

#print(db.temp.sort({"unid":"**"}))
#print(db.filter({"unid":"**"},dict=db.read())['data'])

#print(db.en.update('How-to-add-the-bbPress-forum-to-WordPress-posts-as-comments',{"likes": decrement(1) }))
#for x in glob('Blogdb/*/*'):
 #   print(x)
    #with open(x) as f:
     #   data = json.load(f)
   # dic.append(data)

#while True:
 #db.write('col',dic)
# print(len(db.filter(
#            {"he":"afen"}
#           )['data']))
#print(len(db.read('cole')['data']))


#print(db.filter({'title':'ahello'}))


#print(len(db.read('col')['data']))
  
  
# for x in retult:
#   print(x)
#   break
  #pass
  
  
#print(len(db.sort({"title"},DES)['data']))
#print(db.trash('df'))
#print(len(db.sort('cole',{'title'})['data']))
#print(d)
# p = 1
# for xx in range(1):
#   for x in d:
#         print(p,len(d))
#         p+=1
#         db.write('new',x)

# with open('./Blogdb/Blogdb.bin','rb') as ff:
#    data = json.load(ff)
#    print(data)
      
#print(len(db.filter('new',{"title":"**"})['data']))

#print(db.trash('cole',dropkey='data',where={"unid":"20204159367924604"}))

#db.gen.update({'title':'dfdfdfd'},where={"title":"hello"})
#print(db.gen.trash(where={"title":"dfdfdfd"}))
#print(db.gen.filter({"title":"hello"}))
#print(len(db.read('col')['data']))

#print(db.gen.sort({'title'}))

#print(db.gen.write('jo',dic))
#print(db.update({"title":"hffff"},where={"title":"hello"}))

print(datetime.now() - startTime)



#rint(db.move.update('helld0',{"s":"gooh"},{"name":{"test":"shivjeet"}}))

