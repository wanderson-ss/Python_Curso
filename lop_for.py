"""_summary_
Loop for 

Loop -> Estrutura de repetição 
For -> Uma dessas estruturas 

C ou Java 

for sera para 

for(INT I = 0; i < limitador; i++){
    //execução do loop
} 

#Python

for intem in interavel:
    //execução do loop    

Utilizamos o loops para iterar sequencias ou sob valores iteráveis 
-String
    nome = 'wanderson'
-Lista 
    lista =[1,2,3,4,5,6,7,8,9]
Range
    numeros = range (0,1)    
    
"""
"""
nome = 'wanderson'
lista = [1,3,5,7,9]
numeros = range (1,10) #trasnformar em lista

#exemplo de for 1(Iterando sobre uma string)
for letra in nome:
    print(letra)
    
#exemplo de for 2(Iterando sobre uma lista)

for numeros in lista:
    print(numeros)

#exemplo de for 3(Iterando sobre um range )


 range(valor inicial, valor final )
 OBS: O valor final não é inclusive, no caso de 01 a 10 ele vai até o 09. 
    
for numero in range(1,10):
    print(numero)

    

#for _, letra in enumerate(nome):
 #   print(letra)
OBS: Quando não precisamos de um valor podemos descartalos utilizando o 
"_"



for valor in enumerate(nome):
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd):
    print(f'imprimindo{n}')
    
     
 Mais um exemplo    
    
    
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num =  int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print (f'A soma é {soma}')    


print com uma letra acima de outra 
nome = 'Wanderson'
for letra in nome:
    print(letra)
    
    
    
nome = 'Wanderson'
for letra in nome:
    print(letra, end='')
#Imprime os caracteres sem pular linha 

""" 


 
 
""""""
#Transformando em indicie 


nome = 'Wanderson'
for letra in nome:
    print(letra)

