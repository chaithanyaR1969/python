str1=input("enter string")
out=""
for i in str1:
    if i==" ":
        out=out+"_"
    else:
        out = out + i
print(out)