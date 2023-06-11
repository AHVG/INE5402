NUMERO_DE_ALUNOS = 5
NUMERO_DE_NOTAS = 3
LIMITE_ENTRE_APROVADO_RECUPERACAO = 5.75
LIMITE_ENTRE_RECUPERACAO_REPROVADO = 2.75

def calcular_media(soma_dos_termos, numero_de_termos):
    return (soma_dos_termos / numero_de_termos)

def situacao_de_aprovacao(media):
    if LIMITE_ENTRE_APROVADO_RECUPERACAO <= media:
        return "Aprovado"
    elif LIMITE_ENTRE_RECUPERACAO_REPROVADO <= media:
        return "Recuperação"
    else:
        return "Reprovado"
    
def programa_principal():
    melhor_media = -1
    soma_medias = 0
    for numero_do_aluno in range(1, NUMERO_DE_ALUNOS + 1):
        
        media = 0
        print(f"\nEntre com as notas do aluno {numero_do_aluno}:")
        for numero_da_nota in range(1, NUMERO_DE_NOTAS + 1):
            nota = float(input(f"Nota {numero_da_nota}: "))
            media += nota
        media = calcular_media(media, NUMERO_DE_NOTAS)
        situacao_do_aluno = situacao_de_aprovacao(media)
        print("Média aluno {}: {:.2f}".format(numero_do_aluno, media))
        print(f"Situação do aluno: {situacao_do_aluno}")
            
        soma_medias += media
        if melhor_media < media:
            melhor_media = media
    
    media_da_turma = calcular_media(soma_medias, NUMERO_DE_ALUNOS)
    situacao_da_turma = situacao_de_aprovacao(media_da_turma)
    
    print("\nMelhor média: {:.2f}".format(melhor_media))
    print("Média da turma: {:.2f}".format(media_da_turma))
    print("Situação da turma: {}".format(situacao_da_turma))
    
programa_principal()