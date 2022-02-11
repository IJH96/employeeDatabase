import math #access to sin, cos, pi, etc

def sin(theta):
    result = theta
    delta = theta
    n = 2
    while (delta > 1E-12):
        delta *= (-theta**2)/((2*n-1)*(2*n-2))
        result += delta
        n += 1

    return result #finishes function

theta = float(input("Enter an angle in degrees:"))*math.pi/180
print("Our Function:     ", sin(theta))
print("Library Function:     ", math.sin(theta))
