scores = [60, 73, 81, 95, 34]
n = 0
total = 0
for x in scores:
    n += 1
    total += x

avg = total / n

print('total ' + str(total))
print('average ' + str(avg))

## 平均-分數的平方和
s1=0
t1=0
for i in scores:
    s1=(avg-i)*(avg-i)
    t1+=s1

print("(avg-scores)**  " + str(t1) )

##分數的平方和

s2=0
t2=0
for k in scores:
    s2=k*k
    t2+=s2

print('(scores)**  ' + str(t2) )
