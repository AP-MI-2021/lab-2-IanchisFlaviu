def baza10(numar):
    '''Transforma un numar din baza 10 in baza 2
    param: un numar in baza 10
    :return: numarul in baza 2'''
    rez = 0
    putere = 1
    while numar!=0:
         rest= numar % 2
         rez = rez + rest*putere
         putere = putere * 10
         numar = numar//2
    return rez




def este_palindrom(numar):
    '''
    Verifica daca un numar este palindrom
    :param numar: un numar intreg
    :return: True,daca numarul este palindrom
             False,daca nu este palindrom
    '''

    temp = numar
    oglindit = 0
    while numar>0:
        cif = numar%10
        oglindit = oglindit*10+cif
        numar = numar // 10
    if temp == oglindit:
        return True
    else:
        return False

def test_este_palindrom():
    assert este_palindrom(33)== True
    assert este_palindrom(121)== True
    assert este_palindrom(45) == False


def prim(x):
    '''
    Determina daca un numar este prim sau nu
    Intput:un numar intreg dat de la tastatura
    Output:mesajul: numarul este prim sau nu
    '''
    ok = True
    if x<2:
        ok = False
    else:
        for i in range(2,x//2+1):
            if x%i==0:
                ok= False

    return ok

def ultim_prim(x):
    '''
    Functia determina cel mai mare numar prim mai mic decat un numar dat x
    :param x:numarul dat,citit de la tastatura
    :return: cel mai mare numar prim mai mic decat x
    '''

    for n in range(x-1,1,-1):
        if prim(n)==True:
            return n

def test_ultim_prim(x):
    assert ultim_prim(5)==3
    assert ultim_prim(8)==7
    assert ultim_prim(10)==7
    assert ultim_prim(3)==2



def print_menu():
    print('1.Verifica daca un numar este palindrom')
    print('2.Gaseste ultim prim ')
    print('3.Tranforma din baza 10 in baza 2')
    print('4.Exit')

def main():

    while True:
        print_menu()
        opt = int(input('Dati optiunea '))
        if opt == 1:
            numar = int(input('Dati numarul '))
            print(este_palindrom(numar))
        elif opt == 2:
            x = int(input('Dati numarul '))
            a = ultim_prim(x)
            if not a:
                print('Nu exista numar prim mai mic decat ',2)
            else:
                print('Numarul prim este',a)
        elif opt == 3:
            numar = int(input('Dati numarul '))
            print(baza10(numar))
        elif opt == 4:
            break

        else:
            print('Optiune invalida')

main()

