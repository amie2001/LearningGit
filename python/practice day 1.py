lst =[-22,(20,10),{11,32},{},{},[40,50],3,4,
{"a":"b"},0 ]
count=0
for i in range(len(lst)):
    if type(lst[i])is list:
        count = i
    elif type(lst[i])is tuple:
        count = i
    elif type(lst[i])is set:
        count = i
    elif type(lst[i])==dict:
        count = i
    else :
        count += 1
        print("Count = ", count)
