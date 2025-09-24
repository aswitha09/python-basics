#dictionary:
# creating dictionary:
# normal dictionary:
biodata = {
    "name": "aswitha",
    "roll.no":"Q0",
    "branch":"CSE AI&ML",
      "place":"yapral"
}
#print(biodata)

# dicrionary using 
#biodata = dict(name = "ashu",roll_number = "Q0",branch = "CSE AI&ML",place = "yapral")
#print(biodata1)

# square brackets []:
print(biodata["name"])
print(biodata["roll.no"])
print(biodata["branch"])
print(biodata["place"])

#using get() method:
print(biodata.get("name"))
print(biodata.get("roll.no"))
print(biodata.get("branch"))
print(biodata.get("place"))
print(biodata.get("age"))

#adding and updating dictionary:
biodata["age"] = 18
print(biodata)
biodata["place"] = "hyderabad"
print(biodata)

biodata = {
    "name":"sairam",
    "roll.num":"F9",
    "branch":"CSE AI&ML",
    "place":"charminar",
     "role":"charminar_model"
     }
print()
# removing in dictionary:{}
#"name":"sairam",
#"roll.no":"F9",
#"branch":"CSE AI & ML",

#loops for dictionary:
l = [10,20,30,40,50]
for i in l:
    print(i)
biodata = {
    "name":"sairam",
    "roll.num":"F9",
    "branch":"CSE AI&ML",
    "place":"charminar",
     "role":"charminar_model"
     }  
for i in biodata:
    print(i) 

for i in biodata.keys():
    print(i)

for i in biodata.values():
    print(i)

for i in biodata.items():
    print(i)   

# nested tuple:
t = (10,(20,30),(40,50))  
print(t[2][1])

# nested dictionary

students = {
    "s1":{"name":"ashu","rollno":"Q0"},
    "s2":{"name":"ramya","rollno":"l0"},
    "s3":{"name":"laxmi","rollno":"r2"},
}
print(students["s1"]["name"])
print(students["s2"]["name"])
print(students["s3"]["name"])
print(students["s1"]["rollno"])
print(students["s2"]["rollno"])
print(students["s3"]["rollno"])