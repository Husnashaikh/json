import json
dict1={"a":3,"b":4,"h":7+7j}
for i in dict1:
    if type(dict1[i])==complex:
        print("complex hai")
    else:
        print("complex nahi hai")

# a=100
# b=50
# print(a|b)