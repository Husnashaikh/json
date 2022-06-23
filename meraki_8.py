import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]
b={}
c={}
d={}
e={}
key=["name","designation","age","salary"]
c=({'b':b,'c':c,"d":d,"e":e})
for i in range (len(list1)):
    b.update({key[i]:list1[i]})
for j in range (len(list2)):
    c.update({key[j]:list2[j]})
for k in range (len(list3)):
    d.update({key[k]:list3[k]})
for h in range (len(list4)):
    e.update({key[h]:list4[h]})
with open("meraki q no1","w") as g:
    json.dump(c,g,indent=7)