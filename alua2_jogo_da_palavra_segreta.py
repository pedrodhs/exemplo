# import os 

# palavra_secreta='pedro'

# letrtas_acertadas =''

# numero_de_tentativas=0

# while True:

#     letra_digitada=input('digite uma letra: ')
#     numero_de_tentativas+=1


#     if len(letra_digitada) >1:
#         print('você só pode digitar apenas uma letra pro vez!!')
#         continue

#     if letra_digitada in palavra_secreta:
#         letrtas_acertadas +=letra_digitada
    
#     palavra_formada=''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letrtas_acertadas:
#             palavra_formada+=letra_secreta
        
#         else:
#             palavra_formada+='*'
#     print(f"palavra formada:, {palavra_formada}")
#     if palavra_formada== palavra_secreta:
#         os.system ('cls')
#         print("você ganhou parabens")
#         print(f" A palavra era {palavra_secreta}")
#         print(f"tentativas:{numero_de_tentativas}")
#         letrtas_acertadas= ''
#         numero_de_tentativas=0


# palavra_secreta = "lucas"
# letra_acertadas = ''

# while True:
#     letra_digitada=input('digite uma letra: ')

#     if len (letra_digitada) >1:
#         print("digite apenas uma letra") 
#         continue
#     if letra_digitada in palavra_secreta:
#         letra_acertadas +=letra_digitada
#     palavra_fromada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letra_acertadas:
#             palavra_fromada+=letra_secreta
#     else:
#         palavra_fromada +='*'
#     print(f"A palavra era {palavra_fromada}")
    








# palavra_secreta="victor"
# letras_acertadas=''

# while True:
#     letra_digitada=input("digite uma letra: ")

#     if len(letra_digitad)>1:
#         print("digite apena uma letra!!!")
#         continue
#     if letra_digitada in palavra_secreta:
#         letras_acertadas+=letra_digitada
#     palavra_formada=''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada+=letra_secreta



import os


palavra_secreta= 'vento'
        
letras_acertadas=''

numero_de_tentativas=0
while True:
    letra_digitada=input("digite uma letra: ")
    numero_de_tentativas+=1
    if len (letra_digitada) >1:
        print('digite apenas uma letra!!!')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas+=letra_digitada
    palavra_formada =''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada+=letra_secreta
        else:
            palavra_formada += '*'
    print(f"a palavra é {palavra_formada}")
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('você gonhou!!! parabens')
        print(f'a palavra era {palavra_secreta}')
        print(f'tentativas {numero_de_tentativas}')
        

