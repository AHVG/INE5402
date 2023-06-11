"""
ARVORE = {
          'vertebrado':
          {
              'ave':
              {
                  'carnivoro': 'aguia',
                  'onivoro': 'pomba'
              },
              'mamifero':
              {
                  'onivoro': 'homem',
                  'herbivoro': 'vaca'
              }
          },
          'invertebrado':
          {
              'inseto':
              {
                  'hematofago': 'pulga',
                  'herbivoro': 'lagarta'
              },
              'anelideo':
              {
                  'hematofago': 'sanguessuga',
                  'onivoro': 'minhoca'
              }
          }
         }

filo   = input()
classe = input()
animal = input()

print(ARVORE[filo][classe][animal])
"""

filo   = input()
classe = input()
tipo   = input()

if filo == "vertebrado":
    if classe == "ave":
        if tipo == 'carnivoro':
            print("aguia")
        elif tipo == 'onivoro':
            print("pomba")
        else:
            print("Valores inválidos")
    elif classe == "mamifero":
        if tipo == "onivoro":
            print("homem")
        elif tipo == "herbivoro":
            print("vaca")
        else:
            print("Valores invalidos")
elif filo == "invertebrado":
    if classe == "inseto":
        if tipo == 'hematofago':
            print("pulga")
        elif tipo == 'herbivoro':
            print("lagarta")
        else:
            print("Valores inválidos")
    elif classe == "anelideo":
        if tipo == "hematofago":
            print("sanguessuga")
        elif tipo == "onivoro":
            print("minhoca")
        else:
            print("Valores invalidos")
else:
    print("Valores invalidos")
