import os,errno,hashlib,shutil,datetime,random,csv as csvm
from .status import error,success,info
from .functions.functions import *
from .functions.subclass import subclass
from .operators import *
from pathlib import Path

class pi7db:
  def __init__(self,db_name,db_path=""):
   self.db_np,self.db_name,self.doc_size,self.temp_limt = os.path.join(db_path,db_name),db_name,15000000,120
   self.config_file,self.coll_name = os.path.join(self.db_np,db_name),None
   if not os.path.exists(self.db_np):os.makedirs(self.db_np)
   if not os.path.exists(f"{self.config_file}"):
    self.config = {'secret-key':None,'doc_size':self.doc_size}
    writedoc(f"{self.config_file}",self.config)
   else:self.config={'secret-key':None,'doc_size':self.doc_size}
     
  def __getattr__(self, attrname):
   if attrname == "temp":
    path=self.coll_name=os.path.join(self.db_np,attrname)
    SubClass = type(attrname,(subclass,),{'key':self.key,'config_file':self.config_file,'p_filter':self.filter,'p_sortdict':self.sortdict,'p_update':self.update,'p_trash':self.trash,'p_write':self.write,'config':self.config,'db_np':self.db_np,'db_name':self.db_name,"temp_limt":self.temp_limt})
    SubClass = SubClass()
    return SubClass
  
  def key(self,password):
   if 'load_point' in self.config:return self.config
   else:self.config={**opendoc(f"{self.config_file}"),'load_point':1}
   
   if isinstance(password,dict):
     if password['secret-key'] is None and self.config['secret-key'] is not None:raise ValueError(error.e6)
     else:key=password['secret-key']
   else:key = hashlib.md5(password.encode()).hexdigest()
   if self.config['secret-key'] is not None:
    if key != self.config['secret-key']:raise ValueError(error.e0)
   else:
     self.config['secret-key'] = key
     writedoc(self.config_file,self.config)

  def changekey(self,old_key,New_key):
   files,old_key,New_key = extractfiles(self.db_np,extract_kwargs({},self.db_name)),hashlib.md5(old_key.encode()).hexdigest(),hashlib.md5(New_key.encode()).hexdigest()
   if old_key == opendoc(self.config_file)['secret-key']:
    for x_js in files:
     writedoc(x_js,opendoc(x_js,old_key),New_key)
    writedoc(self.config_file,{'secret-key':New_key})
   else:raise ValueError(error.e1)

  def rename(self,coll_name,doc_name,new_name):
    path,new_path = os.path.join(self.db_np,coll_name,doc_name),os.path.join(self.db_np,coll_name,new_name)
    if os.path.exists(path):
      self.update(coll_name,doc_name,{"cr_dc_path":new_path})
      os.rename(path,new_path)
      return success.s5(doc_name,new_name)
    else:return error.e7(doc_name)

  def status(self):
    dic = {}
    for f in [f for f in os.scandir(self.db_np) if f.is_dir()]:
      doc = extractfiles(f.path,extract_kwargs({},self.db_name))
      dic[f.name] = {"Total_Files":len(doc),"Doc_Name":map(lambda f:f.split("/")[-1],doc)}
    return dic     
  
  def exists(self,file_name,coll_name=None,**kwargs):
    if coll_name is not None:data_files = extractfiles(f"{self.db_np}/{coll_name}",kwargs)
    else:data_files = extractfiles(f"{self.db_np}",extract_kwargs(kwargs,self.db_name))
    for x_file in data_files:
     if file_name == x_file.split('/')[-1]:
      if 'today' in kwargs and kwargs['today']==True:
        if datetime.date.today() == datetime.date.fromtimestamp(Path(x_file).stat().st_mtime):return True
        else:return False
      else:return True
    return False

  def write(self,coll_name,fn_dict,data=None):
   self.key(self.config)
   path = os.path.join(self.db_np,coll_name)
   if data is None and isinstance(fn_dict,dict) or all([isinstance(x,dict) for x in fn_dict]):
    if isinstance(fn_dict,list):return writenodoc(path,fn_dict,self.config)
    else:fn_dict={'unid':unid(),**fn_dict};return writenodoc(path,fn_dict,self.config)
   else:
    try:
     data_dict={'unid':unid(),**data}
     data_dict['cr_dc_path'] = f"{path}/{fn_dict}";create_coll(path)
     writedoc(data_dict['cr_dc_path'],data_dict,self.config['secret-key'])
     return success.s0(fn_dict, self.coll_name)
    except Exception as e:return error.e4
   
  def update(self,coll_name,file_name=None,data_arg=None,**kwargs):
   self.key(self.config)
   if "where" in kwargs:
     if isinstance(coll_name,str) and isinstance(file_name,dict):
       if isinstance(kwargs['where'],list) or isinstance(kwargs['where'],tuple):updatebyfilter(self.filter(coll_name,*kwargs['where'])['data'],file_name,{**self.config,**kwargs,"coll_name":coll_name,"write_func":self.write})
       else:return updatebyfilter(self.filter(coll_name,kwargs['where'])['data'],file_name,{**self.config,**kwargs,"coll_name":coll_name,"write_func":self.write})
     if isinstance(coll_name,dict) and file_name is None:
      if isinstance(kwargs['where'],list) or isinstance(kwargs['where'],tuple):updatebyfilter(self.filter(coll_name,*kwargs['where'])['data'],coll_name,{**self.config,**kwargs})
      else:return updatebyfilter(self.filter(kwargs['where'])['data'],coll_name,{**self.config,**kwargs})
   try:
    js_data=opendoc(f"{self.db_np}/{coll_name}/{file_name}",self.config['secret-key'])
    if isinstance(data_arg,dict):js_data=nes_update(js_data,data_arg,**kwargs)
    else:return error.e2
    writedoc(f"{self.db_np}/{coll_name}/{file_name}",js_data,self.config['secret-key'])
    return success.s1(1)
   except OSError as e:
    if isinstance(file_name,dict):
     if 'write' in kwargs and kwargs['write']==True:return self.write(coll_name,file_name)
     else:
      if e.errno == errno.ENOENT:return error.e3(None)
    elif e.errno == 2:
      if 'write' in kwargs and kwargs['write']==True:return self.write(coll_name,file_name,data_arg)
      else:return e

  def read(self,coll_name=None,file_name=None,key_name=None,**kwargs):
   self.key(self.config)
   kwargs,data_files,r_data = extract_kwargs(kwargs,self.db_name),[],{"data":[],"status":1}
   if key_name is not None:return {"data":opendoc(f"{self.db_np}/{coll_name}/{file_name}",self.config['secret-key'])[key_name],"status":1}
   elif file_name is not None:data_files=[f"{self.db_np}/{coll_name}/{file_name}"]
   elif coll_name is not None:data_files = extractfiles(f"{self.db_np}/{coll_name}",kwargs)
   else:data_files = extractfiles(f"{self.db_np}",kwargs)
   for x_file in data_files[kwargs['f_a']:kwargs['l_a']]:
     o_data = opendoc(x_file,self.config['secret-key'])
     if isinstance(o_data,list):r_data['data'].extend(o_data)
     else:r_data['data'].append(o_data)
   return r_data
    
  def trash(self,coll_name=None,file_name=None,key_name=None,**kwargs):
   self.key(self.config)
   if len(kwargs):
    if 'dropkey' in kwargs:key_name=kwargs['dropkey']
    if isinstance(coll_name,str) and 'where' in kwargs:
      if isinstance(kwargs['where'],list) or isinstance(kwargs['where'],tuple):trashbyfilter(self.filter(coll_name,*kwargs['where'])['data'],key_name,self.config)
      else:trashbyfilter(self.filter(coll_name,kwargs['where'])['data'],key_name,self.config)
      return True
    if 'where' in kwargs and coll_name is None:
      if isinstance(kwargs['where'],list) or isinstance(kwargs['where'],tuple):trashbyfilter(self.filter(coll_name,*kwargs['where'])['data'],key_name,self.config)
      else:trashbyfilter(self.filter(kwargs['where'])['data'],key_name,self.config)
      return True
   if key_name is not None and isinstance(key_name,set) or isinstance(key_name,dict):
     tr_data = opendoc(f"{self.db_np}/{coll_name}/{file_name}",self.config['secret-key'])
     writedoc(f"{self.db_np}/{coll_name}/{file_name}",nes_trash(tr_data,key_name),self.config['secret-key'])
     return success.s2(key_name,file_name)
   elif file_name is not None and isinstance(file_name,str):
     os.remove(f"{self.db_np}/{coll_name}/{file_name}")
     return success.s3(file_name)
   elif coll_name is not None:
     if isinstance(coll_name,str):coll_name = [coll_name]
     if 'IGNORE' in kwargs:
       if isinstance(kwargs['IGNORE'],str):kwargs['IGNORE'] = [kwargs['IGNORE']]
       for x in coll_name:
        for x_file in extractfiles(f"{self.db_np}/{x}",kwargs):os.remove(x_file)
     else:
      for x in coll_name:shutil.rmtree(f"{self.db_np}/{x}", ignore_errors=False, onerror=None)
      return success.s4(",".join(coll_name))
   elif coll_name is None and 'IGNORE_COLLECTION' in kwargs:
      collections = list(self.status().keys())
      if isinstance(kwargs['IGNORE_COLLECTION'],str):kwargs['IGNORE_COLLECTION'] = [kwargs['IGNORE_COLLECTION']]
      for x in kwargs['IGNORE_COLLECTION']:collections.remove(x)
      for x in collections:shutil.rmtree(f"{self.db_np}/{x}", ignore_errors=False, onerror=None)
      return success.s4(",".join(collections))

  def sort(self,coll_name,command_tup=None,**kwargs):
   self.key(self.config)
   un_ex_kwargs,kwargs,order = kwargs,extract_kwargs(kwargs,self.db_name),False
   if "order" in kwargs:order = kwargs['order']
   if isinstance(coll_name,set):all_data,command_tup=self.read(**un_ex_kwargs),coll_name
   else:all_data=self.read(coll_name,**un_ex_kwargs)
   r_data = {"data":all_data['data'],"status":1}
   if isinstance(command_tup,set):
    key_tup = "i"+str([[x] for x in command_tup])[1:-1].replace(', ',"")
    r_data['data'] = sorted(r_data['data'], key = lambda i:(exec('global s;s = %s' % key_tup),s),reverse=order)
   else: 
    if isinstance(command_tup,str):r_data['data'] = sorted(r_data['data'],key = lambda i: i[command_tup],reverse=order)[kwargs['f_a']:kwargs['l_a']]
   return r_data

  def sortdict(self,dict_list,sort_key,**kwargs):
   kwargs,order,r_data = extract_kwargs(kwargs,self.db_name),False,{"data":dict_list['data'],"status":1}
   if "order" in kwargs:order = kwargs['order']
   if isinstance(sort_key,set):
    key_tup = "i"+str([[x] for x in sort_key])[1:-1].replace(', ',"")
    r_data['data'] = sorted(r_data['data'][kwargs['f_a']:kwargs['l_a']], key = lambda i:(exec('global s;s = %s' % key_tup),s),reverse=order)
   else: 
    if isinstance(sort_key,str):r_data['data'][kwargs['f_a']:kwargs['l_a']] = sorted(r_data['data'],key = lambda i: i[sort_key],reverse=order)
   return r_data
  
  def filter(self,*command_tup,**kwargs):
   self.key(self.config)
   un_ex_kwargs,kwargs = kwargs,extract_kwargs(kwargs,self.db_name)
   if "IGNORE" in kwargs:un_ex_kwargs["IGNORE"] = kwargs["IGNORE"]
   if isinstance(command_tup[0],str):command_tup,all_data = list(command_tup[1:]),[command_tup[0]]
   elif 'dict' in kwargs:all_data = kwargs['dict']
   else:
     if 'IGNORE_COLLECTION' in kwargs:
      if isinstance(kwargs['IGNORE_COLLECTION'],str):kwargs['IGNORE_COLLECTION']=[kwargs['IGNORE_COLLECTION']]
     else:kwargs['IGNORE_COLLECTION']=[]
     all_data = [x for x in self.status().keys() if x not in kwargs['IGNORE_COLLECTION']]
   r_data,command_arr= {"data":[],'status':1},[]
   if OR in command_tup:
    for x_p in command_tup:
      if x_p != OR:command_arr.append(x_p)
    for command in command_arr:
     data_get = no_freeze_filter(self,command,all_data,kwargs,un_ex_kwargs)
     for x_l in data_get:
      for x in x_l:
       if x not in r_data['data']:r_data['data'].append(x)
    return r_data
   else:
    for x_L in no_freeze_filter(self,command_tup[0],all_data,kwargs,un_ex_kwargs):
      for x_r in x_L:r_data['data'].append(x_r)
    return r_data
  
  def readkey(self,coll_name=None,**kwargs):
   if not 'key' in kwargs:raise KeyError("Key Is Required")
   self.key(self.config)
   r_data,kwargs = {"data":[],"status":1},extract_kwargs(kwargs,self.db_name)
   if isinstance(kwargs['key'],str):kwargs['key'] = [kwargs['key']]
   if coll_name is not None:data_files = extractfiles(f"{self.db_np}/{coll_name}",kwargs)
   else:data_files = extractfiles(f"{self.db_np}",kwargs)
   for x_file in data_files[kwargs['f_a']:kwargs['l_a']]:
     o_data = opendoc(x_file,self.config['secret-key'])
     if isinstance(o_data,list):
       for x_dict in o_data:
         dic={}
         try:
           for x in kwargs['key']:dic[x] = x_dict[x]
         except:pass
         r_data['data'].append(dic)
     else:
       dic={}
       try:
         for x in kwargs['key']:dic[x] = o_data[x]
       except:pass
       r_data['data'].append(dic)
   return r_data

