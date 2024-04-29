from math import log, exp as e
    
def solve(a, b, dv, *data):
    ERR = 1e-4
    MAX_ITER = 100_000
    
    # _stack = []
    # _ord = []
    
    
    if func(a, dv, *data) == 0:
        return a
    
    elif func(b, dv, *data) == 0:
        return b
    
    for _ in range(MAX_ITER):
        
        dx = (b-a)/2.
        c = a + dx
        
        if sign(func(a, dv, *data)) != sign(func(c, dv, *data)):
            b = c
        else:
            a = c
            
        if(b - a) < ERR:
            break
        
        # _stack.append(c)
        # _ord.append(func(c, dv, *data))
        
    return round(c,3) #,_stack,_ord
    
    
    

def func(x,dv,*args):
    lenght = args.__len__() // 3
    if(lenght == 1):
        return args[0] * log((args[1]+x)/(args[2]+x)) - dv
    
    elif(lenght == 2):
        return args[0] * log((args[1]+x)/(args[2]+x)) + args[3] * log((args[4]+x)/(args[5]+x)) - dv
    
    elif(lenght == 3):
        return args[0] * log((args[1]+x)/(args[2]+x)) + args[3] * log((args[4]+x)/(args[5]+x)) + args[6] * log((args[7]+x)/(args[8]+x)) - dv


if __name__ == "__main__":
    g0 = 9.81
    v0 = 355 * g0
    m0 = 8.4
    m1 = m0 - 6.428

    # v1 = 310 * g0
    # m2 = 25828 - m0
    # m3 = m2 - 17427
    
    # m0 = 104.8
    # m1 = 40.8
    # v0 = 302*g0
    
    # m2 = 21.3
    # m3 = 5.3
    # v1 = 310 * g0

    max_payload = solve(0,3000,3200,v0,m0,m1)
    print(f"Max payload: {max_payload*0.9} < {max_payload} < {max_payload*1.1} t") #+- 10% err
    

