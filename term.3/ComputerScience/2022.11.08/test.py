import re

ch_list = ["Apple", "Lemon", "Melon", "Watermelon"]
ptn = re.compile("^.....$")

ptnn = re.search(ptn, ch_list)
print(ptnn.group(1))
