def pangkat(x, y):
    out = 1
    for i in range(y):
        out *= x
    print(out)
pangkat(2,2)


def pangkatB(x, y):
    if(y == 1):
        return x
    else:
        return x * pangkatB(x, y-1)
print(pangkatB(2,3))
