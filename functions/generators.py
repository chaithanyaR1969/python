def generator():
    yield 1
    yield 2
    yield 3
res4=generator()
print(res4)
print(next(res4))
print(next(res4))
print(next(res4))
print(next(res4))
