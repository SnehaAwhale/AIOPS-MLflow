import os

p1s=[1,4,7,8]
p2s=[2,5,8,0]

for p1 in p1s:
    for p2 in p2s:
        print(f"logging exp for p1:{p1},p2:{p2}")
        os.system(f"python demo.py -p1 {p1} -p2 {p2}")