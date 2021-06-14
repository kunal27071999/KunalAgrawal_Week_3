def decor(func):
    def inner_function(x,y):
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        return func(x,y)
    return inner_function


def add(a,b):
    res = a + b
    return res

@decor
def sub(a,b):
    res = a- b
    return res

# GENERATORS 

# def m():
#     yield 'mahesh'
#     yield 'suresh'

def m(x,y):
    while x<=y:
        yield x
        x+=1


# g = m()
# print(g)
# print(type(g))

# for y in g: 
#     print(y)

g = m(5,10)
for y in g:
    print(y)

add = decor(add)
print(add(20,30))
print(add(-10,5))
print(sub(30,10))
print(sub(10,-5))


