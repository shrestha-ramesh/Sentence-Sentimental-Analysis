import re
import sys
file_read = open("a.txt", "r")
file_read1 = open("writeinput.txt", "r")
if len(sys.argv) == 3:
    file_read = open(sys.argv[1], "r")
    file_read1 = open(sys.argv[2], "r")
text = file_read.read()
text1 = file_read1.read()
text1 = re.sub(r'[*,~!@#,<>$?%^&()\\/._;+=":\t]', '', text1)
text1 = text1.lower()
text1 = text1.replace("-", "")
text1 = text1.replace("'", " ")
text1 = text1.replace("[", "")
text1 = text1.replace("]", "")
text1 = re.sub(r' +', ' ', text1)
text1 = text1.split("\n")
text = text.split("\n")
app_key = []
app_value = []
negdict = {}
posdict = {}
for t in text:
    t = re.split(" +\s", t)
    for i in t:
        y = re.findall("[.]", i)
        if y:
            if i != "":
                app_value.append(i)
        else:
            if i != "":
                app_key.append(i)

for k in range(len(app_key)):
    if app_key[k] in negdict:
        posdict[app_key[k]] = app_value[k]
    else:
        negdict[app_key[k]] = app_value[k]

for t in text1:
    if t != "":
        tsplit = t.split(" ")
        negmultiple = 1
        posmultiple = 1
        for q in tsplit:
            if q != "":
                if q in negdict:
                    negmultiple *= (float(negdict[q]))
                if q in posdict:
                    posmultiple *= (float(posdict[q]))

        if negmultiple > posmultiple:
            print("Negative Reviews", t)
        else:
            print("Positive Reviews", t)
