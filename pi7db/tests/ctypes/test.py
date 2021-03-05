import ctypes
import orjson,json
import glob
import os
from datetime import datetime
ll=glob.glob("../Blogdb/gen/*.bin")

def cread(list_files):
  cc = []
  libfoo = ctypes.cdll.LoadLibrary('./testlib.so')
  L = [x.encode() for x in list_files]
  arr = (ctypes.c_char_p * len(L))()
  arr[:] = L
  foo = libfoo.myprint
  foo.argtypes = ()
  foo.restype = ctypes.POINTER(ctypes.c_char_p)
  result = foo(arr,len(L))
  for x in range(len(L)):  
   try:cc.append(orjson.loads(result[x]))
   except:
     with open(ll[x],'rb') as f:
      data = orjson.loads(f.read())
     cc.append(data)
  return cc
  
start = datetime.now()
print( len(cread(ll)))

print(datetime.now()-start)

start = datetime.now()
for xx in range(10): 
 for x in ll:
  with open(x,'rb') as f:
     data = json.load(f)
    
print(datetime.now()-start)
