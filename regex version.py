import re
lin = 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print(y)


import re
lin = 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^from .*@([^ ]*)',lin)
print(y)

