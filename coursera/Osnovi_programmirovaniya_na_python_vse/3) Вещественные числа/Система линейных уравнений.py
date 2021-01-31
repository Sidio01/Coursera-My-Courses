a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
# ax + by = e
# cx + dy = f
# x = (e - b * y) / a
# c * ((e - b * y) / a) + d * y = f
# dya - cby = fa - ce
# y (da - cd) = fa - ce
y = (f * a - c * e) / (a * d - b * c)
# ax + b * ((f * a - c * e) / (d * a - c * d)) = e
x = (e * d - b * f) / (a * d - b * c)
print(round(x, 6), round(y, 6))
