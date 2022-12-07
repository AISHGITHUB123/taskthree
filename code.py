def get_value(obj:dict,key_list:list):  
    for key in key_list:
        try:
            obj = obj[key]
        except KeyError:
            return None #return none if provided key is not found
    return obj


obj = {'a':{'b':{'c':3}}}    # object
key_list = list(input().split("/"))  #splitting the key at / to pass it on the above iteration

print(obj,key_list) 
print(get_value(obj,key_list))
