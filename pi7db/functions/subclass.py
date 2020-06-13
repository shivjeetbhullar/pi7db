from .functions import *
import os,errno,glob,shutil
from ..status import error,success,info
from ..operators import *
from datetime import datetime,timedelta

class subclass:
  def __init__(self):
      pass
  
  def write(self,fn_dict,data=None):
   if isinstance(fn_dict,dict):fn_dict['$temp_time']=datetime.now()
   elif isinstance(data,dict):data['$temp_time']=datetime.now()
   return self.p_write('$temp',fn_dict,data)
  
  def read(self,file_name=None,key_name=None,**kwargs):
   self.key(self.config)
   kwargs,data_files,r_data = extract_kwargs(kwargs,self.db_name),[],{"data":[],"status":1}
   if key_name is not None:return {"data":opendoc(f"{self.db_np}/$temp/{file_name}",self.config['secret-key'])[key_name],"status":1}
   elif file_name is not None:data_files=[f"{self.db_np}/$temp/{file_name}"]
   else:data_files = extractfiles(f"{self.db_np}",kwargs)
   for x_file in data_files[kwargs['f_a']:kwargs['l_a']]:
     o_data = opendoc(x_file,self.config['secret-key'])
     if isinstance(o_data,list):
       for x_dict in o_data:
         if x_dict['$temp_time']+timedelta(minutes=self.temp_limt) < datetime.now():o_data.remove(x_dict)
         else:r_data['data'].append(x_dict)
       writedoc(x_file,o_data,self.config['secret-key'])
     else:
       if o_data['$temp_time']+timedelta(minutes=self.temp_limt) < datetime.now():os.remove(o_data['cr_dc_path'])
       else:r_data['data'].append(o_data)
   return r_data

  def trash(self,file_name=None,key_name=None,**kwargs):
   return self.p_trash('$temp',file_name,key_name,**kwargs)
  
  def sort(self,sort_key,**kwargs):
   return self.p_sortdict(self.read(),sort_key,**kwargs)

  def filter(self,F_dict,**kwargs):
   kwargs['dict'] = self.read()
   return self.p_filter(F_dict,**kwargs)
  
  def update(self,file_name,data_arg=None,**kwargs):
    return self.p_update('$temp',file_name,data_arg,**kwargs)