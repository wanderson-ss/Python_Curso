
#Estruturas logicas 

"""
and(e);or (ou) , not(não), is(é)    

Operadores unários:
    -not
Operadores binários:
    -and,or,is   
    
    Regras de funcionamento:
    
Para o 'and', ambos valores precisam ser TRUE    
ativo= True
logado = True

Para o 'or',um ou outro o valor precisa ser TRUE
ativo= False
logado = True

Para o 'Not',o valor do boolean é invertido, se for true vira False e se for false vira True
Sempre será ao contrario

Para o is, o valor sempre será false
    
"""

ativo= False
logado = False

#se não estiver ativo: 
if ativo :
    print('vc precisa ativar sua conta.Cheque seu e-mail')
else:
    print('Bem vindo usuário')    

# ativo é falso?
print(ativo is True)