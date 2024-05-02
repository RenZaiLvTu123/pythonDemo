import re

s = "<div><span>包含信息</span></div>"
p = r"((<)+/+\w+(?(2)>))"
m = re.findall(p,s)
print(m)
