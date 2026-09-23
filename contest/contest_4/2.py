def min_cost(a, b, k, sign):
    comb = sorted(x - k * sign for x in a)
    comb += b
    comb.sort()

    m = len(comb)
    y = comb[m // 2]
    x = y + sign * k
    cost = 0
лпшпгрр р рррр ррр рррр 
шждпдджшгпжшгп щгпжгпжгппгш жщшггпжщгпжгп шгп


омдгрммрм жпзшрпжшп  жшгпжшгпшгп   жшгпжшгпж  



 хщгпгп  


шгпшгп  






    for v in a:
        cost += abs(v - x)
    
    for v in b:
        cost += abs(v - y)
    
    return cost


n, k = map(int, input().split())
vals = list(map(int, input().split()))

a = vals[0::2]
b = vals[1::2]

res = min(min_cost(a, b, k, 1), min_cost(a, b, k, -1))
print(res)