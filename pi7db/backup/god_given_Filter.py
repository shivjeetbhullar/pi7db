

def check_GT_LT(d1,d2):
    if "GT" in d1[0] and isinstance(d1[1],int):
        if d1[1] < d2:return True
        else:return False
    elif "LT" in d1[0] and isinstance(d1[1],int):
        if d1[1] > d2:return True
        else:return False
    elif "GET" in d1[0] and isinstance(d1[1],int):
        if d1[1] <= d2:return True
        else:return False
    elif "LET" in d1[0] and isinstance(d1[1],int):
        if d1[1] >= d2:return True
        else:return False
    
    else:return False;

def checkli_stin(l1,l2):
    return all(item in l2 for item in l1)


d1= {"a":{'b':[{"cs":("LET",100),"like":("GT",10)}]},"li":("GT",0),'newa':[1,2,5]}
d2= {"li":10,'a':{'b':[{'cs':10,"like":50},{"css":100}] ,'d':{'cs':[20,50,60,70]}},'newa':[1,2,5]}


def checklist(l1,l2):
    for xx in enumerate(l1):
      for x in enumerate(l2):
        output = findDiff(l1[xx[0]],l2[x[0]])
        if output is None :break
    if output is None or output is True:return True 
    else:return False

boole = False
def findDiff(d1, d2):
    global boole
    for key in d1:
      if (key not in d2):pass
      else:
        if isinstance(d1[key],dict):
            if findDiff(d1[key],d2[key]) is False:return False
        elif type(d1[key]) is list:
          if all(isinstance(s, dict) for s in d1[key]):
            if checklist(d1[key],d2[key]) is False:boole = False;return False
          if all(isinstance(s, str) for s in d1[key]) or all(isinstance(i, int) for i in d1[key]):
              if checkli_stin(d1[key],d2[key]):boole = True
              else:boole = False;return False
        else:
          print(d1[key],7777)
          if isinstance(d1[key],tuple):
             if check_GT_LT(d1[key],d2[key]):boole = True
             else:boole = False;return False
          elif d1[key] == d2[key]:boole = True
          else:boole = False;return False
    
    return boole
    

dd = findDiff(d1,d2)
print(dd)
if dd is True:print("Found")
else:print("NOT FOUND")
