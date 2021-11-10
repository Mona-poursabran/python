def sort_values (dictionary):   # Function without using the sorted() function
    value = list(dictionary.values())
    value.sort()
    sort_dict ={}
    for v in value :
        for k in dictionary.keys():
            if dictionary[k] == v : 
                sort_dict[k] = dictionary[k]
    return sort_dict 

val_str= {"a": "a", "b": "A", 1: "", "green": "1"}
val_int = { "b": 1, "a": 4, "c": -1, "d" : 1}


sort_dict_val_int = sort_values(val_int)
sort_dict_val_srt = sort_values(val_str)


dict = {}
sort = sorted(val_int, key=val_int.get)
for k in sort :
    dict[k] = val_int[k]

print("Sorted function: ",dict, "\n")

print(f"Sort {val_int}   ====>  ", sort_dict_val_int,"\n") 
print(f"Sort {val_str}   ====>  ", sort_dict_val_srt, "\n") 






