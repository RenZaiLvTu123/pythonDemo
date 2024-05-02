t = int(input("请输入幂数："))
if t <= 0:
    t = 8
w = 6
print("%*s" % (int((t-1)*w/2), ""), end="")
print("{0:^{1}}".format(1, w))
line = [1, 1]
print("%*s" % (int((t-2)*w/2), ""), end="")
for i in line:
    print("{0:^{1}}".format(i, w), end="")
print("")
for i in range(2, t):
    r = []
    for j in range(0, len(line)-1):
        r.append(line[j]+line[j+1])
    line = [1]+r+[1]
    print("%*s" % (int((t-i-1)*w/2), ""), end="")
    for k in line:
        print("{0:^{1}}".format(k, w), end="")
    print("")
