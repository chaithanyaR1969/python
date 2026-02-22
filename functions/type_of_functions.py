#no parameter no return values
def add():
    a=10
    b=20
    c=a+b
    print(c)

add()

#no parameter with return values
def add():
    a=10
    b=20
    c=a+b
    return c
res=add()
print(res)

#with parameter no return values
def add(a,b):
    c=a+b
    print(c)
x=10
y=20
add(x,y)

#with parameter with return values
def add(a,b):
    c=a+b
    return c
x=10
y=20
res=add(x,y)
print(res)
