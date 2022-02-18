


def point(x1,y1,x2,y2,x3):
    y=(y1-y2)
    x=(x1-x2)
    a=(y1-y2)/(x1-x2)
    b=y1-a*x1
    _b=y1*x-x1*y
    if b>=0:
        c='+'
    else:
        c='-'
    print('Y='+str(a)+'X'+c+str(b))
    return a*x3+b
    #print('Y=('+str(y)+'/'+str(x)+')X'+c+'('+str(_b)+'/'+str(x)+')')

print(point(1723,590,1514,565,1635))
print(point(1187,810,1219,818,1267))


