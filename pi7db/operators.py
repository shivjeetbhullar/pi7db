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