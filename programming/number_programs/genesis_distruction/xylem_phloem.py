n=int(input('enter number: '))
n_str=str(n)
first_last=int(n_str[0])+int(n_str[-1])
s=0
for i in n_str[1:len(n_str)-1]:
    num=int(i)
    s=s+num
if  first_last==s:
    print("xylem")
else:
    print("phloem")