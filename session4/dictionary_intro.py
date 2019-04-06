person = {
    "name": "duc",
    "age" : 21,
    "uni" : ["ftu"],
    "gf-ex": 3,
}

#key: value

#1. READ
# print(person)
# print(person["name"])

#loop by key 
# for key in person.keys():
#     print(key)


# # loop by value     
# for value in person.values()
#     print(value)

#loop by item 
for key , value in person.items():
    print(key, value)    


#CREATE or UPDATE
# person["gender"] = "unknow"
# person['gf-ex'] = 5
# print(person)

#3.DELETE
# del person["age"]
# print(person)

# uni = person["uni"]
# uni.append("hnu")
# print(person)