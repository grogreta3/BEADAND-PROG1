li1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# alma pohar ablak

def nagy(szo):
    elso =0
    ut = 0
    for i in range(len(li1)):
        if szo[0]==li1[i]:
            elso+=i+1
        if szo[1]==li1[i]:
            ut+=i+1
    return abs(int(elso) - int(ut))


def betuk(szo):
    li=[]
    li.append(szo[0])
    if szo[0]==szo[-1]:
        if szo[0]==szo[-2]:
            li.append(szo[-3])
        else:
            li.append(szo[-2])
    else:
        li.append(szo[-1])
    print(li)
    return nagy(li)


def main():
    szavak=input('adj meg három szót szóközzlel elválasztva:').split(' ')
    print(szavak)
    li3=[]
    for i in szavak:
        li3.append(betuk(i))
    print(li3)
    legnagyobb=max(li3)
    print(legnagyobb)

    for i in range(len(li3)):
        if li3[i]==legnagyobb:
            print(szavak[i])

main()
