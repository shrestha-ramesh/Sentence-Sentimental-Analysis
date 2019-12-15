import re
import sys
file_read = open("text.txt", "r")
file_write = open("a.txt", "w")
if len(sys.argv) == 3:
    file_read = open(sys.argv[1], "r")
    file_write = open(sys.argv[2], "w")
text = file_read.read()
dicpos = {}
dicneg = {}
dicmerg={}
text = re.sub(r'[*,~!@#,<>$?%^&()\\/._;+=":\t]', '', text)
text = text.lower()
text = text.replace("-", "")
text = text.replace("'", " ")
text = text.replace("[", "")
text = text.replace("]", "")
text = re.sub(r' +', ' ', text)
text = text.split("\n")
countnegpara = 0
countpospara=0
totalpara = 0
for t in text:
    totalpara += 1
    t = t.split(" ")
    if t[-1] == "pos":
        countpospara += 1
    else:
        countnegpara += 1
    for x in t:
        if t[-1] == "pos":
            if x != "":
                if x in dicpos:
                    dicpos[x] = dicpos[x] + 1
                else:
                    dicpos[x] = 1
        else:
            if x != "":
                if x in dicneg:
                    dicneg[x] = dicneg[x] + 1
                else:
                    dicneg[x] = 1
def mergeDict(dict1, dict2):
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = [value, dict1[key]]
        elif key in dict1:
            dict3[key]= [0, dict1[key]]
        else:
            dict3[key] = [dict2[key], 0]
    return dict3
#neg value in index 0 and pos value in index 1
dict3 = mergeDict(dicpos, dicneg)
pos = dict3.pop('pos')
neg = dict3.pop('neg')
count = 0
countneg = 0
countpos = 0
for key, value in dict3.items():
    countneg += value[0]
    countpos += value[1]
    count += 1
probabilitypos = countpospara/totalpara
probabilityneg = countnegpara/totalpara
print("Probability of negative case")
print("Prabability Negative "+str(probabilityneg))
for key, value in dict3.items():
    file_write.write(key+"  ")
    v1 = (value[0] + 1) / (countneg + count)
    file_write.write(str(v1)+"\n")
print()
print("Probability of positive case")
print("Probability Positive "+str(probabilitypos))
for key, value in dict3.items():
    file_write.write(key+"  ")
    v = (value[1] + 1) / (countpos + count)
    file_write.write(str(v)+"\n")
print()
print("Total paragraph "+str(totalpara))
print("Total positive paragraph "+str(countpospara))
print("Total negative paragraph "+str(countnegpara))
print("Total unique words "+str(count))
print("Total pos "+str(countpos))
print("Total neg "+str(countneg))


