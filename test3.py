import re

s = "a1b2c3d"

p = r"\d+"

pattern = re.compile(p)

m = pattern.subn("5", s,5)

print(m)
