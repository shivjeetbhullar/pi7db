class error:
    e0 = {"Error":"Error! Key Can't Changed Because Your Data Is Encrypted With Old Key.\n If You Wnat To Change Key Use Function db.Changekey('Old_Key','New_Key')","status":0}
    e1 = {"Error":"Error! Old_key Is Not Correct.","status":0}
    e2 = {"Error":"Error! Only Dict Value Accepted. For Example: {'Key':'value'}.","status":0}
    def e3(file_name):
        return {"Error":f"Error File {file_name} Not Exist!","status":0}
    e4 = {"Error":"Write Function Takes Collection Name, Data_Name And Dict Data For Example: db.collection_name.write('data_name',{'key':'value'})","status":0}
    def e5(operator):
        return {"Error":f"{operator} Only Apply On Integers!","status":0}
    e6 = {"Error":"Error! Data Is Encrypted With Key Please Use Key Your Key. For Example db.key(YOUR_KEY) ","status":0}
    def e7(old_name):
      return {"Error":f"{old_name} Doc Not Exist!","status":0}
    e8 = {"Error":"Error! Collection Name Is Require For Write Data During Update.","status":0}

class success:
    def s0(file_name, coll_name):
      return {"success":f"Success! {file_name} Created in Collection {coll_name}!","status":1}
    def s1(counter):
      return {"success":f"Success! {counter} Values Updated","status":1}
    def s2(key_name,file_name):
      return {"success":f"Deleted! {key_name} Deleted From {file_name}!","status":1}
    def s3(file_name):
      return {"success":f"Deleted! {file_name}!","status":1}
    def s4(coll_name):
      return {"success":f"Deleted! Collection {coll_name.split('/')[-1]} Deleted Successfully!","status":1}
    def s5(old_name,new_name):
      return {"success":f"{old_name} Doc Is Renamed To {new_name} Successfully!","status":1}
    
class info:
    i0 = {"info":f"Failed! Database Can't Be Deleted In This Way!","status":2}