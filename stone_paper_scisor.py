import random
x=True
print("************Stone - Paper - Scissor*****************")
while x==True:
    print('Computer choosed!!')
    comp=random.randint(1,3)
    if comp==1:
        comp='st'
    elif comp==2:
        comp='p'
    elif comp==3:
        comp='sc'
    
    a=input('1-->Stone\n2-->Paper\n3-->Scissor\n\tIt`s Your turn:')
    if a=='1':
        a='st'
    elif a=='2':
        a='p'
    elif a=='3':
        a='sc'
    else:
        print('********* Choose any value in 1,2,3 *********')
    def game():
        if comp==a:
            return None
        elif comp=='st':
            if a=='p':
                return True
            elif a=='sc':
                return False
        elif comp=='p':
            if a=='sc':
                return True
            elif a=='st':
                return False
        elif comp=='sc':
            if a=='p':
                return False
            elif a=='st':
                return True
    d=game()
    if d==True:
        print('You Win')
    elif d==False:
        print('You lose')
    elif d==None:
        print('It`s a tie!!')
    print(f'You choose {a}\nComputer choosed {comp}')
    continue