
import numpy as np

def bond_price_zero_rate(n, t_cf, v_cf, r_zero):
    
    """
    Code to generate the bond price given the zero rate curve

    Args:
        n (int): number of cash flows
        t_cf (array): vector of cash flow dates (of size n)
        v_cf (array): vector of cash flows (of size n)
        r_zero ([type]): [description]
    """
    disc = np.exp(-1 * r_zero * t_cf)
    return (disc, sum(v_cf * disc))

n = 4
t_cf = np.array([6/12, 12/12, 18/12, 24/12])
v_cf = np.array([2.5,2.5,2.5,102.5])

r_zero = np.array([0.05, 0.0525, 0.0535, 0.055])

print(f"\nDiscount Factors: {bond_price_zero_rate(n, t_cf, v_cf, r_zero)[0]} \nBond Price: {bond_price_zero_rate(n, t_cf, v_cf, r_zero)[1]}\n")

f = lambda C : sum(C * np.exp(-1 * r_zero[:-1] * t_cf[:-1])/2) + ( 1 + C/2) * np.exp(-1 * r_zero[-1] * t_cf[-1])

a = 0
b = 1
tol = abs(1-f((b-a)/2))
while abs(tol) >= 0.000001:
    mid = (b+a)/2
    left = (mid+a)/2
    right = (b+mid)/2

    if abs(1-f(left)) < abs(1-f(right)):
        b=mid
        tol = abs(1-f(left))
    elif abs(1-f(left)) > abs(1-f(right)):
        a=mid
        tol = abs(1-f(right))
    else:
        print('Values equal')
        print(tol)
        break
print(f"\nPar yield: {mid:.2%}\n")


    