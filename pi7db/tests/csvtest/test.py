import os
import pandas as pd
class tabledb:
  def __init__(self,db_name):
   self.db_name = db_name
   if not os.path.exists(db_name):os.mkdir(db_name)
 
  def create_table(self,**kwargs):
   if 'name' in kwargs and 'colums' in kwargs and isinstance(kwargs['name'],str) and isinstance(kwargs['colums'],list):
    file_path = os.path.join(self.db_name,f"{kwargs['name']}.csv");kwargs['colums'].insert(0,'un_id')
    if not os.path.exists(file_path):
     df = pd.DataFrame(columns = kwargs['colums']) 
     df.to_csv(file_path,index=False, sep=',',encoding='utf-8')
    else:
     return "PATH ALREADY EXIST"
   else:
     return "NOT PROPER METHOD"
 
  def re_config_table(self,**kwargs):
   if 'name' in kwargs:
    if isinstance(kwargs['name'],dict):
     file_path = os.path.join(self.db_name,f"{list(kwargs['name'])[0]}.csv")
     if os.path.exists(file_path):os.rename(file_path,os.path.join(self.db_name,f"{kwargs['name'][list(kwargs['name'])[0]]}.csv"))
    if isinstance(kwargs['name'],str):
     file_path = os.path.join(self.db_name,f"{kwargs['name']}.csv");df=pd.read_csv(file_path)
     if 'colums' in kwargs and isinstance(kwargs['colums'],dict):
      df = df.rename(kwargs['colums'], axis='columns')
      df.to_csv(file_path,index=False,mode='w', sep=',',encoding='utf-8')
    else:return "TABLE NOT FOUND"
  

 
   
db = tabledb('shivjeet')
#db.create_table(name="yes",colums=["naam","no","yo"])
db.re_config_table(name="yes",colums={"NAME":"Name","ADM-NUMBER":"Admission-no","YEAR":"Year"})


