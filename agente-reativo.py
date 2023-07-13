import random
import time

# definindo as posições dos objetos e da lixeira
start_time = time.time() # obtém o tempo de início da execução
lixos_org = []
lixos_rec = []
lixo_coletado = 0
for i in range(10):
    pos = (random.randint(0, 19), random.randint(0, 19))
    lixos_org.append(pos)
for i in range(5):
    pos = (random.randint(0, 19), random.randint(0, 19))
    lixos_rec.append(pos)
lixeira = (19, 19)

# definindo a posição inicial da IA
pos_ia = (0, 0)

# loop principal
while True:
    # limpando a tela
    print("\033c", end="")

    # desenhando o espaço
    for y in range(20):
        for x in range(20):
            if (x, y) == lixeira:
                print("L", end="")
            elif (x, y) in lixos_org:
                print("O", end="")
            elif (x, y) in lixos_rec:
                print("R", end="")
            elif (x, y) == pos_ia:
                print("I", end="")
            else:
                print(".", end="")
        print()

    # verificando se a IA está na posição da lixeira
    if pos_ia == lixeira:
        if len(lixos_rec) == 0 and len(lixos_org) == 0:
            print("Parabéns, a IA coletou todo o lixo!")
            end_time = time.time() # obtém o tempo de fim da execução
            print("Ambiente completamente limpo em", '{0:.2f}'.format(end_time - start_time), "segundos!")
            break
        else:
            lixo_coletado = 0
            print("IA jogou o lixo na lixeira!")

    if lixo_coletado == 0:    
        # calculando a posição do lixo mais próximo
        if len(lixos_org) != 0 or len(lixos_rec) != 0:
            lixos = lixos_rec if len(lixos_rec) > 0 else lixos_org
            distancias = [abs(pos_ia[0] - lixo[0]) + abs(pos_ia[1] - lixo[1]) for lixo in lixos]
            index_proximo = distancias.index(min(distancias))
            lixo_proximo = lixos[index_proximo]
            # movendo a IA em direção ao lixo mais próximo
            dx = 0
            dy = 0
            if lixo_proximo[0] > pos_ia[0]:
                dx = 1
            elif lixo_proximo[0] < pos_ia[0]:
                dx = -1
            if lixo_proximo[1] > pos_ia[1]:
                dy = 1
            elif lixo_proximo[1] < pos_ia[1]:
                dy = -1
            pos_ia = (pos_ia[0] + dx, pos_ia[1] + dy)
            # verificando se a IA pegou um lixo
            if pos_ia in lixos_rec:
                lixo_coletado = 1
                lixos_rec.remove(pos_ia)
                print("IA pegou um lixo reciclável!")
            elif pos_ia in lixos_org:
                lixo_coletado = 1
                lixos_org.remove(pos_ia)
                print("IA pegou um lixo orgânico!")
            time.sleep(0.2)
    else:
        # movendo a IA para a Lixeira
        dx = 0
        dy = 0
        if lixeira[0] > pos_ia[0]:
            dx = 1
        elif lixeira[0] < pos_ia[0]:
            dx = -1
        if lixeira[1] > pos_ia[1]:
            dy = 1
        elif lixeira[1] < pos_ia[1]:
            dy = -1
        pos_ia = (pos_ia[0] + dx, pos_ia[1] + dy)
        if pos_ia in lixos_rec:
            print("A IA está com o coletor cheio.")
        elif pos_ia in lixos_org:
            print("A IA está com o coletor cheio.")
        time.sleep(0.2)