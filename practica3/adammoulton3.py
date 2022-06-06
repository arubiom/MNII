
def integrate(F,x0,y0,xfinal,N):
    
    import numpy as np
    
    def AM3(F,x0,y0,y1,y2,y3,h):
        return 9/24*F(x0+3*h, y3) + 19/24*F(x0+2*h, y2) - 5/24*F(x0+h, y1) + 1/24*F(x0, y0)
    
    X = np.linspace(x0,xfinal,N+1)
    h = (xfinal-x0)/N
    Y = [y0]
    for i in range(3-1):  # num_pasos - 1
        y1 = y0 + h*F(x0,y0)
        Y.append(y1)
        y0 = y1
        
    for n in range(N-1):
        Y.append(sp.solve(Y[n]+h*AM3(F,X[n],Y[n],Y[n+1],Y[n+2],y3,h)-y3,y2)[0])
    return np.array(X),np.array(Y)
