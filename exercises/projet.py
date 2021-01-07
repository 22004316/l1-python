t = 0
y = 0
p = 0
n = 1

def nombre(x):
        global t,p,n
        if p==0:
                t=t*10+x
        else:
                t=t+x/(10**(n))
                n=n+1
        z.set(str(t))