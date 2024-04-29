from math import log, exp as e
import matplotlib.pyplot as plt
import seaborn as sns


def delta_v(v0, m0, m1):
    dv = []
    xx = []
    for x in range(0, 10000):
        dv.append(v0 * log((m0 + x) / (m1 + x)))
        xx.append(x)
    return dv, xx


def delta_v_2(v0, v1, m0, m1, m2, m3):
    dv, xx = [], []
    
    for x in range(0, 10000):
        dv.append(v0 * log((m0+x)/(m1+x)) + v1 * log((m1+m2+x)/(m1+m3+x)))
        xx.append(x)
    return dv, xx

def solve(v0, m0, m1):
    ans = [ ]
    xx3 = [ ]
    for dv in range(1, 1000):
        betta = e(dv/v0)
        solv = (m0 - betta * m1) / (betta - 1)
        ans.append(solv)
        #print(dv, solv)

        xx3.append(dv)
    return ans, xx3
    
    
    
if __name__ == "__main__":
    g0 = 9.81
    v0 = 355 * g0
    m0 = 8400
    m1 = m0 - 6428
    
    v1 = 310 * g0
    m2 = 25828 - m0
    m3 = m2 - 17427
    

    dv, xx = delta_v(v0, m2, m3)
    dv2, xx2 = delta_v_2(v0, v1, m0, m1, m2, m3)
    
    payload, xx3 = solve(v0, m2, m3)



    #plt.plot(dv, color="red")
    plt.scatter(xx, dv, 0.1, "red")
    plt.scatter(xx2, dv2, 0.1, "blue")

    # plt.scatter(xx3, payload, 0.5, "green")

    
    #plt.grid()
    plt.show()
