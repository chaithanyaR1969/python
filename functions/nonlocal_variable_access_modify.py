def outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        nonlocal a
        a=100
        d=200
        print(a)
        print(d)
    print(a)
    inner()
    print(a)
outer()
