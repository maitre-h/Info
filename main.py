#Exercice 6
import random
name = input("Votre nm et prenom : ")
cin = input("Votre CIN : ")
t = name.find(" ")
k = random.randint(0,t-1)
p = random.randint(t+1,len(name))
d = random.randint(1000,9999)
mdp = name[k]+name[p]+str(d)
username = name[t+1:t+4]+cin[0:2]+str(ord(name[0]))+str(ord(name[t-1]))
print(username)
print(mdp)

#Exercice 5
nombre = input("Entrer un nombre : ")
k = 0
t = 0
for i in range(0,len(nombre)):
    if(i%2 == 0):
        k = k+int(nombre[i])
    else:
        t = t+int(nombre[i])
m = t - k
if(m%11 == 0):
    print("Nombre divisible par 11")
else:
    print("nombre indivisible")

#Exercice 4
l = []
k = 0
for i in range(1,400):
    for n in range(1,i):
        if(i%n == 0):
            k += 1
    if(k == 1):
        l.append(i)
    k = 0

for i in range(0,len(l)):
    print(l[i],end=' ')

#Exercice 3
import random
k = random.randint(0,20)
s = []
p=0
for i in range(0,k):
    l = random.randint(0,10)
    print(l)
    if(i%3 == 0 or i==0):
        h = l
    if(i==1 or i==k-1):
        if(p+1== l):
            s.append(l)
    else:
        if(h+2 == l and p+1 == l):
            s.append(l)
    p = l
print(s)

#Exercice 2
n = input("Entrer votre list : ")
s = 0
for i in range(0,len(n)):
    if(n[i] == " "):
        s = s+int(n[i-1])
    if(n[i]=="-1"):
        break
print(s)

#Exercice 1
import random
n = random.randint(0,100)
m = True
for i in range(0,8):
    k = int(input(f"proposition {i} :"))
    if(k==n):
        print(f"vous avez reussi en {i} essai")
        m = False
        break
    elif(k<n):
        print("Trop petit !")
    else:
        print("Trop Grand !")
if m:
    print(f"Perdu le nombre cherche est : {n}")