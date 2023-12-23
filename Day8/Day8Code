from math import lcm

lines = open("D:\\AdventOfCode\\Day8\\Day8Input.txt", "r").read().splitlines()

c = '' 
d = {} 
for l in lines:
  if not c: c = l; continue
  if not l: continue
  d[l[:3]] = (l[7:10],l[12:15])

def run(p):
  n = len(c)
  for k in range(50000):
    p = d[p][c[k%n]=='R']
    if p[2]=='Z': break
  return k+1

print(run('AAA'))

r = 1
for p in d.keys():
  if p.endswith("A"):
    r = lcm(r,run(p))
print("Solution 2:",r)