class csv:
  def __init__(self,file_path=None):    
   self.file_path = file_path
  
  def csv_read(self,file_path=None,**kwargs):
    if file_path is not None:self.file_path = file_path
    kwargs = extract_kwargs(kwargs,"")
    def checkdigit(num):
      if "no_int" in kwargs:return num
      else:
       if num.isdigit():return int(num)
       else:
         try:return float(num)
         except:return num
    if 'csv_str' in kwargs:csvreader = csvm.reader([x for x in kwargs['csv_str'].splitlines() if x != "" or x.isspace()])
    else:
     with open(self.file_path, 'r') as csvfile:
       csvreader = csvm.reader(csvfile)
    self.fields = list(filter(lambda x: x != "", next(csvreader)))
    rows = [row for row in csvreader]
    self.rows_num = csvreader.line_num
    data = {"data":[],"status":1}
    for row in rows[kwargs['f_a']:kwargs['l_a']]:
     if any(row):
      dic,c = {},0
      for col in row[:len(self.fields)]:
         dic[self.fields[c]] = checkdigit(col)
         c+=1
      data['data'].append(dic)
    return data
  
  def csv_filter(self,*command_tup,**kwargs):
   kwargs = extract_kwargs(kwargs,self.file_path)
   if 'dict' in kwargs:all_data=kwargs.pop('dict')['data']
   else:all_data = self.csv_read(**kwargs)['data']
   r_data,command_arr= {"data":[],'status':1},[]
   if OR in command_tup:
    for x_p in command_tup:
      if x_p != OR:command_arr.append(x_p)
    for command in command_arr:
     data_get = andfilter(command,all_data,kwargs)
     for x in data_get:
      if x not in r_data['data']:r_data['data'].append(x)
    return r_data
   else:
    for x_r in andfilter(command_tup[0],all_data,kwargs):r_data['data'].append(x_r)
    return r_data
    
  def csv_write(self,data,file_path=None,**kwargs):
    if 'write' in kwargs and kwargs['write'] is False:
      csv_str = ''
      csv_str+=','.join(list(data['data'][0].keys()))
      csv_str+=''.join([f"{','.join(map(str, x.values()))}\n" for x in data['data']])
      return csv_str
    else:
     with open(file_path, 'w', newline='') as file:
      writer = csvm.writer(file)
      writer.writerow(list(data['data'][0].keys()))
      writer.writerows([x.values() for x in data['data']])
     return {f"Sucesss! {file_path} Is Created."}
  
  def csv_sort(self,dict_data,sort_key,**kwargs):
   kwargs,order,r_data = extract_kwargs(kwargs,self.file_path),False,{"data":dict_data['data'],"status":1}
   if "order" in kwargs:order = kwargs['order']
   if isinstance(sort_key,set):
    key_tup = "i"+str([[x] for x in sort_key])[1:-1].replace(', ',"")
    r_data['data'] = sorted(r_data['data'][kwargs['f_a']:kwargs['l_a']], key = lambda i:(exec('global s;s = %s' % key_tup),s),reverse=order)
   else: 
    if isinstance(sort_key,str):r_data['data'][kwargs['f_a']:kwargs['l_a']] = sorted(r_data['data'],key = lambda i: i[sort_key],reverse=order)
   return r_data
  
  def csv_trash(self,command):
   data = self.read()
   for x in data['data']:
     if findDiff(command,x):data['data'].remove(x)
   return data

  def csv_update(self,data_arg=None,**kwargs):
   if "where" in kwargs:
    data = self.csv_read()
    for x in data['data']:
     if findDiff(command,x):x.update(data_arg)
    return data
