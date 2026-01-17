import random
def mc_area_x2(a, b, n):
    y_max = max(a*a, b*b)
    hits=0
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, y_max)
        if y <= x*x:
            hits += 1
    return (hits/n)*(b-a)*y_max

def actual_area(a, b,):
    return (1/3)*((b**3)-(a**3))
area1=mc_area_x2(0, 2, 100000)
area2=actual_area(0, 2, 4)
print(f"area by monte-carlo method: {area1}")
print(f"actual area: {area2}")