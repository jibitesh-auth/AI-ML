info = {
    "name" : "jibitesh",
    "cgpa" : 8.5,
    "subjects": ["math","science"],
    3.14: "PI"
}

# print(type(info))

# print(info["name"])
# print(info[3.14])

# info["cgpa"] = 9.0
# print(info["cgpa"])


#---------------------x------------------------
#*Method

# *d.keys()

# print(info.keys())
# dict_keys = list(info.keys())
# print(dict_keys)
# print(type(dict_keys))



# *d.values()

# print(info.values())
# dict_values = list(info.values())
# print(dict_values)
# print(type(dict_values))

#*d.items()
# print(info.items())

# for key,values in info.items():
#     print(key,values)

#*d.get(val)
# print(info.get("cgpa2"))
# print("End of code")

# print(info["cgpa2"])
# print("End of code")

#*d.update(new_item)
# info.update({
#     "city":"Delhi"
# })

# print(info)