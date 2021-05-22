
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

print(f"\nDiscount Factors: \
    {bond_price_zero_rate(n, t_cf, v_cf, r_zero)[0]} \nBond Price: {bond_price_zero_rate(n, t_cf, v_cf, r_zero)[1]}\n")

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
print(f"Par yield: {mid:.2%}\n")


def integrate_midpoint_rule(a, b, n, f_int):
    """
    Code for implementing numerical integration using mid point rule

    Args:
        a (int): left endpoint of the integration interval
        b (int): right endpoint of the integration interval
        n (int ): number of partitions
        f_int (function): routine evauation f(x)
    """
    h = (b - a) / n
    i_midpoints = np.array(a+(np.linspace(1,n,n)-1/2)*h)
    return h*sum([f_int(x) for x in i_midpoints])

print(f"Numerical Integration value using Mid-Point rule:\
    {integrate_midpoint_rule(a=0 , b=2, n=4, f_int = lambda x: np.exp(-1*(x**2))):.8}\n")