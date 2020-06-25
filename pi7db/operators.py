# Operators
OR = "OR"
GET = "GRT"
LET = "LET"
GT = "GT"
LT = "LT"

ASC=asc= False
DSC=dsc= True
increment_v = "Add++"
decrement_v = "Subtract--"

def increment(num):
    return {increment_v:num}

def decrement(num):
    return {decrement_v:num}

def replace_in_list(For_list,With_list):
    if not isinstance(For_list,list) and not isinstance(With_list,list):
        For_list,With_list=[For_list],[With_list]
    return {'$replace':(For_list,With_list)}