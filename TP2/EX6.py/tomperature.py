import conversion
x=float(input("donner la valeur de temperature : "))
n=input("donner l'unite de mesure que vous souhaitez convertir en (c ou f)").upper()

if n=='C':
    c=conversion.fahrenheit_vers_celsius(x)
    print(f"la temperature est {c:.2f}°C")
elif n=='F':
    f=conversion.celsius_vers_fahrenheit(x)
    print(f"la temperature est {f:.2f}°F")
