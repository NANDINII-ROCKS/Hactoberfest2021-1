'''
SET OPERATIONS
 
'''
Total=[]
cricket=[]
badminton=[]
football=[]
CB=[]
CB_NB=[]
n=cricket+badminton
list2=[]
FB=[]
list1=[]
CBF=[]
CF_NB=[]
last=[l for l in CF_NB if l not in CBF]
t=cricket+badminton+football

tot=int(input("Enter total number of students:"))
for i in range(tot):
    temp=int(input())
    Total.append(temp)
print(Total)

c=int(input("Enter total number of students who play Criket:"))
print("Enter Roll Numbers who play Criket:")
for i in range(c):
    temp=int(input())
    cricket.append(temp)
print(cricket)

b=int(input("Enter total number of students who play Badminton:"))
print("Enter Roll Numbers who play Badminton:")
for i in range(b):
    temp=int(input())
    badminton.append(temp)
print(badminton)

f=int(input("Enter total number of students who play Football:"))
print("Enter Roll Numbers who play Football:")
for i in range(f):
    temp=int(input())
    football.append(temp)
print(football)

def both_c_and_b():
    for i in range(len(cricket)):
        for j in range(len(badminton)):
            if cricket[i]==badminton[j]:
                CB.append(cricket[i])
    return CB

def c_or_b(): 
    n=cricket+badminton 
    for x in n:
        if x not in list1:
            list1.append(x)
    return list1

def either_c_or_b_not_both():
    n=cricket+badminton
    c_n_b=both_c_and_b()
    CF_NB=[]
    for i in n:
        if i in c_n_b:
            continue 
        else:
            CB_NB.append(i)
    return CB_NB
    

def neither_c_nor_b():
    NCNB=[]
    t=cricket+badminton+football
    l4 = [k for k in t if k not in list1]
    NCNB.append(l4)
    return NCNB
    


def cfb():
    CBF=[]
    for q in range(len(cricket)):
        for w in range(len(badminton)):
            for o in range(len(football)):
                if cricket[q]==badminton[w]==football[o]:
                    CBF.append(cricket[q])
    return CBF

def c_and_f_not_b():
    z=cfb()
    CBF=[]
    CF_NB=[]

    for i in range(len(cricket)):
        for j in range(len(football)):
            if cricket[i]==football[j]:
                CF_NB.append(cricket[i])
           
    last=[l for l in CF_NB if l not in badminton]
    
    return last

def both_f_and_b():
    for i in range(len(football)):
        for j in range(len(badminton)):
            if football[i]==badminton[j]:
                FB.append(football[i])
    return FB

def only_c(cricket,FB):
    FB=[]
    li_dif = [i for i in cricket + FB if i not in cricket or i not in FB]
    return li_dif

def only_f(football,CB):
    CB=[]
    li = [i for i in football + CB if i not in football or i not in CB]
    return li

def no_game(Total,t):
    t= cricket + badminton + football
    NoG = [i for i in Total + t if i not in Total or i not in t]
    return NoG



print("1] Both Cricket and Badminton:",both_c_and_b())
print("2] Who play either Criket or Badminton not both :", either_c_or_b_not_both())
print("*] Criket Or Badminton:",c_or_b())
print("*] All C and F and B:",cfb())
print("3] Neither Cricket nor badminton:",neither_c_nor_b())
print("4] Cricket and Football but not Badminton",c_and_f_not_b())
print("*] F and B:",both_f_and_b())
print("5] Students who play only Cricket:",only_c(cricket,FB))
print("6] Students who play only football:",only_f(football,CB))
print("7] No Game :",no_game(Total,t))



