import re

my_sub = re.sub(r"\s","_","I love python programming language")
print(my_sub)

my_sub2 = "Bienvenue dans notre cours"
print(re.sub(r"\s","-",my_sub2))