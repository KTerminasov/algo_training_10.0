# a^n = (a^2)^(n/2) при четном n
# a^n = a * a^(n-1) при нечетном n

def my_pow(num, deg):
    if deg == 1:
        return num
    elif deg % 2 == 0:
        return my_pow(num * num, deg // 2)
    else:
        return num * my_pow(num, deg - 1)


a = int(input())
n = int(input())

print(my_pow(a, n))
print(pow(400, 200))
