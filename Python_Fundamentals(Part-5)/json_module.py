import json

# json_str = '{"name" : "Jibitesh","isTeacher" : true}'
# json_str = '{"name" : "Jibitesh","isTeacher" : null}'
# print(type(json_str))

#*json.loads()
# py_obj = json.loads(json_str)
# print(type(py_obj), py_obj)

#*O/P: 
# <class 'dict'> {'name': 'Jibitesh', 'isTeacher': True}
#<class 'dict'> {'name': 'Jibitesh', 'isTeacher': None}


#---------------------x-----------------------------------

#*json.dumps()
# py_obj = {
#     "name" : "jibitesh",
#     "isTeacher" : True
# }

# json_str = json.dumps(py_obj)
# print(type(json_str), json_str)

#*O/P:
#<class 'str'> {"name": "jibitesh", "isTeacher": true}

#---------------------------x------------------------------

#*json.load()

# with open("data.json",'r') as f:
#     py_obj = json.load(f)
#     print(type(py_obj),py_obj)

#*json.dump()
#*Parameter-> First py_object then file

data = {
    "name" : "jibitesh",
    "subject" : ["ai-ml","python"],
    "age" : 21

}
#*In json.dump() [It takes python object and convert to json] so while write (we take python)

with open("data.json",'w') as f:
    json.dump(data,f, indent=4, sort_keys=True)





