import re

s = "http://www.baidu.com/sub/index.htm"

p = r"(\w(\w(\w)))"

m = re.findall(p, s)

print(m)
