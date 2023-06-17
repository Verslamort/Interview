def flist(l):
    l.append(0)
    print(id(l))
    print(l)


ll = []
print(id(ll))
flist(ll)
flist(ll)


def fstr(s):
    s += 'a'
    print(s)


ss = 'hehe'
fstr(ss)
fstr(ss)
