import math
p = int(input())
x = int(input())
y = int(input())
px = round(x / 100 * p, 2)
py = math.floor(y / 100 * p)
xr = round((x + px - int(x + px)) * 100)
yi = round((y + py + xr) % 100)
xi = x + px + (y + py + xr) // 100
print(int(xi), int(yi))
