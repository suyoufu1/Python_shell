import os
def auto():
    data = "requirements.txt"
    re = open(data,'r',encoding="utf8")
    for line in re.readlines():
        os.system("pip install "+line)
auto()