import random
import sys
import json

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
va = sys.argv
print(va)
if len(va)==1:
    #print("Nice!")
    R = random.randint(71, 121)
else:
    if is_int(va[1]) and 50<int(va[1])<150:
        #print(va[1])
        R=int(va[1])
    else:
        #print("ERROR")
        sys.exit("Ошибочка")
#R=97
R1=R
R+=1
r=(bin(R))[2:]
#print("R: "+r)
s=0
for i in range(len(r)-2):
    s=s+int(r[i])
#print(s)
flag=" "
while flag!="Ok":
    if r[-2:]=="00":
        if is_int(R/4) and s%2==0:
            #print(R/4)
            answer=R/4
            flag = "Ok"
    elif r[-2:]=="10" and s%2==1:
        if is_int((R-2)/4):
            #print((R-2)/4)
            answer=(R-2)/4
            flag = "Ok"
    R+=1
    r=(bin(R))[2:]
#print(bin(21))
str1="На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом."
str2="\n\t1.	Строится двоичная запись числа N."
str3="\n\t2.	К этой записи дописываются справа ещё два разряда по следующему правилу:"
str4="\n\t\tа)	складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа (справа). Например, запись 10000 преобразуется в запись 100001;"
str5="\n\t\tб)	над этой записью производятся те же действия — справа дописывается остаток от деления суммы цифр на 2."
str6="\nПолученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R."
str7="\nУкажите такое наименьшее число N, для которого результат работы алгоритма больше "+str(R1)+". В ответе это число запишите в десятичной системе счисления."
st0=str1+str2+str3+str4+str5+str6+str7
#print(st0,answer)
f1=[st0,answer]
f=json.dumps(f1)
print(f)
