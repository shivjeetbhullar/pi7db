import json,os,datetime,glob,random,orjson
from ..operators import *
from .. import cryptopidb as crdb
from ..status import error,success,info

def openjson(file_path,key=None):
     if key is None:
       with open(f"{file_path}","rb") as f:return orjson.loads(f.read())
     else:
       data = crdb.decrypt_file(file_path,key.encode())
       return json.loads(data)

def writejson(file_path,data,key=None):
     if key is None:
      with open(f"{file_path}", "wb") as f:f.write(orjson.dumps(data))
      return True
     else:
      jsdata = json.dumps(data);crdb.encrypt_file(file_path,key.encode(),jsdata)
      return True

def extractfiles(path,Dic_data):
  remove_files,data_files = [f"{x}.bin" for x in Dic_data['REMOVE']],[]
  for root, dirs, files in os.walk(path):
      for x in files:
        if x not in remove_files:data_files.append(f"{root}/{x}")
  return data_files

def trashbyfilter(dic_data,key_name,config):
 if len(dic_data):
  all_trash = []
  for x_path in dic_data:
   if x_path['cr_dc_path'] not in all_trash:all_trash.append(x_path['cr_dc_path'])
  for tr_path in all_trash:
    if not tr_path[-9:] == "pi7dbauto":
      if key_name is not None:
       tr_data = openjson(tr_path,config['secret-key']);tr_data.pop(key_name)
       writejson(tr_path,tr_data,config['secret-key'])
      else:os.remove(tr_path)
    else:
      v_data = openjson(tr_path[:-9],config['secret-key'])
      if isinstance(v_data,list):
        for x_data in v_data:
          if x_data in dic_data:
            if key_name is not None:x_data.pop(key_name)
            else:v_data.remove(x_data)
        writejson(tr_path[:-9],v_data,config['secret-key'])
  return True

def updatebyfilter(dic_data,commands,config):
 if len(dic_data):
  all_update = []
  for x_path in dic_data:
   if x_path['cr_dc_path'] not in all_update:
     all_update.append(x_path['cr_dc_path'])
  for up_path in all_update:
    if not up_path[-9:] == "pi7dbauto":
      js_data=openjson(up_path,config['secret-key']) 
      for x in commands:
        if increment_v in commands:js_data[x] = js_data[x]+commands[x][increment_v]
        elif decrement_v in commands:js_data[x] = js_data[x]-commands[x][decrement_v]
        else:js_data.update({x:commands[x]})
      writejson(up_path,js_data,config['secret-key'])
    else:
      v_data = openjson(up_path[:-9],config['secret-key'])
      if isinstance(v_data,list):
        for x_data in v_data:
           for x in commands:
            if increment_v in commands[x]:x_data[x] = x_data[x]+commands[x][increment_v]
            elif decrement_v in commands[x]:x_data[x] = x_data[x]-commands[x][decrement_v]
            else:x_data.update({x:commands[x]})
        writejson(up_path[:-9],v_data,config['secret-key'])
  return success.s1(commands)



def appendjson(file_path,data,key=None):
     if key is None:
      with open(file_path,'r+') as f:
        f.seek(os.stat(file_path).st_size-1)
        fast_data = f",{json.dumps(data)}]" 
        f.write(fast_data) 
     else:
      dic_data = json.loads(crdb.decrypt_file(file_path,key.encode()))
      dic_data.append(data)
      dic_data = json.dumps(dic_data);crdb.encrypt_file(file_path,key.encode(),dic_data)
     return True

def writenodoc(col_path,dic_data,config):
     path,files=f"{col_path}/{datetime.date.today().year}",[]
     if not os.path.exists(path):os.makedirs(path)
     for x in glob.glob(f"{path}/*"):
      if os.path.getsize(x) < config['doc_size']:files.append(x)
     if len(files):
       dic_data['cr_dc_path'] = f"{files[0]}pi7dbauto"
       appendjson(files[0],dic_data,config['secret-key'])
     else:
       cr_time = datetime.datetime.now().strftime("%Y%M%S%f")
       dic_data['cr_dc_path'] = f"{path}/{cr_time}{random.randint(10000, 99999)}.{config['enc_type']}pi7dbauto"
       writejson(dic_data['cr_dc_path'][:-9],[dic_data],config['secret-key'])

def extract_kwargs(kw_dic,db_name):
     if 'REMOVE' in kw_dic:
        if isinstance(kw_dic["REMOVE"],str):kw_dic["REMOVE"]=[kw_dic["REMOVE"],db_name]
        if isinstance(kw_dic["REMOVE"],list):kw_dic["REMOVE"]=kw_dic["REMOVE"].append(db_name)
     else:kw_dic["REMOVE"]=[db_name]
     if len(kw_dic):
      if 'FIRST' in kw_dic:return {"f_a":None,"l_a":kw_dic['FIRST'],"REMOVE":kw_dic["REMOVE"]}
      if 'LAST' in kw_dic:return {"f_a":-kw_dic['LAST'],"l_a":None,"REMOVE":kw_dic["REMOVE"]}
      if 'FROM' in kw_dic:kw_dic["f_a"] = kw_dic['FROM']
      else:kw_dic["f_a"]=None
      if 'TO' in kw_dic:kw_dic["l_a"] = kw_dic['TO']
      else:kw_dic["l_a"]=None
      return kw_dic
     else:return {"f_a":None,"l_a":None,"REMOVE":kw_dic["REMOVE"]}

