size_list = 6

def search_from_hash(key, hash_list):
    search_index = hash_function(key)
    if hash_list[search_index] == key:
        print("Value Found")
    else:
        print("Value not in the list")

def hash_function(value):
    global size_list
    return value%size_list

def map_hash2index(hash_return_val):
    return hash_return_val


def create_hash_table(list_val, main_list):
    for value in list_val:
        hash_return_val = hash_function(value)
        list_index = map_hash2index(hash_return_val)
        if main_list[list_index][0]:
            main_list[list_index].append(value)
        else:
            main_list[list_index][0] = value
        
        '''
        if list_val[list_index]:
            print("Collision Detected")
        else:
            list_val[list_index] = value
        '''


list_val = [1,3,4,5,8,60,30]
main_list = [[None] for x in range(6)]  #added list of list
print(main_list)
create_hash_table(list_val, main_list)
print(main_list)