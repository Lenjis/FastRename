import os

path1 = "a_b_c_100"
path2 = "a_b_c_200"
names1 = path1.split("_")
last_name1 = names1[-1]
names2 = path2.split("_")
last_name2 = names2[-1]
os.rename(path2, path2.replace(last_name2, str(int(last_name1) + int(last_name2))))
