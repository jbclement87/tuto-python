def volboite(x1=10 , x2=10, x3=10):
    v = x1 * x2 * x3
    return(v)

def maximum(n1, n2, n3):
    m=0
    if n1>n2 and n1>n3:
        m = n1
    if n2>n1 and n2>n3:
        m = n2
    if n3>n1 and n3>n2:
        m = n3
    return(m)

print(volboite(5.2, 3))