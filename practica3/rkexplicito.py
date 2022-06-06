
import numpy as np
def integrate(F,butcher,x0,y0,xfinal,N):
    aj,bj,cj=[],[],[]
    m=len(butcher)
    for kj in butcher:
        cj.append(kj[0])
        bj.append(kj[2])
        aj.append(kj[1])
    h=(xfinal-x0)/N

    def RK(F,x,y,h):
        K=[]
        for i in range(m):
            sum=0
            for j in range(i):
                sum+=aj[i][j]*K[j]
            K.append(F(x+cj[i]*h,y+h*sum))
        evalRK=0
        for i in range(m):
            evalRK+=bj[i]*K[i]
        return evalRK

    X=np.linspace(x0,xfinal,N+1)
    Y=[y0]
    for n in range(N):
        Y.append(Y[n]+h*RK(F,X[n],Y[n],h))
    return np.array(X),np.array(Y)
