import math
def solution(numer1, denom1, numer2, denom2):
    denom3 = denom1 * denom2
    numer3 = numer1*denom2 + numer2*denom1

    gcd = math.gcd(denom3, numer3)

    return [numer3//gcd, denom3//gcd]