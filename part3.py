from math import sqrt

n = sqrt(3.0)
tolerance = 1e-9  # 허용 오차

if abs(n*n - 3.0) < tolerance:
    print("sqrt(3.0)*sqrt(3.0)은 3.0과 거의 같다")
else:
    print("sqrt(3.0)*sqrt(3.0)은 3.0과 같지 않다")
