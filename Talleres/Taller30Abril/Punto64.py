total = 0
pasosRestantes = int(input())
while pasosRestantes > 0:
    if pasosRestantes>=5:
        total+=1
        pasosRestantes -= 5
    elif 5>pasosRestantes>=4:
        total+=1
        pasosRestantes-=4
    elif 4>pasosRestantes>=3:
        total+=1
        pasosRestantes-=3
    elif 3>pasosRestantes>=2:
        total+=1
        pasosRestantes-=2
    elif 2>pasosRestantes>=1:
        total+=1
        pasosRestantes-=1
    if pasosRestantes == 0:
        print(total)