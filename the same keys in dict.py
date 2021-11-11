def sum_same_keys (lst):
    for dict in lst :
        for k in dict.keys():
           new_dic[k] = new_dic.get(k,0) + dict[k]

    result = [(k, v) for k, v in new_dic.items()]   # list(dic.items())
    return result

lst = [{"apple":14,"carrot":5, "banana":9},
 {"apple":3, "lime":10},
 {"carrot":6, "pear":8, "lime":1}]

new_dic = {}

print(sum_same_keys(lst))


