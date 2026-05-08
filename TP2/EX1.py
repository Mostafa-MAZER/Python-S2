import math
def racine_et_log(x):
    r=math.sqrt(x)
    g=math.log(x)
    print(f"la racine carree de {x} est ={r:.2f}")
    print(f"la logarithme nature de {x} est ={g:.2f}")
print(racine_et_log(2))


def trigo(angle):
    c=math.cos(angle)
    s=math.sin(angle)
    t=math.tan(angle)
    print(f"la cosinus de {angle} est ={c:.3f}")
    print(f"le sinus de {angle} est ={s:.3f}")
    print(f"la tangente de {angle} est ={t:.3f}")
print(trigo(15))

def distance_points(X1,Y1,X2,Y2):
    dis=math.sqrt(((X2-X1)**2)+((Y2-Y1)**2))
    print(f"la distance de les point {X1,Y1,X2,Y2} est ={dis:.2f}")
print(distance_points(1,2,4,6))