def keys_extractor(dic):
  data,current_pair,bool = {"keys":[],"sub_keys":[None],"value":[]},dic,True
  while bool:
   for x in current_pair:
     try:
      if len(current_pair.keys()) > 1:data['sub_keys'],bool,data['value'] = list(current_pair.keys()),False,list(current_pair.values());break
      else:data['keys'].append(x);current_pair[x].keys();current_pair = current_pair[x]    
     except:bool,data['value'] = False ,list(current_pair.values())
  return data

def operator_fil(js_data,F_data,value,op_action,action,word_len):
  r_data = []
  if op_action == LET:
   if js_data < value:r_data.append(F_data)  
  elif op_action == GRT:
   if js_data > value:r_data.append(F_data)
  elif action == "fr_skip": 
   if js_data[word_len:] == value:r_data.append(F_data) 
  elif action == "ba_skip":
   if js_data[:word_len] == value:r_data.append(F_data) 
  elif action == "all_skip":
   if value in js_data:r_data.append(F_data) 
  else:
   if js_data == value:r_data.append(F_data)
  try:return r_data[0]
  except:pass

def op_actionfunc(command_tup,command):
   op_action = None
   if isinstance(command_tup[command],tuple):
    value,op_action = command_tup[command][1],command_tup[command][0]
    if not isinstance(value,int):return error.e5(op_action)
   else:value = command_tup[command]
   action,word_len = None,0
   if isinstance(value,str):
    if value[-2:] == '**' and value[:2] == '**':word_len,value,action = len(value[2:-2]),value[2:-2],"all_skip"
    if value[-2:] == '**':word_len,value,action = len(value[:-2]),value[:-2],"ba_skip"
    if value[:2] == '**':word_len,value,action = -int(len(value[2:])),value[2:],"fr_skip"
   return op_action,value,action,word_len

def andfilter(command_tup,config,all_data):
  r_data,enc_key = [],config['secret-key']
  for command in list(command_tup):
   op_action,value,action,word_len = op_actionfunc(command_tup,command)
   if isinstance(value,str) or isinstance(value,int):
    if not r_data:
     for F_data in all_data:
       try:
        fr_data = operator_fil(F_data[command],F_data,value,op_action,action,word_len)
        if fr_data:r_data.append(fr_data)
       except:pass
     if not r_data:return []
    else:
     dup_data,r_data = r_data,[]
     for F_data in dup_data:
       try:
        fr_data = operator_fil(F_data[command],F_data,value,op_action,action,word_len)
        if fr_data:r_data.append(fr_data)
       except:pass
     if not r_data:return []
   
   if isinstance(value,list):
    if not r_data:
     for F_data in all_data:
       try:
        if all(item in F_data[command] for item in value):fr_data = F_data      
        else:continue
        if fr_data:r_data.append(fr_data)
       except:pass
     if not r_data:return []
    else:
     dup_data,r_data = r_data,[]
     for F_data in dup_data:
       try:
        if all(item in F_data[command] for item in value):fr_data = F_data
        else:continue 
        if fr_data:r_data.append(fr_data)
       except:pass
     if not r_data:return []

   if isinstance(value,dict):
    keys_extract = keys_extractor(value)
    for s_k in enumerate(keys_extract['sub_keys']):
     if s_k[1] is None:key_tup,value = f"F_data['{command}']"+str([[x] for x in keys_extract['keys']])[1:-1].replace(', ',""),keys_extract['value'][0]
     else:key_tup,value = f"F_data['{command}']"+str([[x] for x in keys_extract['keys']])[1:-1].replace(', ',"")+f"['{s_k[1]}']",keys_extract['value'][s_k[0]]
     if not r_data:
      for F_data in all_data:
       try:
        exec('global globalfilter; globalfilter = %s' % key_tup)
        fr_data = operator_fil(globalfilter,F_data,value,op_action,action,word_len)
        if fr_data:r_data.append(fr_data)     
       except:pass
      if not r_data:return []
     else:
      dup_data,r_data = r_data,[]
      for F_data in dup_data:   
       try:
        exec('global globalfilter; globalfilter = %s' % key_tup)
        fr_data = operator_fil(globalfilter,F_data,value,op_action,action,word_len)
        if fr_data:r_data.append(fr_data)
       except:
        pass
      if not r_data:return []
  return r_data

def create_coll(path):
  if not os.path.exists(path):os.mkdir(path)