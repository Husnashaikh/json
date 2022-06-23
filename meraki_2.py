import json
a={"name":"David","class":"I","age":6}
y=open("my_data.json","w")
json.dump(a,y,indent=2)
y.close()



















