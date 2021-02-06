import json
import requests

site="https://api.npoint.io/2b57052af2060e84dc86"
# {"name":"blogger","users":[["admins","1","2","3"],["editors","4","5","6"]]}

# Your code goes here
def convertToInt(str):
    try:
        int(str)
        return int(str)
    except ValueError:
        return False

def convert_number(li):
    thelist = []
    for i in li:
        numI = convertToInt(i)
        if numI != False:
            thelist.append(numI)
    return thelist
    
def replace_number(number_list, being_replace, to_replace):
    for i in number_list:
        if i == being_replace:
            x = number_list.index(i)
            number_list.remove(i)
            number_list.insert(x, to_replace)
    return number_list

# Trying to load JSON into text
r = requests.get(site)
print(r.json())
text = r.json()['users']

# Debug
for i in text:
    print("parse " + str(i))

# call the function convert_number
# convert all elements (except the first one) into number and return it as a list

y = convert_number(text[0]) 

print("y")
print(y)

# call the function replace_number
# replace all number 1 by the number 10 in the function


z = replace_number(number_list = y, being_replace = 1, to_replace = 10)

print("z")
print(z)

sum = 0
for i in z:
    sum = sum + i
    print("sum = " + str(sum) + "; i =" + str(i))
print ("Total = " + str(sum))