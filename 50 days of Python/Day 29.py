# --------------------------------------------------------------------------------------QUE-1----------------------------------------------------------------------------------
# Write a function that removes duplicate values from a dictionary and returns the modified dictionary.
# original_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 1}
# result = remove_duplicates(original_dict)
# Output: {'a': 1, 'b': 2}
# d1 = {'a': 1, 'b': 2, 'c': 2, 'd': 1}
# d2={}
# uv = set()
# for key,value in d1.items():
#     if value not in uv:
#         d2[key]=value
#         uv.add(value)
# print(d2)

# --------------------------------------------------------------------------------------QUE-2-------------------------------------------------------------------------------

# Write a function that finds and returns a dictionary containing common key-value pairs between two dictionaries.
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 2, 'd': 4}
# result = common_elements(dict1, dict2)
# Output: {'b': 2}
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'd': 4}
# for k,v in d1.items():
#     for k1,v1 in d2.items():
#         if k==k1 and v==v1:
#             print("Common",{k:v})
