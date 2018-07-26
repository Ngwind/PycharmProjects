y = 0
# using for
for i in range(101):
    y = y + i
print(y)
# using while
z = 0
x = 0
while x < 101:
    z = z + x
    x = x + 1
    if x > 10:
        break
    print("end",x,z)

print(z)
