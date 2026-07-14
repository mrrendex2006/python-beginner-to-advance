#dictionaries are date in key and value pair where keys are immutable and can't be repeated
#and values are mutable 
# creating a dictionary of info of students 
info={"name":"yash singh","age":19,"education":"b.tech AI enginearing","city":"mau" }
# accessing values using key
print(info["name"])
print(info["age"])
#adding and updating keys and values  of a dictionary
info["city"]="vanarash"
info["age"]=20
print(info)

#removing items 
info.pop("city")
#dictionary methods 
info.keys()#retuns all keys 
info.values()#return all values 
info.items()#return all key value pair as turple 
info.get("education")
print(info)
#info.update("city":"district")

