import re
import checker

list1 = ['how', 'why', 'however', 'where', 'never']

#Ex1a
def match(pattern):
    return re.match("[0-1][0-1][0-1]+([a-z]*[A-Z]*[0|1]*)*", pattern)
    
if(match("111dsadas")!="None"):
    print("True")
else:
    print("False")

#Ex1b
def find(pattern):
    return re.findall("[a-z]*ly", pattern)

print(find("it is likely to happen rarely"))

#Ex1c
def sub(pattern):
    return re.sub("wh[a-z]*", "WH-word", pattern)

print(sub("who should do what?"))

#Ex2
for a in ['how', 'why', 'however', 'where', 'never']:
    print("*" + " " + a[:2] + " " + a)
    
#Ex3
for a in list1:
    if(a[:2]=="wh"):
        print("*" + " " + a[:2] + " " + a)
    else:
        print("-" + " " + a[:2] + " " + a)
        
#Ex4
#def checkPrefix(list, prefix):
#    for a in ['how', 'why', 'however', 'where', 'never']:
#        if(a[:2] == prefix):
#            print("*" + " " + a[:2] + " " + a)
#        else:
#            print(a[:2] + " " + a)
            
#Ex5

print(checkPrefix(a, "wh"))
