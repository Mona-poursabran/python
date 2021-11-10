def sort_dict (dictionary, reverse= True) :
    value = list(dictionary.values())
    value.sort(reverse= reverse) 
    sort_dict ={} 
    for v in value:
        for k in dictionary.keys():
            if dictionary[k] == v :
                sort_dict[k] = dictionary[k]
    if reverse == False :
        re= " This sort is ascending(Koochak be bozorg)"
    else:
        re = "This sort is decending(Bozorg be koochak)"
    return sort_dict , re

def sort (dictionary, reverse = True):
    s = dict(sorted(dictionary.items(), key= lambda x : x[1], reverse= reverse))
    return s

def return_value(x):
    return x[1]
def sorting (dic, reverse= True):
    print(dict(sorted(dic.items(), key=return_value, reverse= reverse)))

val_int = { "b": 1, "a": 4, "c": -1, "d" : 1}
val_str= {"a": "a", "b": "A", 1: "", "green": "1"}

sorting(val_int, False)

result_str = sort_dict(val_str, False)
result_int = sort_dict(val_int)

re_s_int = sort(val_int, reverse= False)
re_s_str = sort(val_str)

print(" ",result_str[0],"\n",result_str[1], "\n" ) 
print("", result_int[0],"\n",result_int[1], "\n" ) 

print(re_s_str,"This sort is ascending","\n" ) 
print(re_s_int,"This sort is decending","\n" ) 