# coding: UTF-8
s1 = "パトカー"
s2 = "タクシー"
s: str = ""

for i in range(len(s1)):
    s += s1[i]+s2[i]
    
print(s)