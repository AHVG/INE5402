guarda_chuvas_em_casa_para_comprar = 0
guarda_chuvas_no_trabalho_para_comprar = 0

guarda_chuvas_em_casa = 0
guarda_chuvas_no_trabalho = 0

dias = int(input())
for i in range(0, dias):
    
    ida, volta = [x for x in input().split()]
    
    if ida[0] == 'c':
        if guarda_chuvas_em_casa == 0:
            guarda_chuvas_em_casa_para_comprar += 1
        else:
            guarda_chuvas_em_casa -= 1
        guarda_chuvas_no_trabalho += 1
    if volta[0] == 'c':
        if guarda_chuvas_no_trabalho == 0:
            guarda_chuvas_no_trabalho_para_comprar += 1
        else:
            guarda_chuvas_no_trabalho -= 1
        guarda_chuvas_em_casa += 1
    print(guarda_chuvas_em_casa_para_comprar, guarda_chuvas_no_trabalho_para_comprar)
            

